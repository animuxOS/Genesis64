# This is a generated file. Do not edit.
from StringIO import StringIO
from string import Template
from miro.xhtmltools import urlencode
from miro.frontends.html.template import Handle, fillAttr, quoteAndFillAttr, fillStaticTemplate
from miro.util import quoteattr, escape
from miro import app
from miro import views
from miro import sorts
from miro import indexes
from miro import filters
from miro.platform import resources
from miro import gtcache
_ = gtcache.gettext
def fillTemplate(domHandler, dtvPlatform, eventCookie, bodyTagExtra, *args, **kargs):
    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle = Handle(domHandler, localvars, onUnlink = lambda:None)



    out = StringIO()
    out.write(u"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n")
    out.write(u'<html dtvPlatform="')
    out.write(quoteattr(urlencode(dtvPlatform)))
    out.write(u'" eventCookie="')
    out.write(quoteattr(urlencode(eventCookie)))
    out.write(u'" xmlns:t="http://www.participatorypolitics.org/" xmlns="http://www.w3.org/1999/xhtml" xmlns:i18n="http://www.participatoryculture.org/i18n">\n<head>\n    <meta content="text/html; charset=utf-8" http-equiv="content-type"></meta>        \n</head>\n<body')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n    <div class="main-video-details">\n        <div class="main-video-details-top">\n            <div class="details-link">\n                ')
    if not (this.showMoreInfo):
        out.write(u'<div>\n                    <a href="#" onclick="return eventURL(\'action:toggleMoreItemInfo?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');"><span>')
        out.write(_(u'Details'))
        out.write(u'</span> <img src="')
        out.write(quoteattr(resources.url(u'images/more-info-button.png')))
        out.write(u'" alt=""></img></a>\n                </div>')
    out.write(u'\n\n                ')
    if not (not (this.showMoreInfo)):
        out.write(u'<div>\n                    <a href="#" onclick="return eventURL(\'action:toggleMoreItemInfo?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');"><span>')
        out.write(_(u'Close'))
        out.write(u'</span> <img src="')
        out.write(quoteattr(resources.url(u'images/more-info-button-close.png')))
        out.write(u'" alt=""></img></a>\n                </div>')
    out.write(u'\n            </div>\n            <div class="video-stats">\n                <div class="length">\n                    <span>')
    out.write(escape(this.getDuration()))
    out.write(u'</span>\n                </div>\n                <div class="date">\n                    ')
    if not (not (this.getReleaseDate() != '')):
        out.write(u'<span><span>')
        out.write(escape(this.getReleaseDate()))
        out.write(u'</span></span>')
    out.write(u'\n                </div>\n\n                <div class="size">\n                    ')
    if not (not ((this.getURL() != this.getLink() and this.getLink() != '') or this.isDownloaded())):
        out.write(u'<span><span>')
        out.write(escape(this.getSizeForDisplay()))
        out.write(u'</span></span>')
    out.write(u'\n                </div>\n                <div class="torrent">\n                    ')
    if not (not (this.looksLikeTorrent())):
        out.write(u'<span>\n                        <span>')
        out.write(_(u'.torrent'))
        out.write(u'</span>\n                    </span>')
    out.write(u'\n                </div>\n           </div>\n        </div>\n\n        <div class="main-video-details-main">\n            <div class="details-buttons-right">\n                <div class="save-button-container">\n                    ')
    if not (not (this.showSaveButton())):
        out.write(u'<div>\n                        <a href="#" class="round-button-left save" onclick="return eventURL(\'action:keepItem?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');">\n                        <div class="round-button-right">\n                        <div class="round-button-content">\n                            <span>')
        out.write(_(u'KEEP'))
        out.write(u'</span>\n                        </div>\n                        </div>\n                        </a>\n                    </div>')
    out.write(u'\n                    ')
    if not (not (this.showSaved())):
        out.write(u'<div class="saved-note">SAVED</div>')
    out.write(u'\n                </div>\n                ')
    if not (not (this.showTrashButton())):
        out.write(u'<div>\n                    <a href="#" class="round-button-left delete" onclick="return eventURL(\'action:expireItem?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');">\n                    <div class="round-button-right">\n                    <div class="round-button-content">\n                        <span>')
        out.write(_(u'DELETE'))
        out.write(u'</span>\n                    </div>\n                    </div>\n                    </a>\n                </div>')
    out.write(u'\n            </div>\n\n            \n            ')
    if not (not (this.hasSharableURL())):
        out.write(u'<div class="select-box-left share-box" onclick="showSelectBoxMenu(\'share-menu-')
        out.write(quoteattr(urlencode(viewName)))
        out.write(u'-')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\'); event.stopPropagation();">\n                <div class="select-box-right">\n                    <div class="select-box-mid">\n                        SHARE\n                    </div>\n                </div>\n            </div>')
    out.write(u'\n            <br class="clear"></br>\n            <ul id="share-menu-')
    out.write(quoteattr(urlencode(viewName)))
    out.write(u'-')
    out.write(quoteattr(urlencode(this.getID())))
    out.write(u'" class="select-box-menu share-menu">\n                <li>\n                    <a href="#" class="main-video-details-task-mail" onclick="return recommendItem(\'')
    out.write(quoteattr(urlencode(this.getTitle())))
    out.write(u"', '")
    out.write(quoteattr(urlencode(this.getURL())))
    out.write(u"', '")
    out.write(quoteattr(urlencode(this.getFeed().getURL())))
    out.write(u'\');">\n                        <img src="')
    out.write(quoteattr(resources.url(u'images/email-a-friend.gif')))
    out.write(u'" alt="email-a-friend icon"></img>\n                        <span>')
    out.write(_(u'Email to a friend'))
    out.write(u'</span>\n                    </a>\n                </li>\n                <li>\n                    <a href="#" class="main-video-details-task-bomb" onclick="return eventURL(\'action:videoBombExternally?item=')
    out.write(quoteattr(urlencode(this.getID())))
    out.write(u'\');">\n                        <img src="')
    out.write(quoteattr(resources.url(u'images/videobomb.gif')))
    out.write(u'" alt="videobomb icon"></img>\n                        <span>')
    out.write(_(u'Post to Video Bomb'))
    out.write(u'</span>\n                    </a>\n                </li>\n                <li>\n                    <a href="#" class="main-video-details-delicious" onclick="return eventURL(\'http://del.icio.us/post?v=4&noui&jump=close&url=')
    out.write(quoteattr(urlencode(this.getURL())))
    out.write(u'&title=')
    out.write(quoteattr(urlencode(this.getTitle())))
    out.write(u'\');">\n                        <img src="')
    out.write(quoteattr(resources.url(u'images/delicious.gif')))
    out.write(u'" alt="delicious icon"></img>\n                        <span>')
    out.write(_(u'Post to del.icio.us'))
    out.write(u'</span>\n                    </a>\n                </li>\n                <li>\n                    <a href="#" class="main-video-details-digg" onclick="return eventURL(\'http://www.digg.com/submit?phrase=2&url=')
    out.write(quoteattr(urlencode(this.getQuotedURL())))
    out.write(u'\');">\n                        <img src="')
    out.write(quoteattr(resources.url(u'images/digg.gif')))
    out.write(u'" alt="digg icon"></img>\n                        <span>')
    out.write(_(u'Post to digg'))
    out.write(u'</span>\n                    </a>\n                </li>\n                <li>\n                    <a href="#" class="main-video-details-reddit" onclick="return eventURL(\'http://reddit.com/submit?url=')
    out.write(quoteattr(urlencode(this.getQuotedURL())))
    out.write(u'&title=')
    out.write(quoteattr(urlencode(this.getQuotedTitle())))
    out.write(u'\');">\n                        <img src="')
    out.write(quoteattr(resources.url(u'images/reddit.gif')))
    out.write(u'" alt="reddit icon"></img>\n                        <span>')
    out.write(_(u'Post to Reddit'))
    out.write(u'</span>\n                    </a>\n                </li>\n            </ul>\n            <!-- HOT SPOT download-progress-')
    out.write(quoteattr(viewName))
    out.write(u'-')
    out.write(quoteattr(this.getID()))
    out.write(u' --><div id="download-progress-')
    out.write(quoteattr(viewName))
    out.write(u'-')
    out.write(quoteattr(this.getID()))
    out.write(u'">\n                ')
    if not (not (this.getState() in ('downloading','paused'))):
        out.write(u'<div class="main-video-details-download-info">\n                    ')
        if not (not (this.gotContentLength())):
            out.write(u'<div>\n                        <div class="main-progress-bar-bg">\n                            <div style="width: ')
            out.write(quoteattr(this.downloadProgressWidth()))
            out.write(u'px;" class="main-progress-bar"></div>\n                        </div>\n                    </div>')
        out.write(u'\n                    ')
        if not (this.gotContentLength()):
            out.write(u'<div>\n                        <div class="progress-throbber-bg">\n                            ')
            if not (not (this.downloadRate() != '0KB/s')):
                out.write(u'<span>\n                                <img src="')
                out.write(quoteattr(resources.url(u'images/progress-throbber.gif')))
                out.write(u'"></img>\n                            </span>')
            out.write(u'\n                            ')
            if not (not (this.downloadRate() == '0KB/s')):
                out.write(u'<span>\n                                <img src="')
                out.write(quoteattr(resources.url(u'images/progress-throbber-gray.png')))
                out.write(u'"></img>\n                            </span>')
            out.write(u'\n                        </div>\n                    </div>')
        out.write(u'\n                    ')
        if not (not (this.getState() == 'downloading')):
            out.write(u'<div class="downloading">\n                        ')
            if not (not (this.downloadInProgress())):
                out.write(u'<div class="download-rate-and-eta">\n                            <span class="download-rate">')
                out.write(escape(this.downloadRate()))
                out.write(u'</span>\n                            <span>')
                out.write(escape(this.downloadETA()))
                out.write(u'</span>\n                        </div>')
            out.write(u'\n                        ')
            if not (this.downloadInProgress()):
                out.write(u'<div>\n                            <span>')
                out.write(escape(this.getStartupActivity()))
                out.write(u'</span>\n                        </div>')
            out.write(u'\n                    </div>')
        out.write(u'\n                    ')
        if not (not (this.getState() == 'paused')):
            out.write(u'<div class="paused">\n                        <span>')
            out.write(escape(this.getPausedString()))
            out.write(u'</span>\n                    </div>')
        out.write(u'\n                    ')
        if not (this.getState() == 'paused'):
            out.write(u'<a title="Pause Download" href="#" class="main-progress-pause" onclick="return eventURL(\'action:pauseDownload?item=')
            out.write(quoteattr(urlencode(this.getID())))
            out.write(u'\');"></a>')
        out.write(u'\n                    ')
        if not (not (this.getState() == 'paused')):
            out.write(u'<a href="#" class="main-progress-resume" onclick="return eventURL(\'action:resumeDownload?item=')
            out.write(quoteattr(urlencode(this.getID())))
            out.write(u'\');" title="Pause Download"></a>')
        out.write(u'\n                    <a href="#" class="main-progress-cancel" onclick="return eventURL(\'action:expireItem?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');" title="Cancel Download"></a>\n                </div>')
    out.write(u'\n            </div><!-- HOT SPOT END -->\n            <div class="download-status-strings">\n                ')
    if not (not (this.getExpiring())):
        out.write(u'<div class="main-video-details-expiring">\n                    <span>')
        out.write(escape(this.getExpirationString()))
        out.write(u'</span>\n                </div>')
    out.write(u'\n                ')
    if not (not (this.isPendingAutoDownload())):
        out.write(u'<div class="main-video-details-pending-auto">\n                    <span>')
        out.write(_(u'Pending Auto Download'))
        out.write(u'</span>\n                </div>')
    out.write(u'\n                ')
    if not (not (this.isFailedDownload() and not this.isPendingManualDownload())):
        out.write(u'<div class="main-video-details-failed-download">\n                    <span>')
        out.write(escape(this.getFailureReason()))
        out.write(u'</span>\n                </div>')
    out.write(u'\n            </div>\n            ')
    if not (this.getEmblemCSSString() == ''):
        out.write(u'<div class="video-state ')
        out.write(quoteattr(this.getEmblemCSSClass()))
        out.write(u'">\n                <div class="video-state-left">\n                    <div class="video-state-right">\n                        <span class="video-state-mid">\n                            <span>')
        out.write(escape(this.getEmblemCSSString()))
        out.write(u'</span>\n                        </span>\n                    </div>\n                </div>\n            </div>')
    out.write(u'\n            ')
    if not (not (this.downloader and this.downloader.getState() == 'uploading')):
        out.write(u'<div>\n                 <a href="#" class="round-button-left stop-seeding" onclick="return eventURL(\'action:stopUploadItem?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');">\n                <div class="round-button-right">\n                <div class="round-button-content">\n                    <span>')
        out.write(_(u'STOP SEEDING'))
        out.write(u'</span>\n                </div>\n                </div>\n                </a>\n            </div>')
    out.write(u'\n        </div>\n        ')
    if not (not (this.showMoreInfo)):
        out.write(u'<div class="more-info-details">\n            <div>')
        out.write(this.getMoreInfo())
        out.write(u'</div>\n        </div>')
    out.write(u'\n    </div>\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
