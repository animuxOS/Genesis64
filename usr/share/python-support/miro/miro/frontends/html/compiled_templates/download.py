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
    
    from miro import config
    from miro import prefs
    from miro import util
    from miro import downloader
    from miro.gtcache import gettext as _
    from miro.platform.utils import getAvailableBytesForMovies
    
    def getFreeSpace():
        bytes = getAvailableBytesForMovies()
        return util.formatSizeForUser(bytes, "0B", False)
    
    def getAvailableSpace():
        bytes = getAvailableBytesForMovies()
        if config.get(prefs.PRESERVE_DISK_SPACE):
            preserved = config.get(prefs.PRESERVE_X_GB_FREE) * 1024 * 1024 * 1024
            bytes -= preserved
        return util.formatSizeForUser(bytes, "0B", False)
    
    def getUpRate():
        return _("%0.1f KB/s uploading") % (downloader.totalUpRate / 1024.0,)
    
    def getDownRate():
        return _("%0.1f KB/s downloading") % (downloader.totalDownRate / 1024.0,)
    
    global searchFilter
    searchFilter = lambda x: filters.matchingItems(x, None)
    
    def makeDownloadCategoryView(cat):
        return views.downloadingItems.filterWithIndex(indexes.downloadsByCategory, cat)
    allNormalDownloads = makeDownloadCategoryView('normal')
    allExternalDownloads = views.items.filter(lambda x: x.getFeed().url == 'dtv:manualFeed' and x.isNonVideoFile())
    # Specifically don't include anything in external downloads in uploads.
    allUploads = views.items.filter(lambda x: x.downloader and x.downloader.getState() == 'uploading' and not (x.getFeed().url == 'dtv:manualFeed' and x.isNonVideoFile()))
    allPendingDownloads = makeDownloadCategoryView('pending')
    allPausedDownloads = views.pausedItems.filter (lambda x: not (x.getFeed().url == 'dtv:manualFeed' and x.isNonVideoFile()))
    
    matchingNormalDLs = allNormalDownloads.filter(lambda x:searchFilter(x),sortFunc=sorts.itemSortDownloads.sort,resort=True)
    matchingExternalDLs = allExternalDownloads.filter(lambda x:searchFilter(x))
    matchingULs = allUploads.filter(lambda x:searchFilter(x),sortFunc=sorts.itemSortSeedingTorrents.sort,resort=True)
    matchingPendingDLs = allPendingDownloads.filter(lambda x:searchFilter(x),sortFunc=sorts.itemSortDownloads.sort,resort=True)
    matchingPausedDLs = allPausedDownloads.filter(lambda x:searchFilter(x),sortFunc=sorts.itemSortDownloads.sort,resort=True)
    
    def updateSearchString(newSearch):
        global searchFilter
        if len(newSearch) == 0:
            searchFilter = lambda x: filters.matchingItems(x, None)
        else:
            searchFilter = lambda x: filters.matchingItems(x, newSearch)
        allNormalDownloads.recomputeFilter(matchingNormalDLs)
        allExternalDownloads.recomputeFilter(matchingExternalDLs)
        allUploads.recomputeFilter(matchingULs)
        allPendingDownloads.recomputeFilter(matchingPendingDLs)
        allPausedDownloads.recomputeFilter(matchingPausedDLs)
    
    def setSortBy(by, which, handle):
        if which == 'main':
            sorts.itemSortDownloads.setSortBy(by)
            allNormalDownloads.recomputeSort(matchingNormalDLs)
            allPendingDownloads.recomputeSort(matchingPendingDLs)
            allPausedDownloads.recomputeSort(matchingPausedDLs)
        else:
            sorts.itemSortSeedingTorrents.setSortBy(by)
            allUploads.recomputeSort(matchingULs)
        handle.forceUpdate()
    
        

    def _execOnUnload():
        
        allNormalDownloads.unlink()
        allExternalDownloads.unlink()
        allUploads.unlink()
        allPendingDownloads.unlink()
        allPausedDownloads.unlink()
        
            
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle = Handle(domHandler, localvars, onUnlink = _execOnUnload)

    def up_0_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n                <ul class="download-rates">\n                    ')
        if not (not (downloader.totalDownRate > 1)):
            out.write(u'<li>\n                        <span>')
            out.write(escape(getDownRate()))
            out.write(u'</span>\n                    </li>')
        out.write(u'\n                    ')
        if not (not (downloader.totalUpRate > 1)):
            out.write(u'<li>\n                        <span>')
            out.write(escape(getUpRate()))
            out.write(u'</span>\n                    </li>')
        out.write(u'\n                </ul>\n            </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp01381396','nextSibling',views.remoteDownloads,up_0_handle, u'views.remoteDownloads')
    def up_1_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'"> \n        ')
        if not (matchingNormalDLs.len() + matchingPendingDLs.len() + matchingPausedDLs.len() == 0):
            out.write(u'<div>\n            ')
            out.write(fillStaticTemplate(u'static-tab-sort-bar', onlyBody=True, section='main', itemSort=sorts.itemSortDownloads))
            out.write(u'\n        </div>')
        out.write(u'\n    </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp12565290','nextSibling',views.downloadingItems,up_1_handle, u'views.downloadingItems')
    def up_2_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n        ')
        if not (matchingExternalDLs.len() == 0):
            out.write(u'<div>\n            <div class="main-channelbar downloading-channelbar no-arrow">\n                <span>')
            out.write(_(u'External Downloads'))
            out.write(u'</span>\n                <a title="Clear Completed and Failed Downloads" href="#" onclick="return eventURL(\'action:clearTorrents\');" class="clear-completed-link">')
            out.write(_(u'Clear Completed and Failed Downloads'))
            out.write(u'</a>\n            </div>\n        </div>')
        out.write(u'\n    </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp02815873','nextSibling',matchingExternalDLs,up_2_handle, u'matchingExternalDLs')
    def up_3_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n        ')
        if not (matchingULs.len() == 0):
            out.write(u'<div>\n            <div class="main-channelbar seeding-channelbar no-arrow">\n                <span>')
            out.write(_(u'Seeding Torrents'))
            out.write(u'</span>\n            </div>\n            ')
            out.write(fillStaticTemplate(u'static-tab-sort-bar', onlyBody=True, section='seeding-torrents', itemSort=sorts.itemSortSeedingTorrents))
            out.write(u'\n        </div>')
        out.write(u'\n    </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp96311059','nextSibling',matchingULs,up_3_handle, u'matchingULs')
    def config_up_4_handle(tid):
        out = StringIO()
        out.write(u'<span id="')
        out.write(quoteattr(tid))
        out.write(u'">\n                        ')
        if not (getFreeSpace() == getAvailableSpace()):
            out.write(u'<span>\n                            <span>')
            tmplcomp36971160 = {}
            tmplcomp05579656 = StringIO()
            tmplcomp05579656.write(u'<span>')
            tmplcomp05579656.write(escape(getAvailableSpace()))
            tmplcomp05579656.write(u'</span>')
            tmplcomp05579656.seek(0)
            tmplcomp36971160['size'] = tmplcomp05579656.read()
            out.write(Template(_(u'${size} free for downloads')).substitute(tmplcomp36971160))
            out.write(u'</span>\n                        </span>')
        out.write(u'\n                    </span>')
        out.seek(0)
        return out
    handle.addConfigUpdate('tmplcomp20805891','nextSibling',config_up_4_handle)
    def rep_5_handle(this, viewName, view, tid):
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
    handle.addView('tmplcomp31420032','containerDiv',matchingNormalDLs,rep_5_handle, u'matchingNormalDLs')
    def rep_6_handle(this, viewName, view, tid):
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
    handle.addView('tmplcomp99693165','containerDiv',matchingPendingDLs,rep_6_handle, u'matchingPendingDLs')
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
    handle.addView('tmplcomp52628197','containerDiv',matchingPausedDLs,rep_7_handle, u'matchingPausedDLs')
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
    handle.addView('tmplcomp14614348','containerDiv',matchingExternalDLs,rep_8_handle, u'matchingExternalDLs')
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
    handle.addView('tmplcomp28559900','containerDiv',matchingULs,rep_9_handle, u'matchingULs')
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


    out = StringIO()
    out.write(u"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n")
    out.write(u'<html dtvPlatform="')
    out.write(quoteattr(urlencode(dtvPlatform)))
    out.write(u'" eventCookie="')
    out.write(quoteattr(urlencode(eventCookie)))
    out.write(u'" xmlns="http://www.w3.org/1999/xhtml">\n<head>\n<meta content="text/html; charset=iso-8859-1" http-equiv="Content-Type"></meta>\n\n<link href="')
    out.write(quoteattr(resources.url(u'css/main.css')))
    out.write(u'" type="text/css" rel="stylesheet"></link>\n<link href="')
    out.write(quoteattr(resources.url(u'css/download.css')))
    out.write(u'" type="text/css" rel="stylesheet"></link>\n<script src="')
    out.write(quoteattr(resources.url(u'templates/osxdnd.js')))
    out.write(u'" type="text/javascript"></script>\n<script type="text/javascript">\n<!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n///////////////////////////////////////////////////////////////////////////////\n//// For use on your page                                                  ////\n///////////////////////////////////////////////////////////////////////////////\n\nfunction getDTVPlatform() {\n    var elt = document.getElementsByTagName("html")[0];\n    return elt.getAttribute(\'dtvPlatform\');\n}\n\nfunction loadURL(url) {\n    try {\n        document.location.href = url;\n    } catch (e) {\n        // This may happen if the backend decides to handle the url load\n        // itself.\n    }\n}\n\n// For calling from page Javascript: Cause a URL to be loaded. The\n// assumption is that the application will notice, abort the load, and\n// take some action based on the URL.\nfunction eventURL(url) {\n    if (typeof(window.frontend) == \'undefined\') {\n\t// Generic strategy: trigger a load, and hope the application\n\t// catches it and cancels it without creating a race\n\t// condition.\n        loadURL(url)\n    } else {\n\t// OS X WebKit (KHTML) strategy: pass in an Objective C object\n\t// through the window object and call a method on it.\n\twindow.frontend.eventURL(url);\n    }\n\n    return false;\n}\n\n// Calls eventURL, then calls event.stopPropagation() and\n// event.preventDefault() so that the event chain is stopped.\nfunction eventURLAndStop(url, event) {\n  eventURL(url);\n  event.stopPropagation();\n  event.preventDefault();\n}\n\nfunction recommendItem(title, url) {\n    loadURL(\'http://www.videobomb.com/index/democracyemail?url=\' + \n            url + \'&title=\' + title);\n    return false;\n}\n\nfunction recommendChannel(title, url) {\n    // See also app.py if changing this URL\n    loadURL(\'http://www.videobomb.com/democracy_channel/email_friend\' +\n        \'?url=\' + url + \'&title=\' + title);\n    return false;\n}\n\n// Start the video player. The playlist will be the items in the view\n// named by viewName. If firstItemId is the id of an item in the view,\n// playback will start on that item; otherwise playback will start on\n// the first item.\nfunction playViewNamed(viewName, firstItemId) {\n    url = \'action:playViewNamed?\';\n    url = url + \'viewName=\' + URLencode(viewName);\n    url = url + \'&firstItemId=\' + URLencode(firstItemId);\n    eventURL(url);\n    return false;\n}\n\n// You can make \'incremental search\' text boxes on your page that\n// effectively tie the text box to the \'parameter\' argument of setViewFilter,\n// with the other argumens fixed. To do this, add these two attributes to\n// the text box:\n//   onfocus="startEditSearch(this)"\n//   onblur="endEditFilter()"\n// replacing the arguments in parentheses with the desired strings.\n//\n// You\'ll also need to provide a updateSearchString function at the\n// top of your template to perform the actual update\n\nvar editSearchField = null;\nvar editSearchOldValue = \'\';\nvar editSearchTimer = null;\nvar editSearchCallback = null;\n\nfunction onSearchFocus(obj){\n  if (obj.getAttribute(\'searching\') != \'1\') {\n\tobj.value="";\n\tobj.searching = \'1\';\n  }\n  startEditSearch(obj, null);\n}\n\nfunction startEditSearch(obj, callback) {\n  editSearchOldValue = obj.value;\n\n  editSearchField = obj;\n  editSearchCallback = callback;\n  editSearchTimerTick();\n}\n\nfunction editSearchUpdate() {\n    value = editSearchField.value;\n    if (editSearchOldValue != value) {\n\turl = \'action:setSearchString?searchString=\' + URLencode(value);\n\teventURL(url);\n\teditSearchOldValue = value;\n\tif(editSearchCallback) editSearchCallback();\n    }\n}\n\nfunction editSearchTimerTick() {\n    editSearchUpdate();\n    editSearchTimer = setTimeout(editSearchTimerTick, 50);\n}\n\nfunction endEditSearch() {\n  clearTimeout(editSearchTimer);\n  editSearchUpdate();\n}\n\n// Internal use: \'URL encode\' the given string.\nfunction URLencode(str) {\n    return encodeURIComponent(str)\n}\n\nfunction URLdecode(str) {\n  return decodeURIComponent(str)\n}\n\nvar currentSelectBoxMenu = null;\nfunction showSelectBoxMenu(id) {\n    document.getElementById(id).style.display = \'block\';\n    currentSelectBoxMenu = id;\n    document.addEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\nfunction hideSelectBoxMenu(event) {\n    document.getElementById(currentSelectBoxMenu).style.display = \'\';\n    currentSelectBoxMenu = null;\n    document.removeEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\n///////////////////////////////////////////////////////////////////////////////\n//// For calling by host templating code                                   ////\n///////////////////////////////////////////////////////////////////////////////\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it disappear.\nfunction hideItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'none\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it visible if it was previously hidden.\nfunction showItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Replace the item with the\n// given id with the element described by the proided XML.\nfunction changeItem(id, newXML) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.replaceChild(frag, elt);\n}\n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element immediately before the item\n// with the given id, such that the newly inserted item has the same\n// parent.\nfunction addItemBefore(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.insertBefore(frag, elt);\n}    \n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element as the final child of the\n// item with the given id.\nfunction addItemAtEnd(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.insertBefore(frag, null);\n}    \n\n// For calling by host templating code: Remove the item with the given\n// id.\nfunction removeItem(id) {\n    elt = document.getElementById(id);\n    elt.parentNode.removeChild(elt);\n}    \n\n// Internal use: Sometime if all you do is change the style on a node,\n// Safari doesn\'t update the view until your mouse is next over the\n// window. Force the issue by making a drastic change in the vicinity\n// of the given element and then reversing it.\nfunction forceRedisplay(elt) {\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.extractContents();\n    r.insertNode(frag);\n}\n\nfunction handleContextMenuSelect(event) {\n  if(event.button == 2) {\n    var area = event.currentTarget.getAttribute("selectArea");\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var url = \'action:handleContextMenuSelect?id=\' + id + \'&area=\' + area +\n              \'&viewName=\' + viewName;\n    eventURL(url);\n  }\n  return true;\n}\n\nfunction handleSelect(event) {\n   if(event.target.tagName && event.target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n    }\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var area = event.currentTarget.getAttribute("selectArea");\n    var shiftKey = \'0\';\n    var ctrlKey = \'0\';\n    if(event.shiftKey) shiftKey = \'1\';\n    if(event.ctrlKey || event.metaKey) ctrlKey = \'1\';\n    eventURL(\'action:handleSelect?area=\' + area + \'&viewName=\' + viewName + \n\t\'&id=\' + id + \'&shiftDown=\' + shiftKey + \'&ctrlDown=\' + ctrlKey);\n    return true;\n}\n\nfunction handleDblClick(event, viewName, id) {\n   var target = event.target;\n   while (target != undefined && target.ondblclick === null && target.tagName.toUpperCase() != \'A\') {\n       target = target.parentNode;\n   }\n\n   if(target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n   } else {\n       return eventURL(\'action:playViewNamed?viewName=\' + viewName + \n           \'&firstItemId=\' + id);\n   }\n}\n\nfunction getKeyFromEvent(evt) {\n  var key = 0;\n  if (window.event)  {\n    key = evt.keyCode;\n  } else if (evt.which) {\n  \tkey = evt.which;\n  }\n\n  return key;\n}\n\nfunction sendKeyToSearchBox(event) {\n  if(event.altKey || event.ctrlKey || event.metaKey ||\n      (event.target.tagName && event.target.tagName.toUpperCase() == \'INPUT\'))\n      return true;\n  var key = getKeyFromEvent(event);\n  if ((key == 33) || (key == 34) || (key == 35) || (key == 36) || \n      (key == 37) || (key == 38) || (key == 39) || (key == 40))\n      return true;\n  var searchBox = document.getElementById("search-box");\n  searchBox.focus();\n  return true;\n}\n\nfunction playNewVideos(event, id) {\n  eventURL(\'action:playNewVideos?id=\' + id);\n  event.stopPropagation(); // don\'t want handleSelect to deal with this event\n  return false;\n}\n\n///////////////////////////////////////////////////////////////////////////////\n///////////////////////////////////////////////////////////////////////////////\n\n-->\n</script>\n\n<script type="text/javascript">\n    <!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n    var settingsMode = \'closed\';\n\n    function showSettings()\n    {\n        if(settingsMode == \'open\') return hideSettings();\n        var feedSettings = document.getElementById("feed-settings");\n        feedSettings.style.display = "block";\n        settingsMode = \'open\';\n        return false;\n    }\n\n    function hideSettings()\n    {\n        var feedSettings = document.getElementById("feed-settings");\n        feedSettings.style.display = "none";\n        settingsMode = \'closed\';\n        return false;\n    }\n\n    function setExpiration()\n    {\n        var url = "action:setExpiration";\n        var idx = document.forms[\'settings\'][\'expireAfter\'].selectedIndex;\n        var value = document.forms[\'settings\'][\'expireAfter\'].options[idx].value;\n\n        url += \'?feed=\' + document.forms[\'settings\'][\'feed\'].value;\n        if (value == \'system\' || value == \'never\')\n        {\n            url += "&type=" + value + "&time=0";\n        }\n        else\n        {\n            url += "&type=feed&time=" + value;\n        }\n\n        eventURL(url);\n    }\n\n    function setMaxNew()\n    {\n        var url = "action:setMaxNew";\n\n        url += \'?feed=\' + document.forms[\'settings\'][\'feed\'].value;\n        if (document.forms[\'settings\'][\'maxOutDownloads\'].checked)\n        {\n            var maxNew = document.forms[\'settings\'][\'maxNew\'];\n            maxNew.disabled = false;\n            if(maxNew.value == \'\') maxNew.value = \'0\';\n            if(!(parseInt(maxNew.value) >= 0)) {\n               eventURL(\'action:invalidMaxNew?value=\' + escape(maxNew.value));\n               maxNew.value = \'0\';\n            }\n            url += \'&maxNew=\' + maxNew.value;\n        }\n        else\n        {\n            document.forms[\'settings\'][\'maxNew\'].disabled = true;\n            url += \'&maxNew=-1\';\n        }\n\n        eventURL(url);\n    }\n\n    -->\n</script>\n\n\n    \n    \n</head>\n\n<body onkeydown="sendKeyToSearchBox(event);"')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n\n\n<div id="main-titlebar">\n\t<div id="main-icon" class="noborder"><img src="')
    out.write(quoteattr(resources.url(u'images/download-icon.png')))
    out.write(u'"></img></div>\n        <h1 id="main-title">')
    out.write(_(u'Downloading'))
    out.write(u'</h1>\n        <div id="search-box-container">\n            <input value="')
    out.write(quoteattr(_('Find')))
    out.write(u'" onfocus="onSearchFocus(this)" type="search" id="search-box" onblur="endEditSearch()"></input>\n        </div>\n        <div id="downloads-global-actions">\n            <div><p id="tmplcomp96555138"')
    _hideFunc = lambda : views.downloadingItems.len() == 0
    _dynHide = _hideFunc()
    if _dynHide:
        out.write(u" style=\"display:none\">")
    else:
        out.write(u">")
    handle.addUpdateHideOnView('tmplcomp96555138',views.downloadingItems,_hideFunc,_dynHide)
    out.write(u'<a href="#" onclick="return eventURL(\'action:pauseAll\');" title="Pause All"><img src="')
    out.write(quoteattr(resources.url(u'images/pause-all-downloads.png')))
    out.write(u'"></img><br></br><span>')
    out.write(_(u'Pause All'))
    out.write(u'</span></a></p>&nbsp;</div>\n            <div><p id="tmplcomp72567178"')
    _hideFunc = lambda : views.pausedItems.len() == 0
    _dynHide = _hideFunc()
    if _dynHide:
        out.write(u" style=\"display:none\">")
    else:
        out.write(u">")
    handle.addUpdateHideOnView('tmplcomp72567178',views.pausedItems,_hideFunc,_dynHide)
    out.write(u'<a href="#" onclick="return eventURL(\'action:resumeAll\');" title="Resume All"><img src="')
    out.write(quoteattr(resources.url(u'images/resume-all-downloads.png')))
    out.write(u'"></img><br></br><span>')
    out.write(_(u'Resume All'))
    out.write(u'</span></a></p>&nbsp;</div>\n        </div>\n\n        <div id="download-info">\n            <ul>\n                <li>\n                    <span>')
    tmplcomp53670630 = {}
    tmplcomp32225246 = StringIO()
    tmplcomp32225246.write(u'<span>')
    tmplcomp32225246.write(escape(getFreeSpace()))
    tmplcomp32225246.write(u'</span>')
    tmplcomp32225246.seek(0)
    tmplcomp53670630['size'] = tmplcomp32225246.read()
    out.write(Template(_(u'${size} free on disk')).substitute(tmplcomp53670630))
    out.write(u'</span>\n                </li>\n                <li>\n                    ')
    out.write(u'<span id="tmplcomp20805891"/>\n                </li>\n            </ul>\n            ')
    out.write(u'<span id="tmplcomp01381396"/>\n        </div>\n</div>\n\n\n<div id="main-container">\n        <div class=')
    out.write(quoteAndFillAttr(u'main-channelbar downloading-channelbar no-arrow',locals()))
    out.write(u' id="tmplcomp15738332"')
    _hideFunc = lambda : allNormalDownloads.len() == 0
    _dynHide = _hideFunc()
    if _dynHide:
        out.write(u" style=\"display:none\">")
    else:
        out.write(u">")
    handle.addUpdateHideOnView('tmplcomp15738332',allNormalDownloads,_hideFunc,_dynHide)
    out.write(u'\n                <span>')
    out.write(_(u'Channel Downloads'))
    out.write(u'</span>\n        </div>\n\n     \n    ')
    out.write(u'<span id="tmplcomp12565290"/> \n    \n\n\t\n    <div id="tmplcomp31420032">')
    out.write(u'</div>\n    <div id="tmplcomp99693165">')
    out.write(u'</div>\n    <div id="tmplcomp52628197">')
    out.write(u'</div>\n\t\n    ')
    out.write(u'<span id="tmplcomp02815873"/> \n    <div id="tmplcomp14614348">')
    out.write(u'</div>\n\n    ')
    out.write(u'<span id="tmplcomp96311059"/>\n    <div id="tmplcomp28559900">')
    out.write(u'</div>\n</div>\n\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
