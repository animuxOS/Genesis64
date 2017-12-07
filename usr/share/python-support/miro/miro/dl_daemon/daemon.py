from miro.dl_daemon import command
import os
import cPickle
import socket
import traceback
from time import sleep
from struct import pack, unpack, calcsize
import tempfile
from miro import config
from miro import prefs
from miro import eventloop
from miro import util
import logging
from miro.platform.utils import launchDownloadDaemon, killProcess
from miro import signals
from miro import trapcall
from miro.httpclient import ConnectionHandler

SIZE_OF_INT = calcsize("I")

class DaemonError(Exception):
    """Exception while communicating to a daemon (either controller or
    downloader).
    """
    pass

firstDaemonLaunch = '1'
def startDownloadDaemon(oldpid, port):
    global firstDaemonLaunch

    daemonEnv = {
        'DEMOCRACY_DOWNLOADER_PORT' : str(port),
        'DEMOCRACY_DOWNLOADER_FIRST_LAUNCH' : firstDaemonLaunch,
    }
    launchDownloadDaemon(oldpid, daemonEnv)
    firstDaemonLaunch = '0'

def getDataFile():
    try:
        uid = os.getuid()
    except:
        # This works for win32, where we don't have getuid()
        uid = os.environ['USERNAME']
       
    shortAppName = "Miro"
    return os.path.join(tempfile.gettempdir(), ('%s_Download_Daemon_%s.txt' % (shortAppName,uid)))

pidfile = None
def writePid(pid):
    """Write out our pid.

    This method locks the pid file until the downloader exits.  On windows
    this is achieved by keeping the file open.  On Unix/OS X, we use the
    fcntl.lockf() function.
    """

    global pidfile
    # NOTE: we want to open the file in a mode the standard open() doesn't
    # support.  We want to create the file if nessecary, but not truncate it
    # if it's already around.  We can't truncate it because on unix we haven't
    # locked the file yet.
    fd = os.open(getDataFile(), os.O_WRONLY | os.O_CREAT)
    pidfile = os.fdopen(fd, 'w')
    try:
        import fcntl
    except:
        pass
    else:
        fcntl.lockf(pidfile, fcntl.LOCK_EX | fcntl.LOCK_NB)
    pidfile.write("%s\n" % pid)
    pidfile.flush()
    # NOTE: There may be extra data after the line we write left around from
    # prevous writes to the pid file.  This is fine since readPid() only reads
    # the 1st line.
    #
    # NOTE 2: we purposely don't close the file, to achieve locking on
    # windows.

def readPid():
    try:
        f = open(getDataFile(), "r")
    except IOError:
        return None
    try:
        try:
            return int(f.readline())
        except ValueError:
            return None
    finally:
        f.close()

lastDaemon = None

class Daemon(ConnectionHandler):
    def __init__(self):
        ConnectionHandler.__init__(self)
        global lastDaemon
        lastDaemon = self
        self.waitingCommands = {}
        self.returnValues = {}
        self.size = 0
        self.states['ready'] = self.onSize
        self.states['command'] = self.onCommand
        self.queuedCommands = []
        self.shutdown = False
        self.stream.disableReadTimeout = True
        # disable read timeouts for the downloader daemon communication.  Our
        # normal state is to wait for long periods of time for without seeing
        # any data.

    def onError(self, error):
        """Call this when an error occurs.  It forces the
        daemon to close its connection.
        """
        logging.warning ("socket error in daemon, closing my socket")
        self.closeConnection()
        raise error

    def onConnection(self, socket):
        self.changeState('ready')
        for (comm, callback) in self.queuedCommands:
            self.send(comm, callback)
        self.queuedCommands = []

    def onSize(self):
        if self.buffer.length >= SIZE_OF_INT:
            (self.size,) = unpack("I", self.buffer.read(SIZE_OF_INT))
            self.changeState('command')

    def onCommand(self):
        if self.buffer.length >= self.size:
            try:
                comm = cPickle.loads(self.buffer.read(self.size))
            except:
                logging.exception ("WARNING: error unpickling command.")
            else:
                self.processCommand(comm)
            self.changeState('ready')

    def processCommand(self, comm):
        trapcall.timeTrapCall("Running: %s" % (comm,), self.runCommand, comm)

    def runCommand(self, comm):
        comm.setDaemon(self)
        comm.action()

    def send(self, comm, callback = None):
        if self.state == 'initializing':
            self.queuedCommands.append((comm, callback))
        else:
            raw = cPickle.dumps(comm, cPickle.HIGHEST_PROTOCOL)
            self.sendData(pack("I",len(raw)) + raw, callback)

