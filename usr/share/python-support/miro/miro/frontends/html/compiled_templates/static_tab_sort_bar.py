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
    
    itemSort = kargs['itemSort']
    section = kargs['section']
        
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle = Handle(domHandler, localvars, onUnlink = lambda:None)

    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_0 = Handle(domHandler, localvars, onUnlink = lambda:None)

    handle.addSubHandle(handle_0)


    out = StringIO()
    out.write(u"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n")
    out.write(u'<html dtvPlatform="')
    out.write(quoteattr(urlencode(dtvPlatform)))
    out.write(u'" eventCookie="')
    out.write(quoteattr(urlencode(eventCookie)))
    out.write(u'" xmlns:t="http://www.participatorypolitics.org/" xmlns="http://www.w3.org/1999/xhtml" xmlns:i18n="http://www.participatoryculture.org/i18n">\n<head>\n    <meta content="text/html; charset=utf-8" http-equiv="content-type"></meta>\n    \n</head>\n<body')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n<div class="static-tab-sort">\n    ')
    out.write(u'\n<div class="sort-bar">\n    <div class="sort-buttons">\n        <div class="sort-buttons-right">\n            <a href="#" class="length sort-button ')
    out.write(quoteattr(itemSort.getSortButtonState('duration')))
    out.write(u'" onclick="return eventURL(\'action:sortBy?by=duration&section=')
    out.write(quoteattr(section))
    out.write(u'\');">\n                Length<img src="')
    out.write(quoteattr(resources.url(u'images/sort-up.png')))
    out.write(u'" class="up-arrow"></img><img src="')
    out.write(quoteattr(resources.url(u'images/sort-down.png')))
    out.write(u'" class="down-arrow"></img>\n            </a>\n            <a href="#" class="date sort-button ')
    out.write(quoteattr(itemSort.getSortButtonState('date')))
    out.write(u'" onclick="return eventURL(\'action:sortBy?by=date&section=')
    out.write(quoteattr(section))
    out.write(u'\');">\n                Date<img src="')
    out.write(quoteattr(resources.url(u'images/sort-up.png')))
    out.write(u'" class="up-arrow"></img><img src="')
    out.write(quoteattr(resources.url(u'images/sort-down.png')))
    out.write(u'" class="down-arrow"></img>\n            </a>\n\n            <a href="#" class="size sort-button ')
    out.write(quoteattr(itemSort.getSortButtonState('size')))
    out.write(u'" onclick="return eventURL(\'action:sortBy?by=size&section=')
    out.write(quoteattr(section))
    out.write(u'\');">\n                Size<img src="')
    out.write(quoteattr(resources.url(u'images/sort-up.png')))
    out.write(u'" class="up-arrow"></img><img src="')
    out.write(quoteattr(resources.url(u'images/sort-down.png')))
    out.write(u'" class="down-arrow"></img>\n            </a>\n            <div class="clear"></div>\n        </div>\n\n        <a href="#" class="name sort-button ')
    out.write(quoteattr(itemSort.getSortButtonState('name')))
    out.write(u'" onclick="return eventURL(\'action:sortBy?by=name&section=')
    out.write(quoteattr(section))
    out.write(u'\');">\n            Name<img src="')
    out.write(quoteattr(resources.url(u'images/sort-up.png')))
    out.write(u'" class="up-arrow"></img><img src="')
    out.write(quoteattr(resources.url(u'images/sort-down.png')))
    out.write(u'" class="down-arrow"></img>\n        </a>\n    </div>\n</div>\n')
    out.write(u' \n</div>\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
