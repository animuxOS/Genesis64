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
    
    # Allows this template to be viewed when not included in another
    # template's view
    this = kargs['this']
    viewName = kargs['viewName']
             
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
    out.write(u'" xmlns:t="http://www.participatorypolitics.org/" xmlns="http://www.w3.org/1999/xhtml" xmlns:i18n="http://www.participatoryculture.org/i18n">\n    <head>\n        <meta content="text/html; charset=utf-8" http-equiv="content-type"></meta>\n        <script type="text/javascript">\n<!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n///////////////////////////////////////////////////////////////////////////////\n//// For use on your page                                                  ////\n///////////////////////////////////////////////////////////////////////////////\n\nfunction getDTVPlatform() {\n    var elt = document.getElementsByTagName("html")[0];\n    return elt.getAttribute(\'dtvPlatform\');\n}\n\nfunction loadURL(url) {\n    try {\n        document.location.href = url;\n    } catch (e) {\n        // This may happen if the backend decides to handle the url load\n        // itself.\n    }\n}\n\n// For calling from page Javascript: Cause a URL to be loaded. The\n// assumption is that the application will notice, abort the load, and\n// take some action based on the URL.\nfunction eventURL(url) {\n    if (typeof(window.frontend) == \'undefined\') {\n\t// Generic strategy: trigger a load, and hope the application\n\t// catches it and cancels it without creating a race\n\t// condition.\n        loadURL(url)\n    } else {\n\t// OS X WebKit (KHTML) strategy: pass in an Objective C object\n\t// through the window object and call a method on it.\n\twindow.frontend.eventURL(url);\n    }\n\n    return false;\n}\n\n// Calls eventURL, then calls event.stopPropagation() and\n// event.preventDefault() so that the event chain is stopped.\nfunction eventURLAndStop(url, event) {\n  eventURL(url);\n  event.stopPropagation();\n  event.preventDefault();\n}\n\nfunction recommendItem(title, url) {\n    loadURL(\'http://www.videobomb.com/index/democracyemail?url=\' + \n            url + \'&title=\' + title);\n    return false;\n}\n\nfunction recommendChannel(title, url) {\n    // See also app.py if changing this URL\n    loadURL(\'http://www.videobomb.com/democracy_channel/email_friend\' +\n        \'?url=\' + url + \'&title=\' + title);\n    return false;\n}\n\n// Start the video player. The playlist will be the items in the view\n// named by viewName. If firstItemId is the id of an item in the view,\n// playback will start on that item; otherwise playback will start on\n// the first item.\nfunction playViewNamed(viewName, firstItemId) {\n    url = \'action:playViewNamed?\';\n    url = url + \'viewName=\' + URLencode(viewName);\n    url = url + \'&firstItemId=\' + URLencode(firstItemId);\n    eventURL(url);\n    return false;\n}\n\n// You can make \'incremental search\' text boxes on your page that\n// effectively tie the text box to the \'parameter\' argument of setViewFilter,\n// with the other argumens fixed. To do this, add these two attributes to\n// the text box:\n//   onfocus="startEditSearch(this)"\n//   onblur="endEditFilter()"\n// replacing the arguments in parentheses with the desired strings.\n//\n// You\'ll also need to provide a updateSearchString function at the\n// top of your template to perform the actual update\n\nvar editSearchField = null;\nvar editSearchOldValue = \'\';\nvar editSearchTimer = null;\nvar editSearchCallback = null;\n\nfunction onSearchFocus(obj){\n  if (obj.getAttribute(\'searching\') != \'1\') {\n\tobj.value="";\n\tobj.searching = \'1\';\n  }\n  startEditSearch(obj, null);\n}\n\nfunction startEditSearch(obj, callback) {\n  editSearchOldValue = obj.value;\n\n  editSearchField = obj;\n  editSearchCallback = callback;\n  editSearchTimerTick();\n}\n\nfunction editSearchUpdate() {\n    value = editSearchField.value;\n    if (editSearchOldValue != value) {\n\turl = \'action:setSearchString?searchString=\' + URLencode(value);\n\teventURL(url);\n\teditSearchOldValue = value;\n\tif(editSearchCallback) editSearchCallback();\n    }\n}\n\nfunction editSearchTimerTick() {\n    editSearchUpdate();\n    editSearchTimer = setTimeout(editSearchTimerTick, 50);\n}\n\nfunction endEditSearch() {\n  clearTimeout(editSearchTimer);\n  editSearchUpdate();\n}\n\n// Internal use: \'URL encode\' the given string.\nfunction URLencode(str) {\n    return encodeURIComponent(str)\n}\n\nfunction URLdecode(str) {\n  return decodeURIComponent(str)\n}\n\nvar currentSelectBoxMenu = null;\nfunction showSelectBoxMenu(id) {\n    document.getElementById(id).style.display = \'block\';\n    currentSelectBoxMenu = id;\n    document.addEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\nfunction hideSelectBoxMenu(event) {\n    document.getElementById(currentSelectBoxMenu).style.display = \'\';\n    currentSelectBoxMenu = null;\n    document.removeEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\n///////////////////////////////////////////////////////////////////////////////\n//// For calling by host templating code                                   ////\n///////////////////////////////////////////////////////////////////////////////\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it disappear.\nfunction hideItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'none\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it visible if it was previously hidden.\nfunction showItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Replace the item with the\n// given id with the element described by the proided XML.\nfunction changeItem(id, newXML) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.replaceChild(frag, elt);\n}\n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element immediately before the item\n// with the given id, such that the newly inserted item has the same\n// parent.\nfunction addItemBefore(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.insertBefore(frag, elt);\n}    \n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element as the final child of the\n// item with the given id.\nfunction addItemAtEnd(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.insertBefore(frag, null);\n}    \n\n// For calling by host templating code: Remove the item with the given\n// id.\nfunction removeItem(id) {\n    elt = document.getElementById(id);\n    elt.parentNode.removeChild(elt);\n}    \n\n// Internal use: Sometime if all you do is change the style on a node,\n// Safari doesn\'t update the view until your mouse is next over the\n// window. Force the issue by making a drastic change in the vicinity\n// of the given element and then reversing it.\nfunction forceRedisplay(elt) {\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.extractContents();\n    r.insertNode(frag);\n}\n\nfunction handleContextMenuSelect(event) {\n  if(event.button == 2) {\n    var area = event.currentTarget.getAttribute("selectArea");\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var url = \'action:handleContextMenuSelect?id=\' + id + \'&area=\' + area +\n              \'&viewName=\' + viewName;\n    eventURL(url);\n  }\n  return true;\n}\n\nfunction handleSelect(event) {\n   if(event.target.tagName && event.target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n    }\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var area = event.currentTarget.getAttribute("selectArea");\n    var shiftKey = \'0\';\n    var ctrlKey = \'0\';\n    if(event.shiftKey) shiftKey = \'1\';\n    if(event.ctrlKey || event.metaKey) ctrlKey = \'1\';\n    eventURL(\'action:handleSelect?area=\' + area + \'&viewName=\' + viewName + \n\t\'&id=\' + id + \'&shiftDown=\' + shiftKey + \'&ctrlDown=\' + ctrlKey);\n    return true;\n}\n\nfunction handleDblClick(event, viewName, id) {\n   var target = event.target;\n   while (target != undefined && target.ondblclick === null && target.tagName.toUpperCase() != \'A\') {\n       target = target.parentNode;\n   }\n\n   if(target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n   } else {\n       return eventURL(\'action:playViewNamed?viewName=\' + viewName + \n           \'&firstItemId=\' + id);\n   }\n}\n\nfunction getKeyFromEvent(evt) {\n  var key = 0;\n  if (window.event)  {\n    key = evt.keyCode;\n  } else if (evt.which) {\n  \tkey = evt.which;\n  }\n\n  return key;\n}\n\nfunction sendKeyToSearchBox(event) {\n  if(event.altKey || event.ctrlKey || event.metaKey ||\n      (event.target.tagName && event.target.tagName.toUpperCase() == \'INPUT\'))\n      return true;\n  var key = getKeyFromEvent(event);\n  if ((key == 33) || (key == 34) || (key == 35) || (key == 36) || \n      (key == 37) || (key == 38) || (key == 39) || (key == 40))\n      return true;\n  var searchBox = document.getElementById("search-box");\n  searchBox.focus();\n  return true;\n}\n\nfunction playNewVideos(event, id) {\n  eventURL(\'action:playNewVideos?id=\' + id);\n  event.stopPropagation(); // don\'t want handleSelect to deal with this event\n  return false;\n}\n\n///////////////////////////////////////////////////////////////////////////////\n///////////////////////////////////////////////////////////////////////////////\n\n-->\n</script>\n\n        \n    </head>\n    <body')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n        <div class="dnd-reorder-line"></div>\n        ')
    out.write(u'\n    <img src="')
    out.write(quoteattr(this.getThumbnail()))
    out.write(u'" alt="" class="main-video-tnail" id="video-tnail-')
    out.write(quoteattr(viewName + str(this.getID())))
    out.write(u'"></img>\n\n    <div class="main-video-hitbox">\n        ')
    if not (not (this.isDownloadable())):
        out.write(u'<a href="#" class="icon download" onclick="return eventURL(\'action:startDownload?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');" title="Download \'')
        out.write(quoteattr(this.getTitle()))
        out.write(u'\'"></a>')
    out.write(u'\n        ')
    if not (not (this.getState() == 'paused')):
        out.write(u'<a href="#" class="icon paused-circle" onclick="return eventURL(\'action:startDownload?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');" title="Download \'')
        out.write(quoteattr(this.getTitle()))
        out.write(u'\'"></a>')
    out.write(u'\n        ')
    if not (not (this.getState() == 'downloading')):
        out.write(u'<span class="icon inprogress-background">\n            ')
        if not (this.isPendingManualDownload()):
            out.write(u'<img src="')
            out.write(quoteattr(resources.url(u'images/main-video-inprogress-arrows.gif')))
            out.write(u'" title="Downloading \'')
            out.write(quoteattr(this.getTitle()))
            out.write(u'\'" class="inprogress-arrows"></img>')
        out.write(u'\n            ')
        if not (not (this.isPendingManualDownload())):
            out.write(u'<img src="')
            out.write(quoteattr(resources.url(u'images/download-pending-dot.png')))
            out.write(u'" class="download-pending-icon" title="Download Pending for \'')
            out.write(quoteattr(this.getTitle()))
            out.write(u'\'"></img>')
        out.write(u'\n        </span>')
    out.write(u'\n        ')
    if not (not (this.isPlayable())):
        out.write(u'<a href="#" class="icon play" onclick="return eventURL(\'action:playViewNamed?viewName=')
        out.write(quoteattr(urlencode(viewName)))
        out.write(u'&firstItemId=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');" title="Play \'')
        out.write(quoteattr(this.getTitle()))
        out.write(u'\'"></a>')
    out.write(u'\n    </div>\n')
    out.write(u'\n        ')
    out.write(u'\n    <div class="main-video-details">\n        <div class="main-video-details-top">\n            <div class="details-link">\n                ')
    if not (this.showMoreInfo):
        out.write(u'<div>\n                    <a href="#" onclick="return eventURL(\'action:toggleMoreItemInfo?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');"><span>')
        out.write(_(u'Details'))
        out.write(u'</span> <img src="')
        out.write(quoteattr(resources.url(u'images/more-info-button.png')))
        out.write(u'" alt=""></img></a>\n                </div>')
    out.write(u'\n\n                ')
    if not (not (this.showMoreInfo)):
        out.write(u'<div>\n                    <a href="#" onclick="return eventURL(\'action:toggleMoreItemInfo?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');"><span>')
        out.write(_(u'Close'))
        out.write(u'</span> <img src="')
        out.write(quoteattr(resources.url(u'images/more-info-button-close.png')))
        out.write(u'" alt=""></img></a>\n                </div>')
    out.write(u'\n            </div>\n            <div class="video-stats">\n                <div class="length">\n                    <span>')
    out.write(escape(this.getDuration()))
    out.write(u'</span>\n                </div>\n                <div class="date">\n                    ')
    if not (not (this.getReleaseDate() != '')):
        out.write(u'<span><span>')
        out.write(escape(this.getReleaseDate()))
        out.write(u'</span></span>')
    out.write(u'\n                </div>\n\n                <div class="size">\n                    ')
    if not (not ((this.getURL() != this.getLink() and this.getLink() != '') or this.isDownloaded())):
        out.write(u'<span><span>')
        out.write(escape(this.getSizeForDisplay()))
        out.write(u'</span></span>')
    out.write(u'\n                </div>\n                <div class="torrent">\n                    ')
    if not (not (this.looksLikeTorrent())):
        out.write(u'<span>\n                        <span>')
        out.write(_(u'.torrent'))
        out.write(u'</span>\n                    </span>')
    out.write(u'\n                </div>\n           </div>\n        </div>\n\n        <div class="main-video-details-main">\n            <div class="details-buttons-right">\n                <div class="save-button-container">\n                    ')
    if not (not (this.showSaveButton())):
        out.write(u'<div>\n                        <a href="#" class="round-button-left save" onclick="return eventURL(\'action:keepItem?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');">\n                        <div class="round-button-right">\n                        <div class="round-button-content">\n                            <span>')
        out.write(_(u'KEEP'))
        out.write(u'</span>\n                        </div>\n                        </div>\n                        </a>\n                    </div>')
    out.write(u'\n                    ')
    if not (not (this.showSaved())):
        out.write(u'<div class="saved-note">SAVED</div>')
    out.write(u'\n                </div>\n                ')
    if not (not (this.showTrashButton())):
        out.write(u'<div>\n                    <a href="#" class="round-button-left delete" onclick="return eventURL(\'action:expireItem?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');">\n                    <div class="round-button-right">\n                    <div class="round-button-content">\n                        <span>')
        out.write(_(u'DELETE'))
        out.write(u'</span>\n                    </div>\n                    </div>\n                    </a>\n                </div>')
    out.write(u'\n            </div>\n\n            \n            ')
    if not (not (this.hasSharableURL())):
        out.write(u'<div class="select-box-left share-box" onclick="showSelectBoxMenu(\'share-menu-')
        out.write(quoteattr(urlencode(viewName)))
        out.write(u'-')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\'); event.stopPropagation();">\n                <div class="select-box-right">\n                    <div class="select-box-mid">\n                        SHARE\n                    </div>\n                </div>\n            </div>')
    out.write(u'\n            <br class="clear"></br>\n            <ul id="share-menu-')
    out.write(quoteattr(urlencode(viewName)))
    out.write(u'-')
    out.write(quoteattr(urlencode(this.getID())))
    out.write(u'" class="select-box-menu share-menu">\n                <li>\n                    <a href="#" class="main-video-details-task-mail" onclick="return recommendItem(\'')
    out.write(quoteattr(urlencode(this.getTitle())))
    out.write(u"', '")
    out.write(quoteattr(urlencode(this.getURL())))
    out.write(u"', '")
    out.write(quoteattr(urlencode(this.getFeed().getURL())))
    out.write(u'\');">\n                        <img src="')
    out.write(quoteattr(resources.url(u'images/email-a-friend.gif')))
    out.write(u'" alt="email-a-friend icon"></img>\n                        <span>')
    out.write(_(u'Email to a friend'))
    out.write(u'</span>\n                    </a>\n                </li>\n                <li>\n                    <a href="#" class="main-video-details-task-bomb" onclick="return eventURL(\'action:videoBombExternally?item=')
    out.write(quoteattr(urlencode(this.getID())))
    out.write(u'\');">\n                        <img src="')
    out.write(quoteattr(resources.url(u'images/videobomb.gif')))
    out.write(u'" alt="videobomb icon"></img>\n                        <span>')
    out.write(_(u'Post to Video Bomb'))
    out.write(u'</span>\n                    </a>\n                </li>\n                <li>\n                    <a href="#" class="main-video-details-delicious" onclick="return eventURL(\'http://del.icio.us/post?v=4&noui&jump=close&url=')
    out.write(quoteattr(urlencode(this.getURL())))
    out.write(u'&title=')
    out.write(quoteattr(urlencode(this.getTitle())))
    out.write(u'\');">\n                        <img src="')
    out.write(quoteattr(resources.url(u'images/delicious.gif')))
    out.write(u'" alt="delicious icon"></img>\n                        <span>')
    out.write(_(u'Post to del.icio.us'))
    out.write(u'</span>\n                    </a>\n                </li>\n                <li>\n                    <a href="#" class="main-video-details-digg" onclick="return eventURL(\'http://www.digg.com/submit?phrase=2&url=')
    out.write(quoteattr(urlencode(this.getQuotedURL())))
    out.write(u'\');">\n                        <img src="')
    out.write(quoteattr(resources.url(u'images/digg.gif')))
    out.write(u'" alt="digg icon"></img>\n                        <span>')
    out.write(_(u'Post to digg'))
    out.write(u'</span>\n                    </a>\n                </li>\n                <li>\n                    <a href="#" class="main-video-details-reddit" onclick="return eventURL(\'http://reddit.com/submit?url=')
    out.write(quoteattr(urlencode(this.getQuotedURL())))
    out.write(u'&title=')
    out.write(quoteattr(urlencode(this.getQuotedTitle())))
    out.write(u'\');">\n                        <img src="')
    out.write(quoteattr(resources.url(u'images/reddit.gif')))
    out.write(u'" alt="reddit icon"></img>\n                        <span>')
    out.write(_(u'Post to Reddit'))
    out.write(u'</span>\n                    </a>\n                </li>\n            </ul>\n            <!-- HOT SPOT download-progress-')
    out.write(quoteattr(viewName))
    out.write(u'-')
    out.write(quoteattr(this.getID()))
    out.write(u' --><div id="download-progress-')
    out.write(quoteattr(viewName))
    out.write(u'-')
    out.write(quoteattr(this.getID()))
    out.write(u'">\n                ')
    if not (not (this.getState() in ('downloading','paused'))):
        out.write(u'<div class="main-video-details-download-info">\n                    ')
        if not (not (this.gotContentLength())):
            out.write(u'<div>\n                        <div class="main-progress-bar-bg">\n                            <div style="width: ')
            out.write(quoteattr(this.downloadProgressWidth()))
            out.write(u'px;" class="main-progress-bar"></div>\n                        </div>\n                    </div>')
        out.write(u'\n                    ')
        if not (this.gotContentLength()):
            out.write(u'<div>\n                        <div class="progress-throbber-bg">\n                            ')
            if not (not (this.downloadRate() != '0KB/s')):
                out.write(u'<span>\n                                <img src="')
                out.write(quoteattr(resources.url(u'images/progress-throbber.gif')))
                out.write(u'"></img>\n                            </span>')
            out.write(u'\n                            ')
            if not (not (this.downloadRate() == '0KB/s')):
                out.write(u'<span>\n                                <img src="')
                out.write(quoteattr(resources.url(u'images/progress-throbber-gray.png')))
                out.write(u'"></img>\n                            </span>')
            out.write(u'\n                        </div>\n                    </div>')
        out.write(u'\n                    ')
        if not (not (this.getState() == 'downloading')):
            out.write(u'<div class="downloading">\n                        ')
            if not (not (this.downloadInProgress())):
                out.write(u'<div class="download-rate-and-eta">\n                            <span class="download-rate">')
                out.write(escape(this.downloadRate()))
                out.write(u'</span>\n                            <span>')
                out.write(escape(this.downloadETA()))
                out.write(u'</span>\n                        </div>')
            out.write(u'\n                        ')
            if not (this.downloadInProgress()):
                out.write(u'<div>\n                            <span>')
                out.write(escape(this.getStartupActivity()))
                out.write(u'</span>\n                        </div>')
            out.write(u'\n                    </div>')
        out.write(u'\n                    ')
        if not (not (this.getState() == 'paused')):
            out.write(u'<div class="paused">\n                        <span>')
            out.write(escape(this.getPausedString()))
            out.write(u'</span>\n                    </div>')
        out.write(u'\n                    ')
        if not (this.getState() == 'paused'):
            out.write(u'<a title="Pause Download" href="#" class="main-progress-pause" onclick="return eventURL(\'action:pauseDownload?item=')
            out.write(quoteattr(urlencode(this.getID())))
            out.write(u'\');"></a>')
        out.write(u'\n                    ')
        if not (not (this.getState() == 'paused')):
            out.write(u'<a href="#" class="main-progress-resume" onclick="return eventURL(\'action:resumeDownload?item=')
            out.write(quoteattr(urlencode(this.getID())))
            out.write(u'\');" title="Pause Download"></a>')
        out.write(u'\n                    <a href="#" class="main-progress-cancel" onclick="return eventURL(\'action:expireItem?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');" title="Cancel Download"></a>\n                </div>')
    out.write(u'\n            </div><!-- HOT SPOT END -->\n            <div class="download-status-strings">\n                ')
    if not (not (this.getExpiring())):
        out.write(u'<div class="main-video-details-expiring">\n                    <span>')
        out.write(escape(this.getExpirationString()))
        out.write(u'</span>\n                </div>')
    out.write(u'\n                ')
    if not (not (this.isPendingAutoDownload())):
        out.write(u'<div class="main-video-details-pending-auto">\n                    <span>')
        out.write(_(u'Pending Auto Download'))
        out.write(u'</span>\n                </div>')
    out.write(u'\n                ')
    if not (not (this.isFailedDownload() and not this.isPendingManualDownload())):
        out.write(u'<div class="main-video-details-failed-download">\n                    <span>')
        out.write(escape(this.getFailureReason()))
        out.write(u'</span>\n                </div>')
    out.write(u'\n            </div>\n            ')
    if not (this.getEmblemCSSString() == ''):
        out.write(u'<div class="video-state ')
        out.write(quoteattr(this.getEmblemCSSClass()))
        out.write(u'">\n                <div class="video-state-left">\n                    <div class="video-state-right">\n                        <span class="video-state-mid">\n                            <span>')
        out.write(escape(this.getEmblemCSSString()))
        out.write(u'</span>\n                        </span>\n                    </div>\n                </div>\n            </div>')
    out.write(u'\n            ')
    if not (not (this.downloader and this.downloader.getState() == 'uploading')):
        out.write(u'<div>\n                 <a href="#" class="round-button-left stop-seeding" onclick="return eventURL(\'action:stopUploadItem?item=')
        out.write(quoteattr(urlencode(this.getID())))
        out.write(u'\');">\n                <div class="round-button-right">\n                <div class="round-button-content">\n                    <span>')
        out.write(_(u'STOP SEEDING'))
        out.write(u'</span>\n                </div>\n                </div>\n                </a>\n            </div>')
    out.write(u'\n        </div>\n        ')
    if not (not (this.showMoreInfo)):
        out.write(u'<div class="more-info-details">\n            <div>')
        out.write(this.getMoreInfo())
        out.write(u'</div>\n        </div>')
    out.write(u'\n    </div>\n')
    out.write(u'\n        ')
    out.write(u'\n    <div class="main-video-desc noselect">\n        <h1 class="noselect">')
    out.write(escape(this.getTitle()))
    out.write(u'</h1>\n        <div class="main-video-desc-desc noselect">\n            <span>')
    out.write(this.getDescription())
    out.write(u'</span>\n        </div>\n        <div class="main-video-bottom">\n                <div class="channel-title">\n                        <span>')
    out.write(escape(this.getChannelTitle()))
    out.write(u'</span>\n                </div>\n                <div class="donate-html noselect">\n                    <span>')
    out.write(this.getPaymentHTML())
    out.write(u'</span>\n                </div>\n        </div>\n    </div>\n')
    out.write(u'\n        <div class="clear"></div>\n    </body>\n</html>')
    out.seek(0)


    return (out, handle)