class DownloaderDaemon(Daemon):
    def __init__(self, port):
        # before anything else, write out our PID 
        writePid(os.getpid())
        # connect to the controller and start our listen loop
        Daemon.__init__(self)
        self.openConnection('127.0.0.1', port, self.onConnection, self.onError)
        signals.system.connect('error', self.handleError)

    def handleError(self, obj, report):
        command.DownloaderErrorCommand(self, report).send()

    def handleClose(self, type):
        if self.shutdown:
            return
        self.shutdown = True
        eventloop.quit()
        logging.warning ("downloader: connection closed -- quitting")
        from miro.dl_daemon import download
        download.shutDown()
        import threading
        for thread in threading.enumerate():
            if thread != threading.currentThread() and not thread.isDaemon():
                thread.join()

class ControllerDaemon(Daemon):
    def __init__(self):
        Daemon.__init__(self)
        self.stream.acceptConnection('127.0.0.1', 0, self.onConnection, self.onError)
        self.port = self.stream.port
        startDownloadDaemon(readPid(), self.port)
        data = {}
        remoteConfigItems = [prefs.LIMIT_UPSTREAM,
                   prefs.UPSTREAM_LIMIT_IN_KBS,
		   prefs.LIMIT_DOWNSTREAM_BT,
		   prefs.DOWNSTREAM_BT_LIMIT_IN_KBS,
                   prefs.BT_MIN_PORT,
                   prefs.BT_MAX_PORT,
                   prefs.USE_UPNP,
                   prefs.BT_ENC_REQ,
                   prefs.MOVIES_DIRECTORY,
                   prefs.PRESERVE_DISK_SPACE,
                   prefs.PRESERVE_X_GB_FREE,
                   prefs.SUPPORT_DIRECTORY,
                   prefs.SHORT_APP_NAME,
                   prefs.LONG_APP_NAME,
                   prefs.APP_PLATFORM,
                   prefs.APP_VERSION,
                   prefs.APP_SERIAL,
                   prefs.APP_REVISION,
                   prefs.PUBLISHER,
                   prefs.PROJECT_URL,
                   prefs.DOWNLOADER_LOG_PATHNAME,
                   prefs.LOG_PATHNAME,
                   prefs.GETTEXT_PATHNAME,
                   prefs.LIMIT_UPLOAD_RATIO,
                   prefs.UPLOAD_RATIO
                ]

        for desc in remoteConfigItems:
            data[desc.key] = config.get(desc)
        c = command.InitialConfigCommand(self, data)
        c.send()
        config.addChangeCallback (self.updateConfig)

    def updateConfig (self, key, value):
        if not self.shutdown:
            c = command.UpdateConfigCommand (self, key, value)
            c.send()
            
    def handleClose(self, type):
        if not self.shutdown:
            logging.warning ("Downloader Daemon died")
            # FIXME: replace with code to recover here, but for now,
            # stop sending.
            self.shutdown = True
            config.removeChangeCallback (self.updateConfig)

    def shutdown_timeout_cb(self):
        logging.warning ("killing download daemon")
        killProcess(readPid())
        self.shutdownResponse()

    def shutdownResponse(self):
        if self.shutdown_callback:
            self.shutdown_callback()
        self.shutdown_timeout_dc.cancel()

    def shutdownDownloaderDaemon(self, timeout=5, callback = None):
        """Send the downloader daemon the shutdown command.  If it doesn't
        reply before timeout expires, kill it.  (The reply is not sent until
        the downloader daemon has one remaining thread and that thread will
        immediately exit).
        """
        self.shutdown_callback = callback
        c = command.ShutDownCommand(self)
        c.send()
        self.shutdown = True
        config.removeChangeCallback (self.updateConfig)
        self.shutdown_timeout_dc = eventloop.addTimeout(timeout, self.shutdown_timeout_cb, "Waiting for dl_daemon shutdown")
