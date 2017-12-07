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
    out.write(u'>\n\n<div dragdestdata="channelfolder-')
    out.write(quoteattr(this.objID()))
    out.write(u'" dragdesttype="channelfolder" class="tab-drop-target" drageffectchannelfolder="move">\n<div class="dnd-reorder-indicator circle"></div>\n<div class="dnd-reorder-indicator line"></div>\n<div dragdestdata="channelfolder-')
    out.write(quoteattr(this.objID()))
    out.write(u'" dragdesttype="channel" drageffectchannel="move" class="tab-container-drop-target">\n<div class="dnd-container-drop-indicator left"></div>\n<div class="dnd-container-drop-indicator mid"></div>\n<div class="dnd-container-drop-indicator right"></div>\n<a dragsourcetype="channelfolder" dragicon="channel-tnail-')
    out.write(quoteattr(this.objID()))
    out.write(u'" class="feeditem noselect draggable folder" dragsourcedata="tablist-')
    out.write(quoteattr(this.objID()))
    out.write(u'">\n')
    if not (this.obj.getExpanded()):
        out.write(u'<img src="')
        out.write(quoteattr(resources.url(u'images/tab-arrow-up.png')))
        out.write(u'" alt="expanded" onmousedown="return eventURL(\'action:toggleExpand?id=\' + ')
        out.write(quoteattr(this.objID()))
        out.write(u');" class="expanded-triangle"></img>')
    out.write(u'\n')
    if not (not (this.obj.getExpanded())):
        out.write(u'<img src="')
        out.write(quoteattr(resources.url(u'images/tab-arrow-down.png')))
        out.write(u'" alt="unexpanded" class="expanded-triangle" onmousedown="return eventURL(\'action:toggleExpand?id=\' + ')
        out.write(quoteattr(this.objID()))
        out.write(u');"></img>')
    out.write(u'\n')
    if not (not (this.obj.showA())):
        out.write(u'<div class="left-bubble blue ')
        out.write(quoteattr(this.obj.showU() and 'second' or ''))
        out.write(u'">\n <div class="right-bubble blue">\n  <div class="number-count blue">')
        out.write(escape(this.obj.numAvailable()))
        out.write(u'</div>\n </div>\n</div>')
    out.write(u'\n')
    if not (not (this.obj.showU())):
        out.write(u'<div class="left-bubble green">\n <div class="right-bubble green">\n  <div class="number-count green">')
        out.write(escape(this.obj.numUnwatched()))
        out.write(u'</div>\n </div>\n <div href="#" class="new-video-play-button" onclick="return playNewVideos(event, ')
        out.write(quoteattr(this.objID()))
        out.write(u');">\n     <img src="')
        out.write(quoteattr(resources.url(u'images/play.png')))
        out.write(u'"></img>\n </div>\n</div>')
    out.write(u'\n<div class="line">\n<img src="')
    out.write(quoteattr(resources.url(u'images/folder-icon-tablist.png')))
    out.write(u'" id="channel-tnail-')
    out.write(quoteattr(this.objID()))
    out.write(u'" class="icon"></img><div class="name">')
    out.write(escape(this.obj.getTitle()))
    out.write(u'</div>\n</div>\n</a>\n</div>\n</div>\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
