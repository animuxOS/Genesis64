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
    
    feed = views.feeds.getObjectByID(int(kargs['id']))
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
    out.write(u'" xmlns:t="http://www.participatorypolitics.org/" xmlns="http://www.w3.org/1999/xhtml" xmlns:i18n="http://www.participatoryculture.org/i18n">\n<head>\n<meta content="text/html; charset=utf-8" http-equiv="content-type"></meta>\n\n<link href="')
    out.write(quoteattr(resources.url(u'css/main.css')))
    out.write(u'" type="text/css" rel="stylesheet"></link>\n<script type="text/javascript">\n<!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n///////////////////////////////////////////////////////////////////////////////\n//// For use on your page                                                  ////\n///////////////////////////////////////////////////////////////////////////////\n\nfunction getDTVPlatform() {\n    var elt = document.getElementsByTagName("html")[0];\n    return elt.getAttribute(\'dtvPlatform\');\n}\n\nfunction loadURL(url) {\n    try {\n        document.location.href = url;\n    } catch (e) {\n        // This may happen if the backend decides to handle the url load\n        // itself.\n    }\n}\n\n// For calling from page Javascript: Cause a URL to be loaded. The\n// assumption is that the application will notice, abort the load, and\n// take some action based on the URL.\nfunction eventURL(url) {\n    if (typeof(window.frontend) == \'undefined\') {\n\t// Generic strategy: trigger a load, and hope the application\n\t// catches it and cancels it without creating a race\n\t// condition.\n        loadURL(url)\n    } else {\n\t// OS X WebKit (KHTML) strategy: pass in an Objective C object\n\t// through the window object and call a method on it.\n\twindow.frontend.eventURL(url);\n    }\n\n    return false;\n}\n\n// Calls eventURL, then calls event.stopPropagation() and\n// event.preventDefault() so that the event chain is stopped.\nfunction eventURLAndStop(url, event) {\n  eventURL(url);\n  event.stopPropagation();\n  event.preventDefault();\n}\n\nfunction recommendItem(title, url) {\n    loadURL(\'http://www.videobomb.com/index/democracyemail?url=\' + \n            url + \'&title=\' + title);\n    return false;\n}\n\nfunction recommendChannel(title, url) {\n    // See also app.py if changing this URL\n    loadURL(\'http://www.videobomb.com/democracy_channel/email_friend\' +\n        \'?url=\' + url + \'&title=\' + title);\n    return false;\n}\n\n// Start the video player. The playlist will be the items in the view\n// named by viewName. If firstItemId is the id of an item in the view,\n// playback will start on that item; otherwise playback will start on\n// the first item.\nfunction playViewNamed(viewName, firstItemId) {\n    url = \'action:playViewNamed?\';\n    url = url + \'viewName=\' + URLencode(viewName);\n    url = url + \'&firstItemId=\' + URLencode(firstItemId);\n    eventURL(url);\n    return false;\n}\n\n// You can make \'incremental search\' text boxes on your page that\n// effectively tie the text box to the \'parameter\' argument of setViewFilter,\n// with the other argumens fixed. To do this, add these two attributes to\n// the text box:\n//   onfocus="startEditSearch(this)"\n//   onblur="endEditFilter()"\n// replacing the arguments in parentheses with the desired strings.\n//\n// You\'ll also need to provide a updateSearchString function at the\n// top of your template to perform the actual update\n\nvar editSearchField = null;\nvar editSearchOldValue = \'\';\nvar editSearchTimer = null;\nvar editSearchCallback = null;\n\nfunction onSearchFocus(obj){\n  if (obj.getAttribute(\'searching\') != \'1\') {\n\tobj.value="";\n\tobj.searching = \'1\';\n  }\n  startEditSearch(obj, null);\n}\n\nfunction startEditSearch(obj, callback) {\n  editSearchOldValue = obj.value;\n\n  editSearchField = obj;\n  editSearchCallback = callback;\n  editSearchTimerTick();\n}\n\nfunction editSearchUpdate() {\n    value = editSearchField.value;\n    if (editSearchOldValue != value) {\n\turl = \'action:setSearchString?searchString=\' + URLencode(value);\n\teventURL(url);\n\teditSearchOldValue = value;\n\tif(editSearchCallback) editSearchCallback();\n    }\n}\n\nfunction editSearchTimerTick() {\n    editSearchUpdate();\n    editSearchTimer = setTimeout(editSearchTimerTick, 50);\n}\n\nfunction endEditSearch() {\n  clearTimeout(editSearchTimer);\n  editSearchUpdate();\n}\n\n// Internal use: \'URL encode\' the given string.\nfunction URLencode(str) {\n    return encodeURIComponent(str)\n}\n\nfunction URLdecode(str) {\n  return decodeURIComponent(str)\n}\n\nvar currentSelectBoxMenu = null;\nfunction showSelectBoxMenu(id) {\n    document.getElementById(id).style.display = \'block\';\n    currentSelectBoxMenu = id;\n    document.addEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\nfunction hideSelectBoxMenu(event) {\n    document.getElementById(currentSelectBoxMenu).style.display = \'\';\n    currentSelectBoxMenu = null;\n    document.removeEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\n///////////////////////////////////////////////////////////////////////////////\n//// For calling by host templating code                                   ////\n///////////////////////////////////////////////////////////////////////////////\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it disappear.\nfunction hideItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'none\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it visible if it was previously hidden.\nfunction showItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Replace the item with the\n// given id with the element described by the proided XML.\nfunction changeItem(id, newXML) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.replaceChild(frag, elt);\n}\n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element immediately before the item\n// with the given id, such that the newly inserted item has the same\n// parent.\nfunction addItemBefore(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.insertBefore(frag, elt);\n}    \n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element as the final child of the\n// item with the given id.\nfunction addItemAtEnd(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.insertBefore(frag, null);\n}    \n\n// For calling by host templating code: Remove the item with the given\n// id.\nfunction removeItem(id) {\n    elt = document.getElementById(id);\n    elt.parentNode.removeChild(elt);\n}    \n\n// Internal use: Sometime if all you do is change the style on a node,\n// Safari doesn\'t update the view until your mouse is next over the\n// window. Force the issue by making a drastic change in the vicinity\n// of the given element and then reversing it.\nfunction forceRedisplay(elt) {\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.extractContents();\n    r.insertNode(frag);\n}\n\nfunction handleContextMenuSelect(event) {\n  if(event.button == 2) {\n    var area = event.currentTarget.getAttribute("selectArea");\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var url = \'action:handleContextMenuSelect?id=\' + id + \'&area=\' + area +\n              \'&viewName=\' + viewName;\n    eventURL(url);\n  }\n  return true;\n}\n\nfunction handleSelect(event) {\n   if(event.target.tagName && event.target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n    }\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var area = event.currentTarget.getAttribute("selectArea");\n    var shiftKey = \'0\';\n    var ctrlKey = \'0\';\n    if(event.shiftKey) shiftKey = \'1\';\n    if(event.ctrlKey || event.metaKey) ctrlKey = \'1\';\n    eventURL(\'action:handleSelect?area=\' + area + \'&viewName=\' + viewName + \n\t\'&id=\' + id + \'&shiftDown=\' + shiftKey + \'&ctrlDown=\' + ctrlKey);\n    return true;\n}\n\nfunction handleDblClick(event, viewName, id) {\n   var target = event.target;\n   while (target != undefined && target.ondblclick === null && target.tagName.toUpperCase() != \'A\') {\n       target = target.parentNode;\n   }\n\n   if(target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n   } else {\n       return eventURL(\'action:playViewNamed?viewName=\' + viewName + \n           \'&firstItemId=\' + id);\n   }\n}\n\nfunction getKeyFromEvent(evt) {\n  var key = 0;\n  if (window.event)  {\n    key = evt.keyCode;\n  } else if (evt.which) {\n  \tkey = evt.which;\n  }\n\n  return key;\n}\n\nfunction sendKeyToSearchBox(event) {\n  if(event.altKey || event.ctrlKey || event.metaKey ||\n      (event.target.tagName && event.target.tagName.toUpperCase() == \'INPUT\'))\n      return true;\n  var key = getKeyFromEvent(event);\n  if ((key == 33) || (key == 34) || (key == 35) || (key == 36) || \n      (key == 37) || (key == 38) || (key == 39) || (key == 40))\n      return true;\n  var searchBox = document.getElementById("search-box");\n  searchBox.focus();\n  return true;\n}\n\nfunction playNewVideos(event, id) {\n  eventURL(\'action:playNewVideos?id=\' + id);\n  event.stopPropagation(); // don\'t want handleSelect to deal with this event\n  return false;\n}\n\n///////////////////////////////////////////////////////////////////////////////\n///////////////////////////////////////////////////////////////////////////////\n\n-->\n</script>\n\n<script type="text/javascript">\n    <!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n    var settingsMode = \'closed\';\n\n    function showSettings()\n    {\n        if(settingsMode == \'open\') return hideSettings();\n        var feedSettings = document.getElementById("feed-settings");\n        feedSettings.style.display = "block";\n        settingsMode = \'open\';\n        return false;\n    }\n\n    function hideSettings()\n    {\n        var feedSettings = document.getElementById("feed-settings");\n        feedSettings.style.display = "none";\n        settingsMode = \'closed\';\n        return false;\n    }\n\n    function setExpiration()\n    {\n        var url = "action:setExpiration";\n        var idx = document.forms[\'settings\'][\'expireAfter\'].selectedIndex;\n        var value = document.forms[\'settings\'][\'expireAfter\'].options[idx].value;\n\n        url += \'?feed=\' + document.forms[\'settings\'][\'feed\'].value;\n        if (value == \'system\' || value == \'never\')\n        {\n            url += "&type=" + value + "&time=0";\n        }\n        else\n        {\n            url += "&type=feed&time=" + value;\n        }\n\n        eventURL(url);\n    }\n\n    function setMaxNew()\n    {\n        var url = "action:setMaxNew";\n\n        url += \'?feed=\' + document.forms[\'settings\'][\'feed\'].value;\n        if (document.forms[\'settings\'][\'maxOutDownloads\'].checked)\n        {\n            var maxNew = document.forms[\'settings\'][\'maxNew\'];\n            maxNew.disabled = false;\n            if(maxNew.value == \'\') maxNew.value = \'0\';\n            if(!(parseInt(maxNew.value) >= 0)) {\n               eventURL(\'action:invalidMaxNew?value=\' + escape(maxNew.value));\n               maxNew.value = \'0\';\n            }\n            url += \'&maxNew=\' + maxNew.value;\n        }\n        else\n        {\n            document.forms[\'settings\'][\'maxNew\'].disabled = true;\n            url += \'&maxNew=-1\';\n        }\n\n        eventURL(url);\n    }\n\n    -->\n</script>\n\n</head>\n    \n\n<body')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n\n<form action="javascript:eventURL(\'template:channel?id=')
    out.write(quoteattr(urlencode(feed.getID())))
    out.write(u'\')" method="GET" name="settings">\n\t<input type="hidden" name="feed" value="')
    out.write(quoteattr(urlencode(feed.getID())))
    out.write(u'"></input>\n\t\n\t<div id="settings-inner">\n            <div id="channel-url">\n                <div class="selectable">')
    out.write(escape(feed.getURL()))
    out.write(u'</div>\n                <div><a href="#" class="remove-channel" onclick="return eventURL(\'action:removeFeed?id=')
    out.write(quoteattr(urlencode(feed.getID())))
    out.write(u'\');"><span>')
    out.write(_(u'remove channel'))
    out.write(u'</span></a></div>\n            </div>\n\t<h2>')
    tmplcomp60765835 = {}
    tmplcomp74297851 = StringIO()
    tmplcomp74297851.write(u'<span>')
    tmplcomp74297851.write(escape(feed.getTitle()))
    tmplcomp74297851.write(u'</span>')
    tmplcomp74297851.seek(0)
    tmplcomp60765835['title'] = tmplcomp74297851.read()
    out.write(Template(_(u'Settings for ${title}')).substitute(tmplcomp60765835))
    out.write(u'</h2> \n\t\t\t\t\n\t\t<div id="actual-settings">\n\t\t\n\t\t<span>')
    out.write(_(u'Videos expire after'))
    out.write(u'</span>\n\t\t<select onChange="javascript:setExpiration();" name="expireAfter">\n\t\t\t')
    if not (feed.getExpirationType() != 'system'):
        out.write(u'<option selected="1" value="system"><span>')
        out.write(_(u'Default'))
        out.write(u'</span> \n(<span>')
        out.write(escape(feed.getFormattedDefaultExpiration()))
        out.write(u'</span>)</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationType() ==  'system'):
        out.write(u'<option value="system"><span>')
        out.write(_(u'default'))
        out.write(u'</span> (<span>')
        out.write(escape(feed.getFormattedDefaultExpiration()))
        out.write(u'</span>)</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime()  != 3):
        out.write(u'<option selected="1" value="3">3 hours</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() == 3):
        out.write(u'<option value="3">3 hours</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() != 24):
        out.write(u'<option selected="1" value="24">1 day</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() == 24):
        out.write(u'<option value="24">1 day</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() != 72):
        out.write(u'<option selected="1" value="72">3 days</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() == 72):
        out.write(u'<option value="72">3 days</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() != 144):
        out.write(u'<option selected="1" value="144">6 days</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() == 144):
        out.write(u'<option value="144">6 days</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() != 240):
        out.write(u'<option selected="1" value="240">10 days</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() == 240):
        out.write(u'<option value="240">10 days</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() != 720):
        out.write(u'<option selected="1" value="720">1 month</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationTime() == 720):
        out.write(u'<option value="720">1 month</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationType() != 'never'):
        out.write(u'<option selected="1" value="never">Never</option>')
    out.write(u'\n\t\t\t')
    if not (feed.getExpirationType() ==  'never'):
        out.write(u'<option value="never">Never</option>')
    out.write(u'\n\t\t</select>\n<br></br><br></br>\n\t\t')
    if not (feed.getMaxNew() == 'unlimited'):
        out.write(u'<input checked="checked" type="checkbox" name="maxOutDownloads" onClick="javascript:setMaxNew();"></input>')
    out.write(u'\n\t\t')
    if not (feed.getMaxNew() != 'unlimited'):
        out.write(u'<input type="checkbox" name="maxOutDownloads" onClick="javascript:setMaxNew();"></input>')
    out.write(u'\n\t\t<span>')
    tmplcomp39784944 = {}
    tmplcomp70226240 = StringIO()
    if not (feed.getMaxNew() == 'unlimited'):
        tmplcomp70226240.write(u'<input onBlur="javascript:setMaxNew();" name="maxNew" value="')
        tmplcomp70226240.write(quoteattr(urlencode(feed.getMaxNew())))
        tmplcomp70226240.write(u'" type="text" size="3"></input>')
    tmplcomp70226240.seek(0)
    tmplcomp39784944['maxnew2'] = tmplcomp70226240.read()
    tmplcomp34420342 = StringIO()
    if not (feed.getMaxNew() != 'unlimited'):
        tmplcomp34420342.write(u'<input onBlur="javascript:setMaxNew();" name="maxNew" value="3" disabled="1" type="text" size="3"></input>')
    tmplcomp34420342.seek(0)
    tmplcomp39784944['maxnew'] = tmplcomp34420342.read()
    out.write(Template(_(u"Don't Auto Download when more than ${maxnew} ${maxnew2} videos are waiting unwatched.")).substitute(tmplcomp39784944))
    out.write(u'</span><div class="settings-small">')
    out.write(_(u'Prevents this channel from using unlimited disk space.'))
    out.write(u'</div>\n\n\t    <div class="gray-button-wrap settings-button">\n\t\t    <div id="feed-settings-close-button" onclick="return hideSettings()" class="gray-button-bg">\n                <div class="gray-button-left"></div>\n                <div class="gray-button-right"></div>\n                <div class="gray-button-content" i18:translate="">Done</div>\n            </div>\n\t</div>\n \t</div>         \n</div>\n\n\n</form>\n\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
