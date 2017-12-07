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
    out.write(u'>\n    <img src="')
    out.write(quoteattr(this.getThumbnail()))
    out.write(u'" alt="" class="main-video-tnail" id="video-tnail-')
    out.write(quoteattr(viewName + str(this.getID())))
    out.write(u'"></img>\n\n    <div class="main-video-hitbox">\n        ')
    if not (not (this.isDownloadable())):
        out.write(u'<a href="#" class="icon download" onclick="return eventURL(\'action:startDownload?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');" title="Download \'')
        out.write(quoteattr(this.getTitle()))
        out.write(u'\'"></a>')
    out.write(u'\n        ')
    if not (not (this.getState() == 'paused')):
        out.write(u'<a href="#" class="icon paused-circle" onclick="return eventURL(\'action:startDownload?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');" title="Download \'')
        out.write(quoteattr(this.getTitle()))
        out.write(u'\'"></a>')
    out.write(u'\n        ')
    if not (not (this.getState() == 'downloading')):
        out.write(u'<span class="icon inprogress-background">\n            ')
        if not (this.isPendingManualDownload()):
            out.write(u'<img src="')
            out.write(quoteattr(resources.url(u'images/main-video-inprogress-arrows.gif')))
            out.write(u'" title="Downloading \'')
            out.write(quoteattr(this.getTitle()))
            out.write(u'\'" class="inprogress-arrows"></img>')
        out.write(u'\n            ')
        if not (not (this.isPendingManualDownload())):
            out.write(u'<img src="')
            out.write(quoteattr(resources.url(u'images/download-pending-dot.png')))
            out.write(u'" class="download-pending-icon" title="Download Pending for \'')
            out.write(quoteattr(this.getTitle()))
            out.write(u'\'"></img>')
        out.write(u'\n        </span>')
    out.write(u'\n        ')
    if not (not (this.isPlayable())):
        out.write(u'<a href="#" class="icon play" onclick="return eventURL(\'action:playViewNamed?viewName=')
        out.write(quoteattr(urlencode(viewName)))
        out.write(u'&firstItemId=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');" title="Play \'')
        out.write(quoteattr(this.getTitle()))
        out.write(u'\'"></a>')
    out.write(u'\n    </div>\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
