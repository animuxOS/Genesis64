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
    
    guideTabs = views.guideTabs
    staticTabs = views.staticTabs
    feedTabs = kargs['channelTabOrder'].getView()
    playlistTabs = kargs['playlistTabOrder'].getView()
    
        
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle = Handle(domHandler, localvars, onUnlink = lambda:None)

    def rep_0_handle(this, viewName, view, tid):
        out = StringIO()
        out.write(u'<li onmousedown="return handleContextMenuSelect(event);" selectArea="tablist" onclick="return handleSelect(event);" selectViewName="guideTabs" selectID="')
        out.write(quoteattr(this.objID()))
        out.write(u'" class="')
        out.write(quoteattr(this.getState()))
        out.write(u'" id="')
        out.write(quoteattr(tid))
        out.write(u'">\n\t      ')
        out.write(u'\n<a class="feeditem">\n    <div class="line">\n    <img src="')
        out.write(quoteattr(this.obj.getIconURL()))
        out.write(u'" alt="" class="icon"></img>\n    <div class="name">')
        out.write(escape(this.obj.getTitle()))
        out.write(u'</div>\n    </div>\n</a>\n')
        out.write(u'\n\t</li>')
        out.seek(0)
        return out
    handle.addView('tmplcomp21430688','nextSibling',guideTabs,rep_0_handle, u'guideTabs')
    def rep_1_handle(this, viewName, view, tid):
        out = StringIO()
        out.write(u'<li selectID="')
        out.write(quoteattr(this.objID()))
        out.write(u'" selectArea="tablist" onclick="return handleSelect(event);" selectViewName="staticTabs" class="')
        out.write(quoteattr(this.getState()))
        out.write(u'" id="')
        out.write(quoteattr(tid))
        out.write(u'">\n\t    ')
        out.write(u'\n<a class="feeditem noselect">\n    <img src="')
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
        out.write(u'</div>\n    </div>\n</a>\n\n')
        out.write(u'\n\t</li>')
        out.seek(0)
        return out
    handle.addView('tmplcomp22875509','nextSibling',staticTabs,rep_1_handle, u'staticTabs')
    def rep_2_handle(this, viewName, view, tid):
        out = StringIO()
        out.write(u'<li onmousedown="return handleContextMenuSelect(event);" selectArea="tablist" onclick="return handleSelect(event)" selectViewName="feedTabs" selectID="')
        out.write(quoteattr(this.objID()))
        out.write(u'" class="')
        out.write(quoteattr(this.getState()))
        out.write(u'" id="')
        out.write(quoteattr(tid))
        out.write(u'">\n        <div id="tab-')
        out.write(quoteattr(this.objID()))
        out.write(u'">\n\t  ')
        if not (not (this.isFeed())):
            out.write(u'<div>\n\t      ')
            out.write(u'\n\n<div dragdestdata="channel-')
            out.write(quoteattr(this.objID()))
            out.write(u'" dragdesttype="')
            out.write(quoteattr(this.obj.getDragDestType()))
            out.write(u'" drageffectchannel="move" class="tab-drop-target ')
            out.write(quoteattr(this.obj.getFolder() and 'child' or ''))
            out.write(u'" drageffectchannelfolder="move">\n<div class="dnd-reorder-indicator circle"></div>\n<div class="dnd-reorder-indicator line"></div>\n<a dragsourcetype="')
            out.write(quoteattr(this.getDragSourceType()))
            out.write(u'" dragicon="channel-tnail-')
            out.write(quoteattr(this.objID()))
            out.write(u'" class="feeditem draggable noselect ')
            out.write(quoteattr(this.obj.isBlinking() and 'blinking' or ''))
            out.write(u'" dragsourcedata="tablist-')
            out.write(quoteattr(this.objID()))
            out.write(u'">\n')
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
            out.write(u'\n<div class="line">\n')
            if not (not (this.obj.isUpdating())):
                out.write(u'<div class="feed-loading-icon"></div>')
            out.write(u'\n<img src="')
            out.write(quoteattr(this.obj.getTablistThumbnail()))
            out.write(u'" id="channel-tnail-')
            out.write(quoteattr(this.objID()))
            out.write(u'" class="icon"></img><div class="name noselect">')
            out.write(escape(this.obj.getTitle()))
            out.write(u'</div>\n</div>\n</a>\n</div>\n\n')
            out.write(u'\n\t    </div>')
        out.write(u'\n\t  ')
        if not (not (this.isChannelFolder())):
            out.write(u'<div>\n\t      ')
            out.write(u'\n\n<div dragdestdata="channelfolder-')
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
            out.write(u'</div>\n</div>\n</a>\n</div>\n</div>\n')
            out.write(u'\n\t  </div>')
        out.write(u'\n        </div>\n      </li>')
        out.seek(0)
        return out
    handle.addView('tmplcomp18811378','nextSibling',feedTabs,rep_2_handle, u'feedTabs')
    def rep_3_handle(this, viewName, view, tid):
        out = StringIO()
        out.write(u'<li onmousedown="return handleContextMenuSelect(event);" selectArea="tablist" onclick="return handleSelect(event);" selectViewName="playlistTabs" selectID="')
        out.write(quoteattr(this.objID()))
        out.write(u'" class="')
        out.write(quoteattr(this.getState()))
        out.write(u'" id="')
        out.write(quoteattr(tid))
        out.write(u'">\n        <div id="tab-')
        out.write(quoteattr(this.objID()))
        out.write(u'">\n\t  ')
        if not (not (this.isPlaylist())):
            out.write(u'<div>\n\t      ')
            out.write(u'\n\n<div dragdestdata="playlist-')
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
            out.write(u'</div>\n</div>\n</a>\n</div>\n</div>\n')
            out.write(u'\n\t  </div>')
        out.write(u'\n\t  ')
        if not (not (this.isPlaylistFolder())):
            out.write(u'<div>\n              ')
            out.write(u'\n\n<div dragdestdata="playlistfolder-')
            out.write(quoteattr(this.objID()))
            out.write(u'" dragdesttype="playlistfolder" drageffectplaylistfolder="move" class="tab-drop-target">\n<div class="dnd-reorder-indicator circle"></div>\n<div class="dnd-reorder-indicator line"></div>\n<div dragdestdata="playlistfolder-')
            out.write(quoteattr(this.objID()))
            out.write(u'" drageffectplaylist="move" dragdesttype="playlist" class="tab-container-drop-target">\n<div class="dnd-container-drop-indicator left"></div>\n<div class="dnd-container-drop-indicator mid"></div>\n<div class="dnd-container-drop-indicator right"></div>\n<a dragsourcetype="playlistfolder" dragicon="playlist-tnail-')
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
            out.write(u'\n<div class="line">\n<img src="')
            out.write(quoteattr(resources.url(u'images/folder-icon-tablist.png')))
            out.write(u'" id="playlist-tnail-')
            out.write(quoteattr(this.objID()))
            out.write(u'" class="icon"></img><div class="name">')
            out.write(escape(this.obj.getTitle()))
            out.write(u'</div>\n</div>\n</a>\n</div>\n</div>\n')
            out.write(u'\n\t  </div>')
        out.write(u'\n        </div>\n      </li>')
        out.seek(0)
        return out
    handle.addView('tmplcomp19184334','nextSibling',playlistTabs,rep_3_handle, u'playlistTabs')
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
    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_3 = Handle(domHandler, localvars, onUnlink = lambda:None)

    handle.addSubHandle(handle_3)
    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_4 = Handle(domHandler, localvars, onUnlink = lambda:None)

    handle.addSubHandle(handle_4)
    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_5 = Handle(domHandler, localvars, onUnlink = lambda:None)

    handle.addSubHandle(handle_5)


    out = StringIO()
    out.write(u"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n")
    out.write(u'<html dtvPlatform="')
    out.write(quoteattr(urlencode(dtvPlatform)))
    out.write(u'" eventCookie="')
    out.write(quoteattr(urlencode(eventCookie)))
    out.write(u'" xmlns:t="http://www.participatorypolitics.org/" xmlns="http://www.w3.org/1999/xhtml" xmlns:i18n="http://www.participatoryculture.org/i18n">\n<head>\n    <title>video player interface</title>\n\n    <link href="')
    out.write(quoteattr(resources.url(u'css/style.css')))
    out.write(u'" type="text/css" rel="stylesheet"></link>\n    <meta content="text/html; charset=utf-8" http-equiv="content-type"></meta>\n    <script type="text/javascript">\n<!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n///////////////////////////////////////////////////////////////////////////////\n//// For use on your page                                                  ////\n///////////////////////////////////////////////////////////////////////////////\n\nfunction getDTVPlatform() {\n    var elt = document.getElementsByTagName("html")[0];\n    return elt.getAttribute(\'dtvPlatform\');\n}\n\nfunction loadURL(url) {\n    try {\n        document.location.href = url;\n    } catch (e) {\n        // This may happen if the backend decides to handle the url load\n        // itself.\n    }\n}\n\n// For calling from page Javascript: Cause a URL to be loaded. The\n// assumption is that the application will notice, abort the load, and\n// take some action based on the URL.\nfunction eventURL(url) {\n    if (typeof(window.frontend) == \'undefined\') {\n\t// Generic strategy: trigger a load, and hope the application\n\t// catches it and cancels it without creating a race\n\t// condition.\n        loadURL(url)\n    } else {\n\t// OS X WebKit (KHTML) strategy: pass in an Objective C object\n\t// through the window object and call a method on it.\n\twindow.frontend.eventURL(url);\n    }\n\n    return false;\n}\n\n// Calls eventURL, then calls event.stopPropagation() and\n// event.preventDefault() so that the event chain is stopped.\nfunction eventURLAndStop(url, event) {\n  eventURL(url);\n  event.stopPropagation();\n  event.preventDefault();\n}\n\nfunction recommendItem(title, url) {\n    loadURL(\'http://www.videobomb.com/index/democracyemail?url=\' + \n            url + \'&title=\' + title);\n    return false;\n}\n\nfunction recommendChannel(title, url) {\n    // See also app.py if changing this URL\n    loadURL(\'http://www.videobomb.com/democracy_channel/email_friend\' +\n        \'?url=\' + url + \'&title=\' + title);\n    return false;\n}\n\n// Start the video player. The playlist will be the items in the view\n// named by viewName. If firstItemId is the id of an item in the view,\n// playback will start on that item; otherwise playback will start on\n// the first item.\nfunction playViewNamed(viewName, firstItemId) {\n    url = \'action:playViewNamed?\';\n    url = url + \'viewName=\' + URLencode(viewName);\n    url = url + \'&firstItemId=\' + URLencode(firstItemId);\n    eventURL(url);\n    return false;\n}\n\n// You can make \'incremental search\' text boxes on your page that\n// effectively tie the text box to the \'parameter\' argument of setViewFilter,\n// with the other argumens fixed. To do this, add these two attributes to\n// the text box:\n//   onfocus="startEditSearch(this)"\n//   onblur="endEditFilter()"\n// replacing the arguments in parentheses with the desired strings.\n//\n// You\'ll also need to provide a updateSearchString function at the\n// top of your template to perform the actual update\n\nvar editSearchField = null;\nvar editSearchOldValue = \'\';\nvar editSearchTimer = null;\nvar editSearchCallback = null;\n\nfunction onSearchFocus(obj){\n  if (obj.getAttribute(\'searching\') != \'1\') {\n\tobj.value="";\n\tobj.searching = \'1\';\n  }\n  startEditSearch(obj, null);\n}\n\nfunction startEditSearch(obj, callback) {\n  editSearchOldValue = obj.value;\n\n  editSearchField = obj;\n  editSearchCallback = callback;\n  editSearchTimerTick();\n}\n\nfunction editSearchUpdate() {\n    value = editSearchField.value;\n    if (editSearchOldValue != value) {\n\turl = \'action:setSearchString?searchString=\' + URLencode(value);\n\teventURL(url);\n\teditSearchOldValue = value;\n\tif(editSearchCallback) editSearchCallback();\n    }\n}\n\nfunction editSearchTimerTick() {\n    editSearchUpdate();\n    editSearchTimer = setTimeout(editSearchTimerTick, 50);\n}\n\nfunction endEditSearch() {\n  clearTimeout(editSearchTimer);\n  editSearchUpdate();\n}\n\n// Internal use: \'URL encode\' the given string.\nfunction URLencode(str) {\n    return encodeURIComponent(str)\n}\n\nfunction URLdecode(str) {\n  return decodeURIComponent(str)\n}\n\nvar currentSelectBoxMenu = null;\nfunction showSelectBoxMenu(id) {\n    document.getElementById(id).style.display = \'block\';\n    currentSelectBoxMenu = id;\n    document.addEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\nfunction hideSelectBoxMenu(event) {\n    document.getElementById(currentSelectBoxMenu).style.display = \'\';\n    currentSelectBoxMenu = null;\n    document.removeEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\n///////////////////////////////////////////////////////////////////////////////\n//// For calling by host templating code                                   ////\n///////////////////////////////////////////////////////////////////////////////\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it disappear.\nfunction hideItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'none\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it visible if it was previously hidden.\nfunction showItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Replace the item with the\n// given id with the element described by the proided XML.\nfunction changeItem(id, newXML) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.replaceChild(frag, elt);\n}\n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element immediately before the item\n// with the given id, such that the newly inserted item has the same\n// parent.\nfunction addItemBefore(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.insertBefore(frag, elt);\n}    \n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element as the final child of the\n// item with the given id.\nfunction addItemAtEnd(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.insertBefore(frag, null);\n}    \n\n// For calling by host templating code: Remove the item with the given\n// id.\nfunction removeItem(id) {\n    elt = document.getElementById(id);\n    elt.parentNode.removeChild(elt);\n}    \n\n// Internal use: Sometime if all you do is change the style on a node,\n// Safari doesn\'t update the view until your mouse is next over the\n// window. Force the issue by making a drastic change in the vicinity\n// of the given element and then reversing it.\nfunction forceRedisplay(elt) {\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.extractContents();\n    r.insertNode(frag);\n}\n\nfunction handleContextMenuSelect(event) {\n  if(event.button == 2) {\n    var area = event.currentTarget.getAttribute("selectArea");\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var url = \'action:handleContextMenuSelect?id=\' + id + \'&area=\' + area +\n              \'&viewName=\' + viewName;\n    eventURL(url);\n  }\n  return true;\n}\n\nfunction handleSelect(event) {\n   if(event.target.tagName && event.target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n    }\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var area = event.currentTarget.getAttribute("selectArea");\n    var shiftKey = \'0\';\n    var ctrlKey = \'0\';\n    if(event.shiftKey) shiftKey = \'1\';\n    if(event.ctrlKey || event.metaKey) ctrlKey = \'1\';\n    eventURL(\'action:handleSelect?area=\' + area + \'&viewName=\' + viewName + \n\t\'&id=\' + id + \'&shiftDown=\' + shiftKey + \'&ctrlDown=\' + ctrlKey);\n    return true;\n}\n\nfunction handleDblClick(event, viewName, id) {\n   var target = event.target;\n   while (target != undefined && target.ondblclick === null && target.tagName.toUpperCase() != \'A\') {\n       target = target.parentNode;\n   }\n\n   if(target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n   } else {\n       return eventURL(\'action:playViewNamed?viewName=\' + viewName + \n           \'&firstItemId=\' + id);\n   }\n}\n\nfunction getKeyFromEvent(evt) {\n  var key = 0;\n  if (window.event)  {\n    key = evt.keyCode;\n  } else if (evt.which) {\n  \tkey = evt.which;\n  }\n\n  return key;\n}\n\nfunction sendKeyToSearchBox(event) {\n  if(event.altKey || event.ctrlKey || event.metaKey ||\n      (event.target.tagName && event.target.tagName.toUpperCase() == \'INPUT\'))\n      return true;\n  var key = getKeyFromEvent(event);\n  if ((key == 33) || (key == 34) || (key == 35) || (key == 36) || \n      (key == 37) || (key == 38) || (key == 39) || (key == 40))\n      return true;\n  var searchBox = document.getElementById("search-box");\n  searchBox.focus();\n  return true;\n}\n\nfunction playNewVideos(event, id) {\n  eventURL(\'action:playNewVideos?id=\' + id);\n  event.stopPropagation(); // don\'t want handleSelect to deal with this event\n  return false;\n}\n\n///////////////////////////////////////////////////////////////////////////////\n///////////////////////////////////////////////////////////////////////////////\n\n-->\n</script>\n\n    <script src="')
    out.write(quoteattr(resources.url(u'templates/osxdnd.js')))
    out.write(u'" type="text/javascript"></script>\n    \n</head>\n<body')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n\n<div id="sidebar">\n  <div dragdestdata="channel-START" dragdesttype="channel:channelfolder" drageffectchannel="move" class="tab-list-drop-target" drageffectchannelfolder="move">\n    <ul class="tab-list first">\n\t')
    out.write(u'<span id="tmplcomp21430688"/>\n\t')
    out.write(u'<span id="tmplcomp22875509"/>\n    </ul>\n    <div class="dnd-reorder-indicator circle"></div>\n    <div class="dnd-reorder-indicator line"></div>\n  </div>\n  <div dragdestdata="playlist-START" drageffectplaylist="move" dragdesttype="playlist:playlistfolder" drageffectplaylistfolder="move" class="tab-list-drop-target">\n    <ul class="tab-list">\n      ')
    out.write(u'<span id="tmplcomp18811378"/>\n    </ul>\n    <div class="dnd-reorder-indicator circle"></div>\n    <div class="dnd-reorder-indicator line"></div>\n  </div>\n  <div dragdestdata="channel-END" dragdesttype="channel:channelfolder" drageffectchannel="move" class="tab-list-drop-target" drageffectchannelfolder="move">\n\t<div class="dnd-reorder-indicator show-on-top circle"></div>\n\t<div class="dnd-reorder-indicator show-on-top line"></div>\n      <ul class="tab-list">\n      ')
    out.write(u'<span id="tmplcomp19184334"/>\n    </ul>\n  </div>\n  <div dragdestdata="playlist-END" drageffectplaylist="move" dragdesttype="playlist:playlistfolder" drageffectplaylistfolder="move" class="tab-list-drop-target">\n      <div class="dnd-reorder-indicator show-on-top circle"></div>\n      <div class="dnd-reorder-indicator show-on-top line"></div>\n    </div>\n</div>\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
