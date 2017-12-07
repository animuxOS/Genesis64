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

    def up_0_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n')
        if not (allDownloadingItems.len() == 0):
            out.write(u'<div>\n<div class="main-channelbar downloading-channelbar" onclick="return eventURL(\'action:toggleDownloadsView\');">\n  ')
            if not (showDownloads):
                out.write(u'<div class="triangle"></div>')
            out.write(u'\n  ')
            if not (not showDownloads):
                out.write(u'<div class="triangle down"></div>')
            out.write(u'\n  <a href="#" class="download-bar-action" onclick="eventURLAndStop(\'action:cancelDownloads\', event);">Cancel All</a>\n  ')
            if not (allItemsPaused(allDownloadingItems)):
                out.write(u'<a href="#" class="download-bar-action" onclick="eventURLAndStop(\'action:pauseDownloads\', event);">Pause All</a>')
            out.write(u'\n  ')
            if not (allItemsDownloading(allDownloadingItems)):
                out.write(u'<a href="#" class="download-bar-action" onclick="eventURLAndStop(\'action:resumeDownloads\', event);">Resume All</a>')
            out.write(u'\n  ')
            if not (allDownloadingItems.len()==1):
                out.write(u'<span>\n      <span>')
                out.write(escape(allDownloadingItems.len()))
                out.write(u'</span> Downloading</span>')
            out.write(u'\n   ')
            if not (allDownloadingItems.len()!=1):
                out.write(u'<span>1 Downloading</span>')
            out.write(u'\n</div>\n</div>')
        out.write(u'\n</div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp28589914','nextSibling',allDownloadingItems,up_0_handle, u'allDownloadingItems')
    def up_1_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div class="downloading-sort" id="')
        out.write(quoteattr(tid))
        out.write(u'">\n        ')
        if not (downloadingItems.len() == 0):
            out.write(u'<div>\n            ')
            out.write(fillStaticTemplate(u'sort-bar', onlyBody=True, section='downloading', itemSort=itemSortDownloading))
            out.write(u'\n        </div>')
        out.write(u'\n    </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp95406263','nextSibling',downloadingItems,up_1_handle, u'downloadingItems')
    def up_2_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<a href="#" class="main-channelbar available-channelbar" onclick="return eventURL(\'action:toggleNewItemsView\');" id="')
        out.write(quoteattr(tid))
        out.write(u'">\n        ')
        if not (showNewItems):
            out.write(u'<div class="triangle"></div>')
        out.write(u'\n        ')
        if not (not showNewItems):
            out.write(u'<div class="triangle down"></div>')
        out.write(u'\n\n        ')
        if not (not (not isFolder)):
            out.write(u'<div>\n            ')
            if not (not (feed.inlineSearchTerm is None)):
                out.write(u'<div>\n                <span>')
                out.write(escape(notDeleted.len()))
                out.write(u'</span> \n                Items in this Channel\n            </div>')
            out.write(u'\n            ')
            if not (not (feed.inlineSearchTerm is not None)):
                out.write(u'<div>\n                ')
                if not (not (notDeleted.len() == matchingItems.len())):
                    out.write(u'<div>\n                    All <span>')
                    out.write(escape(matchingItems.len()))
                    out.write(u'</span> \n                    Match This Search\n                </div>')
                out.write(u'\n                ')
                if not (notDeleted.len() == matchingItems.len()):
                    out.write(u'<div>\n                    <span>')
                    out.write(escape(matchingItems.len()))
                    out.write(u'</span> \n                    Match This Search\n                </div>')
                out.write(u'\n            </div>')
            out.write(u'\n        </div>')
        out.write(u'\n\n        ')
        if not (not (isFolder)):
            out.write(u'<div>\n            <span>')
            out.write(escape(notDeleted.len()))
            out.write(u'</span> \n            Items in this Channel Folder\n        </div>')
        out.write(u'\n    </a>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp72831069','nextSibling',matchingItems,up_2_handle, u'matchingItems')
    def up_3_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n    ')
        if not (not (showNewItems)):
            out.write(u'<div class="available-sort">\n        ')
            out.write(fillStaticTemplate(u'sort-bar', onlyBody=True, section='main', itemSort=itemSort))
            out.write(u'\n    </div>')
        out.write(u'\n</div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp74057481','nextSibling',matchingItems,up_3_handle, u'matchingItems')
    def up_4_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">  \n  ')
        if not (allItemsMode or not showNewItems or newItems.len() == matchingItems.len()):
            out.write(u'<div>\n      <a href="#" class="main-notification" onclick="return eventURL(\'action:toggleAllItemsMode\');">\n          ')
            if not (isFolder):
                out.write(u'<span><span>')
                out.write(escape(matchingItems.len() - newItems.len()))
                out.write(u'</span> more on this channel &gt;&gt;</span>')
            out.write(u'\n          ')
            if not (not (isFolder)):
                out.write(u'<span><span>')
                out.write(escape(matchingItems.len()))
                out.write(u'</span> items in this channel folder &gt;&gt;</span>')
            out.write(u'\n        </a>\n        <a href="#" class="main-notification-right" onclick="return eventURL(\'action:toggleAllItemsMode\');">&nbsp;</a>\n     <br clear="left"></br>\n  </div>')
        out.write(u'\n</div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp98453751','nextSibling',matchingItems,up_4_handle, u'matchingItems')
    def up_5_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n        ')
        if not (len(allWatchableItems) == 0 or (not isFolder and feed.getURL().startswith('dtv:directoryfeed'))):
            out.write(u'<a href="#" class="main-channelbar downloaded-channelbar" onclick="return eventURL(\'action:toggleWatchableView\')">\n            ')
            if not (showWatchableItems):
                out.write(u'<div class="triangle"></div>')
            out.write(u'\n            ')
            if not (not showWatchableItems):
                out.write(u'<div class="triangle down"></div>')
            out.write(u'\n            <span>')
            tmplcomp56815477 = {}
            tmplcomp81811879 = StringIO()
            tmplcomp81811879.write(u'<span>')
            tmplcomp81811879.write(escape(allWatchableItems.len()))
            tmplcomp81811879.write(u'</span>')
            tmplcomp81811879.seek(0)
            tmplcomp56815477['len'] = tmplcomp81811879.read()
            out.write(Template(_(u'${len} Downloaded')).substitute(tmplcomp56815477))
            out.write(u'</span>\n        </a>')
        out.write(u'\n    </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp57513717','nextSibling',allWatchableItems,up_5_handle, u'allWatchableItems')
    def up_6_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n        ')
        if not (len(watchableItems) == 0):
            out.write(u'<div>\n            ')
            out.write(fillStaticTemplate(u'sort-bar', onlyBody=True, section='watchable', itemSort=itemSortWatchable))
            out.write(u'\n        </div>')
        out.write(u'\n    </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp67539601','nextSibling',watchableItems,up_6_handle, u'watchableItems')
    def rep_7_handle(this, viewName, view, tid):
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
    handle.addView('tmplcomp12109923','containerDiv',downloadingItems,rep_7_handle, u'downloadingItems')
    def rep_8_handle(this, viewName, view, tid):
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
    handle.addView('tmplcomp51210476','containerDiv',newItems,rep_8_handle, u'newItems')
    def rep_9_handle(this, viewName, view, tid):
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
    handle.addView('tmplcomp39536925','containerDiv',watchableItems,rep_9_handle, u'watchableItems')
    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_0 = Handle(domHandler, localvars, onUnlink = lambda:None)

    handle.addSubHandle(handle_0)
    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_1 = Handle(domHandler, localvars, onUnlink = lambda:None)

    handle.addSubHandle(handle_1)
    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_2 = Handle(domHandler, localvars, onUnlink = lambda:None)

    handle.addSubHandle(handle_2)


    out = StringIO()
    out.write(u"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n")
    out.write(u'<html dtvPlatform="')
    out.write(quoteattr(urlencode(dtvPlatform)))
    out.write(u'" eventCookie="')
    out.write(quoteattr(urlencode(eventCookie)))
    out.write(u'" xmlns:t="http://www.participatorypolitics.org/" xmlns="http://www.w3.org/1999/xhtml" xmlns:i18n="http://www.participatoryculture.org/i18n">\n<head>\n    <meta content="text/html; charset=utf-8" http-equiv="content-type"></meta>\n        <script type="text/javascript">\n<!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n///////////////////////////////////////////////////////////////////////////////\n//// For use on your page                                                  ////\n///////////////////////////////////////////////////////////////////////////////\n\nfunction getDTVPlatform() {\n    var elt = document.getElementsByTagName("html")[0];\n    return elt.getAttribute(\'dtvPlatform\');\n}\n\nfunction loadURL(url) {\n    try {\n        document.location.href = url;\n    } catch (e) {\n        // This may happen if the backend decides to handle the url load\n        // itself.\n    }\n}\n\n// For calling from page Javascript: Cause a URL to be loaded. The\n// assumption is that the application will notice, abort the load, and\n// take some action based on the URL.\nfunction eventURL(url) {\n    if (typeof(window.frontend) == \'undefined\') {\n\t// Generic strategy: trigger a load, and hope the application\n\t// catches it and cancels it without creating a race\n\t// condition.\n        loadURL(url)\n    } else {\n\t// OS X WebKit (KHTML) strategy: pass in an Objective C object\n\t// through the window object and call a method on it.\n\twindow.frontend.eventURL(url);\n    }\n\n    return false;\n}\n\n// Calls eventURL, then calls event.stopPropagation() and\n// event.preventDefault() so that the event chain is stopped.\nfunction eventURLAndStop(url, event) {\n  eventURL(url);\n  event.stopPropagation();\n  event.preventDefault();\n}\n\nfunction recommendItem(title, url) {\n    loadURL(\'http://www.videobomb.com/index/democracyemail?url=\' + \n            url + \'&title=\' + title);\n    return false;\n}\n\nfunction recommendChannel(title, url) {\n    // See also app.py if changing this URL\n    loadURL(\'http://www.videobomb.com/democracy_channel/email_friend\' +\n        \'?url=\' + url + \'&title=\' + title);\n    return false;\n}\n\n// Start the video player. The playlist will be the items in the view\n// named by viewName. If firstItemId is the id of an item in the view,\n// playback will start on that item; otherwise playback will start on\n// the first item.\nfunction playViewNamed(viewName, firstItemId) {\n    url = \'action:playViewNamed?\';\n    url = url + \'viewName=\' + URLencode(viewName);\n    url = url + \'&firstItemId=\' + URLencode(firstItemId);\n    eventURL(url);\n    return false;\n}\n\n// You can make \'incremental search\' text boxes on your page that\n// effectively tie the text box to the \'parameter\' argument of setViewFilter,\n// with the other argumens fixed. To do this, add these two attributes to\n// the text box:\n//   onfocus="startEditSearch(this)"\n//   onblur="endEditFilter()"\n// replacing the arguments in parentheses with the desired strings.\n//\n// You\'ll also need to provide a updateSearchString function at the\n// top of your template to perform the actual update\n\nvar editSearchField = null;\nvar editSearchOldValue = \'\';\nvar editSearchTimer = null;\nvar editSearchCallback = null;\n\nfunction onSearchFocus(obj){\n  if (obj.getAttribute(\'searching\') != \'1\') {\n\tobj.value="";\n\tobj.searching = \'1\';\n  }\n  startEditSearch(obj, null);\n}\n\nfunction startEditSearch(obj, callback) {\n  editSearchOldValue = obj.value;\n\n  editSearchField = obj;\n  editSearchCallback = callback;\n  editSearchTimerTick();\n}\n\nfunction editSearchUpdate() {\n    value = editSearchField.value;\n    if (editSearchOldValue != value) {\n\turl = \'action:setSearchString?searchString=\' + URLencode(value);\n\teventURL(url);\n\teditSearchOldValue = value;\n\tif(editSearchCallback) editSearchCallback();\n    }\n}\n\nfunction editSearchTimerTick() {\n    editSearchUpdate();\n    editSearchTimer = setTimeout(editSearchTimerTick, 50);\n}\n\nfunction endEditSearch() {\n  clearTimeout(editSearchTimer);\n  editSearchUpdate();\n}\n\n// Internal use: \'URL encode\' the given string.\nfunction URLencode(str) {\n    return encodeURIComponent(str)\n}\n\nfunction URLdecode(str) {\n  return decodeURIComponent(str)\n}\n\nvar currentSelectBoxMenu = null;\nfunction showSelectBoxMenu(id) {\n    document.getElementById(id).style.display = \'block\';\n    currentSelectBoxMenu = id;\n    document.addEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\nfunction hideSelectBoxMenu(event) {\n    document.getElementById(currentSelectBoxMenu).style.display = \'\';\n    currentSelectBoxMenu = null;\n    document.removeEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\n///////////////////////////////////////////////////////////////////////////////\n//// For calling by host templating code                                   ////\n///////////////////////////////////////////////////////////////////////////////\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it disappear.\nfunction hideItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'none\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it visible if it was previously hidden.\nfunction showItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Replace the item with the\n// given id with the element described by the proided XML.\nfunction changeItem(id, newXML) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.replaceChild(frag, elt);\n}\n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element immediately before the item\n// with the given id, such that the newly inserted item has the same\n// parent.\nfunction addItemBefore(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.insertBefore(frag, elt);\n}    \n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element as the final child of the\n// item with the given id.\nfunction addItemAtEnd(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.insertBefore(frag, null);\n}    \n\n// For calling by host templating code: Remove the item with the given\n// id.\nfunction removeItem(id) {\n    elt = document.getElementById(id);\n    elt.parentNode.removeChild(elt);\n}    \n\n// Internal use: Sometime if all you do is change the style on a node,\n// Safari doesn\'t update the view until your mouse is next over the\n// window. Force the issue by making a drastic change in the vicinity\n// of the given element and then reversing it.\nfunction forceRedisplay(elt) {\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.extractContents();\n    r.insertNode(frag);\n}\n\nfunction handleContextMenuSelect(event) {\n  if(event.button == 2) {\n    var area = event.currentTarget.getAttribute("selectArea");\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var url = \'action:handleContextMenuSelect?id=\' + id + \'&area=\' + area +\n              \'&viewName=\' + viewName;\n    eventURL(url);\n  }\n  return true;\n}\n\nfunction handleSelect(event) {\n   if(event.target.tagName && event.target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n    }\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var area = event.currentTarget.getAttribute("selectArea");\n    var shiftKey = \'0\';\n    var ctrlKey = \'0\';\n    if(event.shiftKey) shiftKey = \'1\';\n    if(event.ctrlKey || event.metaKey) ctrlKey = \'1\';\n    eventURL(\'action:handleSelect?area=\' + area + \'&viewName=\' + viewName + \n\t\'&id=\' + id + \'&shiftDown=\' + shiftKey + \'&ctrlDown=\' + ctrlKey);\n    return true;\n}\n\nfunction handleDblClick(event, viewName, id) {\n   var target = event.target;\n   while (target != undefined && target.ondblclick === null && target.tagName.toUpperCase() != \'A\') {\n       target = target.parentNode;\n   }\n\n   if(target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n   } else {\n       return eventURL(\'action:playViewNamed?viewName=\' + viewName + \n           \'&firstItemId=\' + id);\n   }\n}\n\nfunction getKeyFromEvent(evt) {\n  var key = 0;\n  if (window.event)  {\n    key = evt.keyCode;\n  } else if (evt.which) {\n  \tkey = evt.which;\n  }\n\n  return key;\n}\n\nfunction sendKeyToSearchBox(event) {\n  if(event.altKey || event.ctrlKey || event.metaKey ||\n      (event.target.tagName && event.target.tagName.toUpperCase() == \'INPUT\'))\n      return true;\n  var key = getKeyFromEvent(event);\n  if ((key == 33) || (key == 34) || (key == 35) || (key == 36) || \n      (key == 37) || (key == 38) || (key == 39) || (key == 40))\n      return true;\n  var searchBox = document.getElementById("search-box");\n  searchBox.focus();\n  return true;\n}\n\nfunction playNewVideos(event, id) {\n  eventURL(\'action:playNewVideos?id=\' + id);\n  event.stopPropagation(); // don\'t want handleSelect to deal with this event\n  return false;\n}\n\n///////////////////////////////////////////////////////////////////////////////\n///////////////////////////////////////////////////////////////////////////////\n\n-->\n</script>\n\n\n</head>\n<body')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n\n')
    out.write(u'<span id="tmplcomp28589914"/>\n\n    ')
    out.write(u'<span id="tmplcomp95406263"/>\n    <div id="tmplcomp12109923">')
    out.write(u'</div>\n\n\n\n\n\n<div class="available-channelbar-wrap">\n    ')
    out.write(u'<span id="tmplcomp72831069"/>\n</div>\n\n')
    out.write(u'<span id="tmplcomp74057481"/>\n\n<div id="tmplcomp51210476">')
    out.write(u'</div>\n\n\n')
    out.write(u'<span id="tmplcomp98453751"/>\n\n\n\n\n<div id="tmplcomp68035101"')
    _hideFunc = lambda : not isFolder and feed.getURL().startswith('dtv:directoryfeed')
    _dynHide = _hideFunc()
    if _dynHide:
        out.write(u" style=\"display:none\">")
    else:
        out.write(u">")
    handle.addUpdateHideOnView('tmplcomp68035101',thisFeedView,_hideFunc,_dynHide)
    out.write(u'\n    ')
    out.write(u'<span id="tmplcomp57513717"/>\n    \n    ')
    out.write(u'<span id="tmplcomp67539601"/>\n    <div id="tmplcomp39536925">')
    out.write(u'</div>\n</div>\n\n\n</><!-- HOT SPOT END -->\n</html>')
    out.seek(0)


    return (out, handle)
