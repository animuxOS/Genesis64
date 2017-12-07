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
    out.write(u'>\n    <div class="main-video-desc noselect">\n        <h1 class="noselect">')
    out.write(escape(this.getTitle()))
    out.write(u'</h1>\n        <div class="main-video-desc-desc noselect">\n            <span>')
    out.write(this.getDescription())
    out.write(u'</span>\n        </div>\n        <div class="main-video-bottom">\n                <div class="channel-title">\n                        <span>')
    out.write(escape(this.getChannelTitle()))
    out.write(u'</span>\n                </div>\n                <div class="donate-html noselect">\n                    <span>')
    out.write(this.getPaymentHTML())
    out.write(u'</span>\n                </div>\n        </div>\n    </div>\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
