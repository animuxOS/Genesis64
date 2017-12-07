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
    out.write(u'>\n\n<div dragdestdata="playlist-')
    out.write(quoteattr(this.objID()))
    out.write(u'" drageffectplaylist="move" dragdesttype="')
    out.write(quoteattr(this.obj.getDragDestType()))
    out.write(u'" drageffectplaylistfolder="move" class="tab-drop-target ')
    out.write(quoteattr(this.obj.getFolder() and 'child' or ''))
    out.write(u'">\n<div class="dnd-reorder-indicator circle"></div>\n<div class="dnd-reorder-indicator line"></div>\n<div dragdestdata="playlist-')
    out.write(quoteattr(this.objID()))
    out.write(u'" dragdesttype="downloadeditem" drageffectdownloadeditem="copy" class="tab-container-drop-target">\n<div class="dnd-container-drop-indicator left"></div>\n<div class="dnd-container-drop-indicator mid"></div>\n<div class="dnd-container-drop-indicator right"></div>\n<a dragsourcetype="')
    out.write(quoteattr(this.getDragSourceType()))
    out.write(u'" dragicon="playlist-tnail-')
    out.write(quoteattr(this.objID()))
    out.write(u'" class="feeditem draggable noselect" dragsourcedata="tablist-')
    out.write(quoteattr(this.objID()))
    out.write(u'">\n<div class="line">\n<img src="')
    out.write(quoteattr(resources.url(u'images/playlist-icon-tablist.png')))
    out.write(u'" id="playlist-tnail-')
    out.write(quoteattr(this.objID()))
    out.write(u'" class="icon"></img><div class="name">')
    out.write(escape(this.obj.getTitle()))
    out.write(u'</div>\n</div>\n</a>\n</div>\n</div>\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
