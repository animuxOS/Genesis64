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
    
    #print templateState
    from miro import searchengines
    searchFeed = views.feeds.filterWithIndex(indexes.feedsByURL, 'dtv:search')
    feed = searchFeed[0]
    
    searchItems = views.items.filterWithIndex(indexes.itemsByFeed, feed.getID())
    searchItemsSorted = searchItems.sort(sorts.itemSortSearch.sort, resort=True)
    searchEngines = views.searchEngines
    
    def setSortBy(by, section, handle):
        sorts.itemSortSearch.setSortBy(by)
        searchItems.recomputeSort(searchItemsSorted)
        handle.forceUpdate()
    
        
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle = Handle(domHandler, localvars, onUnlink = lambda:None)

    def up_0_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n      <div id="engine-search">\n         <form onsubmit="return performSearch();" name="search">\n         ')
        out.write(searchengines.getSearchEnginesHTML())
        out.write(u'\n         <input name="query" onKeyPress="return validateSearch(event);" value="')
        out.write(quoteattr(feed.quoteLastQuery()))
        out.write(u'" onKeyUp="return fillSearch();" type="search" id="search-box"></input>\n         <input type="submit" value="')
        out.write(quoteattr(_('Search')))
        out.write(u'"></input>      \n         </form>\n      </div>\n      </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp02754863','nextSibling',searchFeed,up_0_handle, u'searchFeed')
    def up_1_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n                ')
        if not (not (feed.getStatus() == 'idle-empty')):
            out.write(u'<div class="search-message">\n                    <span>')
            out.write(_(u'No videos found.<br></br> Enter a query in the search field above.'))
            out.write(u'</span>\n                </div>')
        out.write(u'\n                ')
        if not (not (feed.getStatus() == 'searching')):
            out.write(u'<div class="search-message">\n                    <span>')
            out.write(_(u'Searching...'))
            out.write(u'</span>\n                </div>')
        out.write(u'\n                ')
        if not (not (feed.getStatus() == 'idle-no-results')):
            out.write(u'<div class="search-message">\n                    <span>')
            out.write(_(u'No matching videos found.<br></br> Enter a different query in the search field above.'))
            out.write(u'</span>\n                </div>')
        out.write(u'\n                ')
        if not (not (feed.getStatus() == 'idle-with-results')):
            out.write(u'<div class="search-results-bar">\n\t\t\t<div id="results-text">')
            tmplcomp12758846 = {}
            tmplcomp85659343 = StringIO()
            tmplcomp85659343.write(u'<span>')
            tmplcomp85659343.write(escape(feed.lastQuery))
            tmplcomp85659343.write(u'</span>')
            tmplcomp85659343.seek(0)
            tmplcomp12758846['query'] = tmplcomp85659343.read()
            out.write(Template(_(u'Results for "${query}"')).substitute(tmplcomp12758846))
            out.write(u'</div>\n\t\t\t<div class="white-button-left save-search-searchpage">\n\t\t\t<div class="white-button-right">\n\t\t\t<div class="white-button-middle">\n                        <a href="#" onclick="return eventURL(\'action:addEngineSearchFeed?term=')
            out.write(quoteattr(urlencode(feed.lastQuery)))
            out.write(u'&name=')
            out.write(quoteattr(urlencode(feed.lastEngine)))
            out.write(u'\');">Save This Search as a Channel</a>\n\t\t\t</div>\n\t\t\t</div>\n\t\t\t</div>\n                </div>')
        out.write(u'\n            </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp60920477','nextSibling',searchFeed,up_1_handle, u'searchFeed')
    def up_2_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n                ')
        if not (searchItemsSorted.len() == 0):
            out.write(u'<div>\n                    ')
            out.write(fillStaticTemplate(u'static-tab-sort-bar', onlyBody=True, section='main', itemSort=sorts.itemSortSearch))
            out.write(u'\n                </div>')
        out.write(u'\n            </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp43414285','nextSibling',searchItemsSorted,up_2_handle, u'searchItemsSorted')
    def rep_3_handle(this, viewName, view, tid):
        out = StringIO()
        out.write(u'\n<div dragsourcetype="')
        out.write(quoteattr(this.getDragType()))
        out.write(u'" selectArea="itemlist" drageffectdownloadeditem="move" dragdestdata="playlistitem-')
        out.write(quoteattr(this.getID()))
        out.write(u'" dragicon="video-tnail-')
        out.write(quoteattr(viewName + str(this.getID())))
        out.write(u'" selectID="')
        out.write(quoteattr(this.getID()))
        out.write(u'" class="main-video draggable ')
        out.write(quoteattr(this.getSelectedState(view)))
        out.write(u' ')
        out.write(quoteattr(this.getMoreInfoState()))
        out.write(u'" dragsourcedata="itemlist-')
        out.write(quoteattr(this.getID()))
        out.write(u'" onclick="return handleSelect(event);" selectViewName="')
        out.write(quoteattr(urlencode(viewName)))
        out.write(u'" onmousedown="return handleContextMenuSelect(event);" dragdesttype="')
        out.write(quoteattr(viewName == 'playlistView' and 'downloadeditem' or ''))
        out.write(u'" ondblclick="return handleDblClick(event, \'')
        out.write(quoteattr(urlencode(viewName)))
        out.write(u"', ")
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u');" id="')
        out.write(quoteattr(tid))
        out.write(u'">\n    <div>')
        out.write(this.getItemXML(viewName))
        out.write(u'</div>\n</div>\n')
        out.seek(0)
        return out
    handle.addView('tmplcomp29193808','containerDiv',searchItemsSorted,rep_3_handle, u'searchItemsSorted')
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
    out.write(u'" xmlns:t="http://www.participatorypolitics.org/" xmlns="http://www.w3.org/1999/xhtml" xmlns:i18n="http://www.participatoryculture.org/i18n">\n\n    <head>\n        <meta content="text/html; charset=utf-8" http-equiv="content-type"></meta>\n        <link href="')
    out.write(quoteattr(resources.url(u'css/main.css')))
    out.write(u'" type="text/css" rel="stylesheet"></link>\n        <script type="text/javascript">\n<!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n///////////////////////////////////////////////////////////////////////////////\n//// For use on your page                                                  ////\n///////////////////////////////////////////////////////////////////////////////\n\nfunction getDTVPlatform() {\n    var elt = document.getElementsByTagName("html")[0];\n    return elt.getAttribute(\'dtvPlatform\');\n}\n\nfunction loadURL(url) {\n    try {\n        document.location.href = url;\n    } catch (e) {\n        // This may happen if the backend decides to handle the url load\n        // itself.\n    }\n}\n\n// For calling from page Javascript: Cause a URL to be loaded. The\n// assumption is that the application will notice, abort the load, and\n// take some action based on the URL.\nfunction eventURL(url) {\n    if (typeof(window.frontend) == \'undefined\') {\n\t// Generic strategy: trigger a load, and hope the application\n\t// catches it and cancels it without creating a race\n\t// condition.\n        loadURL(url)\n    } else {\n\t// OS X WebKit (KHTML) strategy: pass in an Objective C object\n\t// through the window object and call a method on it.\n\twindow.frontend.eventURL(url);\n    }\n\n    return false;\n}\n\n// Calls eventURL, then calls event.stopPropagation() and\n// event.preventDefault() so that the event chain is stopped.\nfunction eventURLAndStop(url, event) {\n  eventURL(url);\n  event.stopPropagation();\n  event.preventDefault();\n}\n\nfunction recommendItem(title, url) {\n    loadURL(\'http://www.videobomb.com/index/democracyemail?url=\' + \n            url + \'&title=\' + title);\n    return false;\n}\n\nfunction recommendChannel(title, url) {\n    // See also app.py if changing this URL\n    loadURL(\'http://www.videobomb.com/democracy_channel/email_friend\' +\n        \'?url=\' + url + \'&title=\' + title);\n    return false;\n}\n\n// Start the video player. The playlist will be the items in the view\n// named by viewName. If firstItemId is the id of an item in the view,\n// playback will start on that item; otherwise playback will start on\n// the first item.\nfunction playViewNamed(viewName, firstItemId) {\n    url = \'action:playViewNamed?\';\n    url = url + \'viewName=\' + URLencode(viewName);\n    url = url + \'&firstItemId=\' + URLencode(firstItemId);\n    eventURL(url);\n    return false;\n}\n\n// You can make \'incremental search\' text boxes on your page that\n// effectively tie the text box to the \'parameter\' argument of setViewFilter,\n// with the other argumens fixed. To do this, add these two attributes to\n// the text box:\n//   onfocus="startEditSearch(this)"\n//   onblur="endEditFilter()"\n// replacing the arguments in parentheses with the desired strings.\n//\n// You\'ll also need to provide a updateSearchString function at the\n// top of your template to perform the actual update\n\nvar editSearchField = null;\nvar editSearchOldValue = \'\';\nvar editSearchTimer = null;\nvar editSearchCallback = null;\n\nfunction onSearchFocus(obj){\n  if (obj.getAttribute(\'searching\') != \'1\') {\n\tobj.value="";\n\tobj.searching = \'1\';\n  }\n  startEditSearch(obj, null);\n}\n\nfunction startEditSearch(obj, callback) {\n  editSearchOldValue = obj.value;\n\n  editSearchField = obj;\n  editSearchCallback = callback;\n  editSearchTimerTick();\n}\n\nfunction editSearchUpdate() {\n    value = editSearchField.value;\n    if (editSearchOldValue != value) {\n\turl = \'action:setSearchString?searchString=\' + URLencode(value);\n\teventURL(url);\n\teditSearchOldValue = value;\n\tif(editSearchCallback) editSearchCallback();\n    }\n}\n\nfunction editSearchTimerTick() {\n    editSearchUpdate();\n    editSearchTimer = setTimeout(editSearchTimerTick, 50);\n}\n\nfunction endEditSearch() {\n  clearTimeout(editSearchTimer);\n  editSearchUpdate();\n}\n\n// Internal use: \'URL encode\' the given string.\nfunction URLencode(str) {\n    return encodeURIComponent(str)\n}\n\nfunction URLdecode(str) {\n  return decodeURIComponent(str)\n}\n\nvar currentSelectBoxMenu = null;\nfunction showSelectBoxMenu(id) {\n    document.getElementById(id).style.display = \'block\';\n    currentSelectBoxMenu = id;\n    document.addEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\nfunction hideSelectBoxMenu(event) {\n    document.getElementById(currentSelectBoxMenu).style.display = \'\';\n    currentSelectBoxMenu = null;\n    document.removeEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\n///////////////////////////////////////////////////////////////////////////////\n//// For calling by host templating code                                   ////\n///////////////////////////////////////////////////////////////////////////////\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it disappear.\nfunction hideItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'none\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it visible if it was previously hidden.\nfunction showItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Replace the item with the\n// given id with the element described by the proided XML.\nfunction changeItem(id, newXML) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.replaceChild(frag, elt);\n}\n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element immediately before the item\n// with the given id, such that the newly inserted item has the same\n// parent.\nfunction addItemBefore(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.insertBefore(frag, elt);\n}    \n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element as the final child of the\n// item with the given id.\nfunction addItemAtEnd(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.insertBefore(frag, null);\n}    \n\n// For calling by host templating code: Remove the item with the given\n// id.\nfunction removeItem(id) {\n    elt = document.getElementById(id);\n    elt.parentNode.removeChild(elt);\n}    \n\n// Internal use: Sometime if all you do is change the style on a node,\n// Safari doesn\'t update the view until your mouse is next over the\n// window. Force the issue by making a drastic change in the vicinity\n// of the given element and then reversing it.\nfunction forceRedisplay(elt) {\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.extractContents();\n    r.insertNode(frag);\n}\n\nfunction handleContextMenuSelect(event) {\n  if(event.button == 2) {\n    var area = event.currentTarget.getAttribute("selectArea");\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var url = \'action:handleContextMenuSelect?id=\' + id + \'&area=\' + area +\n              \'&viewName=\' + viewName;\n    eventURL(url);\n  }\n  return true;\n}\n\nfunction handleSelect(event) {\n   if(event.target.tagName && event.target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n    }\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var area = event.currentTarget.getAttribute("selectArea");\n    var shiftKey = \'0\';\n    var ctrlKey = \'0\';\n    if(event.shiftKey) shiftKey = \'1\';\n    if(event.ctrlKey || event.metaKey) ctrlKey = \'1\';\n    eventURL(\'action:handleSelect?area=\' + area + \'&viewName=\' + viewName + \n\t\'&id=\' + id + \'&shiftDown=\' + shiftKey + \'&ctrlDown=\' + ctrlKey);\n    return true;\n}\n\nfunction handleDblClick(event, viewName, id) {\n   var target = event.target;\n   while (target != undefined && target.ondblclick === null && target.tagName.toUpperCase() != \'A\') {\n       target = target.parentNode;\n   }\n\n   if(target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n   } else {\n       return eventURL(\'action:playViewNamed?viewName=\' + viewName + \n           \'&firstItemId=\' + id);\n   }\n}\n\nfunction getKeyFromEvent(evt) {\n  var key = 0;\n  if (window.event)  {\n    key = evt.keyCode;\n  } else if (evt.which) {\n  \tkey = evt.which;\n  }\n\n  return key;\n}\n\nfunction sendKeyToSearchBox(event) {\n  if(event.altKey || event.ctrlKey || event.metaKey ||\n      (event.target.tagName && event.target.tagName.toUpperCase() == \'INPUT\'))\n      return true;\n  var key = getKeyFromEvent(event);\n  if ((key == 33) || (key == 34) || (key == 35) || (key == 36) || \n      (key == 37) || (key == 38) || (key == 39) || (key == 40))\n      return true;\n  var searchBox = document.getElementById("search-box");\n  searchBox.focus();\n  return true;\n}\n\nfunction playNewVideos(event, id) {\n  eventURL(\'action:playNewVideos?id=\' + id);\n  event.stopPropagation(); // don\'t want handleSelect to deal with this event\n  return false;\n}\n\n///////////////////////////////////////////////////////////////////////////////\n///////////////////////////////////////////////////////////////////////////////\n\n-->\n</script>\n\n        <script src="')
    out.write(quoteattr(resources.url(u'templates/search.js')))
    out.write(u'" type="text/javascript"></script>\n        <script src="')
    out.write(quoteattr(resources.url(u'templates/osxdnd.js')))
    out.write(u'" type="text/javascript"></script>\n\n    \n    <t:execOnUnLoad>\nsearchFeed.unlink()\nsearchItems.unlink()\n\n</t:execOnUnLoad>\n\n</head>\n\n<body onkeydown="sendKeyToSearchBox(event);"')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n  <div id="main-titlebar">\n      <div id="main-icon" class="noborder"><img src="')
    out.write(quoteattr(resources.url(u'images/search-icon.png')))
    out.write(u'"></img></div>\n      <h1 id="main-title">')
    out.write(_(u'Video Search'))
    out.write(u'</h1>\n      ')
    out.write(u'<span id="tmplcomp02754863"/>\n  </div>\n\n        <div id="main-container">\n            ')
    out.write(u'<span id="tmplcomp60920477"/>\n            \n\t    ')
    out.write(u'<span id="tmplcomp43414285"/>\n\n            <div id="search-results">\n                <div id="tmplcomp29193808">')
    out.write(u'</div>\n            </div>\n        </div>\n    </body>\n\n</html>')
    out.seek(0)


    return (out, handle)
