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
    
    this = app.controller.videoInfoItem
    thisItemView = views.items.filter(lambda x: x.getID() == this.getID())
    app.controller.videoInfoItem = None
    import os.path
    from miro.platform.utils import filenameToUnicode
    filename = filenameToUnicode(os.path.basename(this.getFilename()))

    def _execOnUnload():
        
        thisItemView.unlink()
        import os.path
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle = Handle(domHandler, localvars, onUnlink = _execOnUnload)

    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_0 = Handle(domHandler, localvars, onUnlink = lambda:None)

    def up_0_handle_0(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n<div id="videodetails-actions">\n     ')
        if not (not (this.hasSharableURL())):
            out.write(u'<div>\n        <a href="#" onclick="return recommendItem(\'')
            out.write(quoteattr(urlencode(this.getTitle())))
            out.write(u"', '")
            out.write(quoteattr(urlencode(this.getURL())))
            out.write(u"', '")
            out.write(quoteattr(urlencode(this.getFeed().getURL())))
            out.write(u'\');"><span>')
            out.write(_(u'EMAIL A FRIEND'))
            out.write(u'</span></a>\n     </div>')
        out.write(u'\n     ')
        if not (not (this.getLink())):
            out.write(u'<div>\n        <a href="')
            out.write(quoteattr(this.getLink()))
            out.write(u'"><span>')
            out.write(_(u'PERMALINK'))
            out.write(u'</span></a>\n     </div>')
        out.write(u'\n     <div>\n        ')
        if not (not (this.getExpiring())):
            out.write(u'<span><span class="expiration">')
            out.write(escape(this.getExpirationString()))
            out.write(u'</span></span>')
        out.write(u'\n        ')
        if not (not (this.showSaveButton())):
            out.write(u'<span>\n\t  <a href="#" onclick="return eventURL(\'action:keepItem?item=')
            out.write(quoteattr(urlencode(this.getID())))
            out.write(u'\');"><span>')
            out.write(_(u'KEEP'))
            out.write(u'</span></a> \n\t</span>')
        out.write(u'\n        ')
        if not (not (this.getFeedURL() == u'dtv:singleFeed')):
            out.write(u'<span>\n\t  <a href="#" onclick="return eventURL(\'action:addItemToLibrary?item=')
            out.write(quoteattr(urlencode(this.getID())))
            out.write(u'\');"><span>')
            out.write(_(u'ADD TO LIBRARY'))
            out.write(u'</span></a> \n\t</span>')
        out.write(u'\n        ')
        if not (this.getFeedURL() == u'dtv:singleFeed'):
            out.write(u'<span>\n        ')
            if not (not (this.showSaveButton())):
                out.write(u'<span> - </span>')
            out.write(u'\n\t  <a href="#" onclick="return eventURL(\'action:expirePlayingItem?item=')
            out.write(quoteattr(urlencode(this.getID())))
            out.write(u'\');"><span>')
            out.write(_(u'DELETE'))
            out.write(u'</span></a>\n        </span>')
        out.write(u'\n      </div>\n</div>\n</div>')
        out.seek(0)
        return out
    handle_0.addUpdate('tmplcomp99408884','nextSibling',thisItemView,up_0_handle_0, u'thisItemView')
    handle.addSubHandle(handle_0)


    out = StringIO()
    out.write(u"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n")
    out.write(u'<html dtvPlatform="')
    out.write(quoteattr(urlencode(dtvPlatform)))
    out.write(u'" eventCookie="')
    out.write(quoteattr(urlencode(eventCookie)))
    out.write(u'" xmlns="http://www.w3.org/1999/xhtml">\n\n<head>\n    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"></meta>\n    <title>Miro - External Playback Template</title>\n\n    <link href="')
    out.write(quoteattr(resources.url(u'css/external.css')))
    out.write(u'" type="text/css" rel="stylesheet"></link>\n    <link href="')
    out.write(quoteattr(resources.url(u'css/video-info.css')))
    out.write(u'" type="text/css" rel="stylesheet"></link>\n\n    <script type="text/javascript">\n<!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n///////////////////////////////////////////////////////////////////////////////\n//// For use on your page                                                  ////\n///////////////////////////////////////////////////////////////////////////////\n\nfunction getDTVPlatform() {\n    var elt = document.getElementsByTagName("html")[0];\n    return elt.getAttribute(\'dtvPlatform\');\n}\n\nfunction loadURL(url) {\n    try {\n        document.location.href = url;\n    } catch (e) {\n        // This may happen if the backend decides to handle the url load\n        // itself.\n    }\n}\n\n// For calling from page Javascript: Cause a URL to be loaded. The\n// assumption is that the application will notice, abort the load, and\n// take some action based on the URL.\nfunction eventURL(url) {\n    if (typeof(window.frontend) == \'undefined\') {\n\t// Generic strategy: trigger a load, and hope the application\n\t// catches it and cancels it without creating a race\n\t// condition.\n        loadURL(url)\n    } else {\n\t// OS X WebKit (KHTML) strategy: pass in an Objective C object\n\t// through the window object and call a method on it.\n\twindow.frontend.eventURL(url);\n    }\n\n    return false;\n}\n\n// Calls eventURL, then calls event.stopPropagation() and\n// event.preventDefault() so that the event chain is stopped.\nfunction eventURLAndStop(url, event) {\n  eventURL(url);\n  event.stopPropagation();\n  event.preventDefault();\n}\n\nfunction recommendItem(title, url) {\n    loadURL(\'http://www.videobomb.com/index/democracyemail?url=\' + \n            url + \'&title=\' + title);\n    return false;\n}\n\nfunction recommendChannel(title, url) {\n    // See also app.py if changing this URL\n    loadURL(\'http://www.videobomb.com/democracy_channel/email_friend\' +\n        \'?url=\' + url + \'&title=\' + title);\n    return false;\n}\n\n// Start the video player. The playlist will be the items in the view\n// named by viewName. If firstItemId is the id of an item in the view,\n// playback will start on that item; otherwise playback will start on\n// the first item.\nfunction playViewNamed(viewName, firstItemId) {\n    url = \'action:playViewNamed?\';\n    url = url + \'viewName=\' + URLencode(viewName);\n    url = url + \'&firstItemId=\' + URLencode(firstItemId);\n    eventURL(url);\n    return false;\n}\n\n// You can make \'incremental search\' text boxes on your page that\n// effectively tie the text box to the \'parameter\' argument of setViewFilter,\n// with the other argumens fixed. To do this, add these two attributes to\n// the text box:\n//   onfocus="startEditSearch(this)"\n//   onblur="endEditFilter()"\n// replacing the arguments in parentheses with the desired strings.\n//\n// You\'ll also need to provide a updateSearchString function at the\n// top of your template to perform the actual update\n\nvar editSearchField = null;\nvar editSearchOldValue = \'\';\nvar editSearchTimer = null;\nvar editSearchCallback = null;\n\nfunction onSearchFocus(obj){\n  if (obj.getAttribute(\'searching\') != \'1\') {\n\tobj.value="";\n\tobj.searching = \'1\';\n  }\n  startEditSearch(obj, null);\n}\n\nfunction startEditSearch(obj, callback) {\n  editSearchOldValue = obj.value;\n\n  editSearchField = obj;\n  editSearchCallback = callback;\n  editSearchTimerTick();\n}\n\nfunction editSearchUpdate() {\n    value = editSearchField.value;\n    if (editSearchOldValue != value) {\n\turl = \'action:setSearchString?searchString=\' + URLencode(value);\n\teventURL(url);\n\teditSearchOldValue = value;\n\tif(editSearchCallback) editSearchCallback();\n    }\n}\n\nfunction editSearchTimerTick() {\n    editSearchUpdate();\n    editSearchTimer = setTimeout(editSearchTimerTick, 50);\n}\n\nfunction endEditSearch() {\n  clearTimeout(editSearchTimer);\n  editSearchUpdate();\n}\n\n// Internal use: \'URL encode\' the given string.\nfunction URLencode(str) {\n    return encodeURIComponent(str)\n}\n\nfunction URLdecode(str) {\n  return decodeURIComponent(str)\n}\n\nvar currentSelectBoxMenu = null;\nfunction showSelectBoxMenu(id) {\n    document.getElementById(id).style.display = \'block\';\n    currentSelectBoxMenu = id;\n    document.addEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\nfunction hideSelectBoxMenu(event) {\n    document.getElementById(currentSelectBoxMenu).style.display = \'\';\n    currentSelectBoxMenu = null;\n    document.removeEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\n///////////////////////////////////////////////////////////////////////////////\n//// For calling by host templating code                                   ////\n///////////////////////////////////////////////////////////////////////////////\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it disappear.\nfunction hideItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'none\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it visible if it was previously hidden.\nfunction showItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Replace the item with the\n// given id with the element described by the proided XML.\nfunction changeItem(id, newXML) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.replaceChild(frag, elt);\n}\n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element immediately before the item\n// with the given id, such that the newly inserted item has the same\n// parent.\nfunction addItemBefore(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.insertBefore(frag, elt);\n}    \n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element as the final child of the\n// item with the given id.\nfunction addItemAtEnd(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.insertBefore(frag, null);\n}    \n\n// For calling by host templating code: Remove the item with the given\n// id.\nfunction removeItem(id) {\n    elt = document.getElementById(id);\n    elt.parentNode.removeChild(elt);\n}    \n\n// Internal use: Sometime if all you do is change the style on a node,\n// Safari doesn\'t update the view until your mouse is next over the\n// window. Force the issue by making a drastic change in the vicinity\n// of the given element and then reversing it.\nfunction forceRedisplay(elt) {\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.extractContents();\n    r.insertNode(frag);\n}\n\nfunction handleContextMenuSelect(event) {\n  if(event.button == 2) {\n    var area = event.currentTarget.getAttribute("selectArea");\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var url = \'action:handleContextMenuSelect?id=\' + id + \'&area=\' + area +\n              \'&viewName=\' + viewName;\n    eventURL(url);\n  }\n  return true;\n}\n\nfunction handleSelect(event) {\n   if(event.target.tagName && event.target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n    }\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var area = event.currentTarget.getAttribute("selectArea");\n    var shiftKey = \'0\';\n    var ctrlKey = \'0\';\n    if(event.shiftKey) shiftKey = \'1\';\n    if(event.ctrlKey || event.metaKey) ctrlKey = \'1\';\n    eventURL(\'action:handleSelect?area=\' + area + \'&viewName=\' + viewName + \n\t\'&id=\' + id + \'&shiftDown=\' + shiftKey + \'&ctrlDown=\' + ctrlKey);\n    return true;\n}\n\nfunction handleDblClick(event, viewName, id) {\n   var target = event.target;\n   while (target != undefined && target.ondblclick === null && target.tagName.toUpperCase() != \'A\') {\n       target = target.parentNode;\n   }\n\n   if(target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n   } else {\n       return eventURL(\'action:playViewNamed?viewName=\' + viewName + \n           \'&firstItemId=\' + id);\n   }\n}\n\nfunction getKeyFromEvent(evt) {\n  var key = 0;\n  if (window.event)  {\n    key = evt.keyCode;\n  } else if (evt.which) {\n  \tkey = evt.which;\n  }\n\n  return key;\n}\n\nfunction sendKeyToSearchBox(event) {\n  if(event.altKey || event.ctrlKey || event.metaKey ||\n      (event.target.tagName && event.target.tagName.toUpperCase() == \'INPUT\'))\n      return true;\n  var key = getKeyFromEvent(event);\n  if ((key == 33) || (key == 34) || (key == 35) || (key == 36) || \n      (key == 37) || (key == 38) || (key == 39) || (key == 40))\n      return true;\n  var searchBox = document.getElementById("search-box");\n  searchBox.focus();\n  return true;\n}\n\nfunction playNewVideos(event, id) {\n  eventURL(\'action:playNewVideos?id=\' + id);\n  event.stopPropagation(); // don\'t want handleSelect to deal with this event\n  return false;\n}\n\n///////////////////////////////////////////////////////////////////////////////\n///////////////////////////////////////////////////////////////////////////////\n\n-->\n</script>\n\n    <script type="text/javascript">\n<!-- // Protect from our XML parser, which doesn\'t know to protect <script>\nvar counting = false;\nvar count = 0;\n\nfunction startCountdown(itemID)\n{\n    counting = true;\n    count = 10;\n    updateCountdown(itemID)\n}\n\nfunction stopCountdown()\n{\n    counting = false;\n}\n\nfunction updateCountdown(itemID)\n{\n    if (counting)\n    {\n        count = count - 1;\n        if (count >= 0)\n        {\n            document.getElementById(\'countdown\').innerHTML = count;\n            setTimeout(\'updateCountdown(\' + itemID + \')\', 1000);\n        }\n        else\n        {\n            skipItem(itemID)\n        }\n    }\n}\n\nfunction playItemExternally(itemID)\n{\n    stopCountdown();\n    eventURL(\'action:playItemExternally?itemID=\' + itemID)\n}\n\nfunction skipItem(itemID)\n{\n    stopCountdown();\n    eventURL(\'action:skipItem?itemID=\' + itemID)\n}\n\nfunction revealItem(itemID)\n{\n    stopCountdown();\n    eventURL(\'action:revealItem?item=\' + itemID)\n}\n\n-->\n</script>\n\n\n    \n    \n\n</head>\n\n<body onload="startCountdown(')
    out.write(quoteattr(urlencode(this.getID())))
    out.write(u')"')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n    <div id="external-container-basic">\n    \t<span>')
    tmplcomp29783576 = {}
    tmplcomp61598871 = StringIO()
    tmplcomp61598871.write(u'<span>')
    tmplcomp61598871.write(escape(this.getFormat(emptyForUnknown=False)))
    tmplcomp61598871.write(u'</span>')
    tmplcomp61598871.seek(0)
    tmplcomp29783576['format'] = tmplcomp61598871.read()
    tmplcomp38588428 = StringIO()
    tmplcomp38588428.write(u'<span>')
    tmplcomp38588428.write(escape(filename))
    tmplcomp38588428.write(u'</span>')
    tmplcomp38588428.seek(0)
    tmplcomp29783576['filename'] = tmplcomp38588428.read()
    out.write(Template(_(u"Miro can't play this file. You may be able to open it with a different program.<br></br><br></br><strong>Filename:</strong> ${filename}<br></br><strong>File type:</strong> ${format}")).substitute(tmplcomp29783576))
    out.write(u'</span><br></br><a style="color: white;" href="javascript:revealItem(')
    out.write(quoteattr(urlencode(this.getID())))
    out.write(u');"><span>')
    out.write(_(u'REVEAL FILE'))
    out.write(u'</span></a>\n\n<br style="clear: both;"></br>\n        <a href="javascript:playItemExternally(')
    out.write(quoteattr(urlencode(this.getID())))
    out.write(u')" id="external-button-left">\n            <span>')
    out.write(_(u'Play Externally'))
    out.write(u'</span>\n        </a>\n        \n        <a href="javascript:skipItem(')
    out.write(quoteattr(urlencode(this.getID())))
    out.write(u')" id="external-button-right">\n            <span>')
    tmplcomp77669767 = {}
    tmplcomp58977376 = StringIO()
    tmplcomp58977376.write(u'<b id="countdown"></b>')
    tmplcomp58977376.seek(0)
    tmplcomp77669767['countdown'] = tmplcomp58977376.read()
    out.write(Template(_(u'Skip >> ${countdown}')).substitute(tmplcomp77669767))
    out.write(u'</span>\n        </a>\n    </div>\n    \n    <div id="embedded-video-info">\n        <div id="video_info_area">')
    out.write(u'\n<div id="videodetails-container">\n')
    out.write(u'<span id="tmplcomp99408884"/>\n\t<div id="videodetails-channeltitle">\n        <h1>')
    out.write(escape(this.getTitle()))
    out.write(u'</h1> \n        <h2>')
    out.write(escape(this.getFeed().getTitle()))
    out.write(u'</h2>\n        <h3>')
    out.write(this.getPaymentHTML())
    out.write(u'</h3>\n\t</div>\n\t<div id="videodetails-ad">\n\t    <span>')
    out.write(this.getAd())
    out.write(u'</span>\n\t</div>\n</div>\n')
    out.write(u'</div>\n    </div>\n</body>\n\n</html>')
    out.seek(0)


    return (out, handle)
