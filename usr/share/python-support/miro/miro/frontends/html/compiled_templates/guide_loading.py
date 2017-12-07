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
    
    guide = views.guides.getObjectByID(int(kargs['id']))
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
    out.write(u'" xmlns:t="http://www.participatorypolitics.org/" xmlns="http://www.w3.org/1999/xhtml" xmlns:i18n="http://www.participatoryculture.org/i18n">\n<head>\n    \n<meta content="text/html; charset=utf-8" http-equiv="content-type"></meta>\n<meta content="')
    out.write(quoteattr(guide.getLastVisitedURL()))
    out.write(u'" name="guideURL"></meta>\n<link href="')
    out.write(quoteattr(resources.url(u'css/style.css')))
    out.write(u'" type="text/css" rel="stylesheet"></link>\n<script type="text/javascript">\n    function navBarLoaded() \n    {\n        var metas = document.getElementsByTagName(\'meta\');\n        var i;\n        for (i=0; i < metas.length; i++)\n        {\n            if (metas[i].getAttribute(\'name\') == "guideURL")\n            {\n                miro_guide_frame.location = metas[i].getAttribute(\'content\');\n                break;\n            }\n        }\n    }\n\n    function guideLoaded() \n    {\n        try\n        {\n            netscape.security.PrivilegeManager.enablePrivilege(\'UniversalBrowserRead\');\n            netscape.security.PrivilegeManager.enablePrivilege(\'UniversalBrowserWrite\');\n        }\n        catch (e) {}\n        \n        var loadIndicator = miro_navigation_frame.document.getElementById(\'load-indicator\');\n        if (loadIndicator !== null)\n        {\n            loadIndicator.style.display = \'none\';\n        }\n    }\n\n    function guideUnloaded() \n    {\n        try\n        {\n            netscape.security.PrivilegeManager.enablePrivilege(\'UniversalBrowserRead\');\n            netscape.security.PrivilegeManager.enablePrivilege(\'UniversalBrowserWrite\');\n        }\n        catch (e) {}\n        \n        miro_navigation_frame.document.getElementById(\'load-indicator\').style.display = \'block\';\n    }\n</script>\n\n\n</head>\n<frameset rows="26, *" border="0" framespacing="0" frameborder="0">\n    <frame onload="navBarLoaded()" name="miro_navigation_frame" src="')
    out.write(quoteattr(resources.url(u'html/guide-navigation.html')))
    out.write(u'" noresize="noresize" marginheight="0" scrolling="no" frameborder="0" marginwidth="0"></frame>\n    <frame onload="guideLoaded()" marginheight="0" name="miro_guide_frame" frameborder="0" marginwidth="0"></frame>\n</frameset>\n</html>')
    out.seek(0)


    return (out, handle)
