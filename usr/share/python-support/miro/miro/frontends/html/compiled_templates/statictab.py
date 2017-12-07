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
    out.write(u'<html xmlns:t="http://www.participatorypolitics.org/" xmlns:i18n="http://www.participatoryculture.org/i18n">\n<head>\n</head>\n<body')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n<a class="feeditem noselect">\n    <img src="')
    out.write(quoteattr(this.obj.getIconURL()))
    out.write(u'" alt="" class="icon"></img>\n    ')
    if not (this.obj.getNumber() == 0):
        out.write(u'<div class="left-bubble ')
        out.write(quoteattr(urlencode(this.obj.getNumberColor())))
        out.write(u'">\n        <div class="right-bubble ')
        out.write(quoteattr(urlencode(this.obj.getNumberColor())))
        out.write(u'">\n            <div class="number-count ')
        out.write(quoteattr(urlencode(this.obj.getNumberColor())))
        out.write(u'">')
        out.write(escape(this.obj.getNumber()))
        out.write(u'</div>\n        </div>\n        ')
        if not (not (this.obj.enableNewVideoPlayButton())):
            out.write(u'<div href="#" class="new-video-play-button" onclick="return playNewVideos(event, ')
            out.write(quoteattr(this.objID()))
            out.write(u');">\n            <img src="')
            out.write(quoteattr(resources.url(u'images/play.png')))
            out.write(u'"></img>\n        </div>')
        out.write(u'\n    </div>')
    out.write(u'\n    <div class="line">\n    <div class="name">')
    out.write(escape(this.obj.getTitle()))
    out.write(u'</div>\n    </div>\n</a>\n\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
