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
    global feed, showDownloads, showWatchableItems, showNewItems, allItemsMode, allItems, watchableItems, matchingItems, newItems, itemSort, itemSortWatchable, itemSortDownloading, notDeleted
    
    def _setFeed(kargs):
        global feed, allItemsMode, showDownloads, showNewItems, showWatchableItems
    
        # The main section
        allItemsMode = False
        
        # Initial states of views in this template
        showDownloads = False
        showNewItems = True
        showWatchableItems = True
    
        feed = views.feeds.getObjectByID(int(kargs['id']))
        filters.switchNewItemsChannel(feed)
        sorts.switchUnwatchedFirstChannel(feed)
    
    def _updateView ():
        global showNewItems, allItemsMode
    
        showNewItems = (len(watchableItems) == 0) or (len(newItems) > 0 and feed.getAutoDownloadMode() == 'off') or feed.getURL().startswith('dtv:directoryfeed')
    
        if len(newItems) == 0 or not showNewItems:
            allItemsMode = True
            matchingItems.recomputeFilter(newItems)
    
        feed.updateIcons()
    
    def reInit(*args, **kargs):
        global feed, allItems, showDownloads, showWatchableItems, showNewItems, allItemsMode, watchableItems, matchingItems, newItems, itemSort, itemSortWatchable, itemSortDownloading
    
        if feed.idExists():
            feed.markAsViewed()
    
        #print "reinitting %s" % repr(kargs)
        _setFeed(kargs)
        itemSort = feed.itemSort
        itemSortDownloading = feed.itemSortDownloading
        itemSortWatchable = feed.itemSortWatchable
        newItems.sortFunc = feed.itemSort.sort
        downloadingItems.sortFunc = feed.itemSortDownloading.sort
        watchableItems.sortFunc = feed.itemSortWatchable.sort
    
        allItems.changeIndexValue(indexes.itemsByFeed, int(kargs['id']))
        views.feeds.recomputeFilter(thisFeedView)
    
        _updateView()
    
    def showDownloadsFilter(x):
        return showDownloads
    
    def showWatchableFilter(x):
        return showWatchableItems
    
    def showNewFilter(x):
        isNew = filters.newItems(x)
        # need to make call newItems() so that the filter remembers if the item
        # was flagged as new or not.
        return showNewItems and (allItemsMode or isNew)
    
    def updateSearchString(newSearch):
        global feed
        if len(newSearch) == 0:
            feed.setInlineSearchTerm(None)
        else:
            feed.setInlineSearchTerm(newSearch)
        allItems.recomputeFilters()
    
    def toggleDownloadsView(handle):
        global showDownloads
        showDownloads = not showDownloads
        allDownloadingItems.recomputeFilter(downloadingItems)
        handle.forceUpdate()
    
    def toggleWatchableView(handle):
        global showWatchableItems
        showWatchableItems = not showWatchableItems
        allWatchableItems.recomputeFilter(watchableItems)
        handle.forceUpdate()
    
    def toggleNewItemsView(handle):
        global showNewItems
        showNewItems = not showNewItems
        matchingItems.recomputeFilter(newItems)
        handle.forceUpdate()
    
    def toggleAllItemsMode(handle):
        global allItemsMode
        allItemsMode = not allItemsMode
        matchingItems.recomputeFilter(newItems)
        handle.forceUpdate()
    
    def setSortBy(by, which, handle):
        if which == 'main':
            feed.itemSort.setSortBy(by)
            matchingItems.recomputeSort(newItems)
        elif which == 'downloading':
            feed.itemSortDownloading.setSortBy(by)
            allDownloadingItems.recomputeSort(downloadingItems)
        else:
            feed.itemSortWatchable.setSortBy(by)
            allWatchableItems.recomputeSort(watchableItems)
        handle.forceUpdate()
    
    _setFeed(kargs)
    
    allItems = views.items.filterWithIndex(indexes.itemsByFeed, feed.getID())
    notDeleted = allItems.filter(filters.notDeleted)
    matchingItems = notDeleted.filter(lambda x: filters.matchingItems(x, feed.inlineSearchTerm))
    newItems = matchingItems.filter(showNewFilter, sortFunc=feed.itemSort.sort, resort=True)
    
    allDownloadingItems = matchingItems.filter(filters.downloadingOrPausedItems)
    downloadingItems = allDownloadingItems.filter(showDownloadsFilter,sortFunc=feed.itemSortDownloading.sort,resort=True)
    allWatchableItems = matchingItems.filter(filters.watchableItems)
    watchableItems = allWatchableItems.filter(showWatchableFilter,sortFunc=feed.itemSortWatchable.sort,resort=True)
    
    thisFeedView = views.feeds.filter(lambda x: x is feed)
    itemSort = feed.itemSort
    itemSortWatchable = feed.itemSortWatchable
    itemSortDownloading = feed.itemSortDownloading
    
    def allItemsHaveState(view, state):
        for item in view:
            if item.getState() != state:
                return False
        return True
    def allItemsPaused(view):
        return allItemsHaveState(view, 'paused')
    def allItemsDownloading(view):
        return allItemsHaveState(view, 'downloading')
    
    _updateView()
    
    isFolder = False
    
        

    def _execOnUnload():
        
        matchingItems.unlink()
        thisFeedView.unlink()
        notDeleted.unlink()
        allItems.unlink()
        if feed.idExists():
            feed.markAsViewed()
        
            
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle = Handle(domHandler, localvars, onUnlink = _execOnUnload)

    def up_0_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n    ')
        out.write(u'\n\n<form action="javascript:eventURL(\'template:channel?id=')
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
        tmplcomp48487852 = {}
        tmplcomp57087858 = StringIO()
        tmplcomp57087858.write(u'<span>')
        tmplcomp57087858.write(escape(feed.getTitle()))
        tmplcomp57087858.write(u'</span>')
        tmplcomp57087858.seek(0)
        tmplcomp48487852['title'] = tmplcomp57087858.read()
        out.write(Template(_(u'Settings for ${title}')).substitute(tmplcomp48487852))
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
        tmplcomp74349669 = {}
        tmplcomp32516708 = StringIO()
        if not (feed.getMaxNew() == 'unlimited'):
            tmplcomp32516708.write(u'<input onBlur="javascript:setMaxNew();" name="maxNew" value="')
            tmplcomp32516708.write(quoteattr(urlencode(feed.getMaxNew())))
            tmplcomp32516708.write(u'" type="text" size="3"></input>')
        tmplcomp32516708.seek(0)
        tmplcomp74349669['maxnew2'] = tmplcomp32516708.read()
        tmplcomp95333484 = StringIO()
        if not (feed.getMaxNew() != 'unlimited'):
            tmplcomp95333484.write(u'<input onBlur="javascript:setMaxNew();" name="maxNew" value="3" disabled="1" type="text" size="3"></input>')
        tmplcomp95333484.seek(0)
        tmplcomp74349669['maxnew'] = tmplcomp95333484.read()
        out.write(Template(_(u"Don't Auto Download when more than ${maxnew} ${maxnew2} videos are waiting unwatched.")).substitute(tmplcomp74349669))
        out.write(u'</span><div class="settings-small">')
        out.write(_(u'Prevents this channel from using unlimited disk space.'))
        out.write(u'</div>\n\n\t    <div class="gray-button-wrap settings-button">\n\t\t    <div id="feed-settings-close-button" onclick="return hideSettings()" class="gray-button-bg">\n                <div class="gray-button-left"></div>\n                <div class="gray-button-right"></div>\n                <div class="gray-button-content" i18:translate="">Done</div>\n            </div>\n\t</div>\n \t</div>         \n</div>\n\n\n</form>\n\n')
        out.write(u'\n  </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp55637128','nextSibling',thisFeedView,up_0_handle, u'thisFeedView')
    def up_1_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n            <div>\n                <img src="')
        out.write(quoteattr(feed.getThumbnail()))
        out.write(u'" alt="" id="main-icon"></img>\n\t    </div>\n            ')
        if not (feed.getURL().startswith('dtv:directoryfeed')):
            out.write(u'<div class="main-titlebar-right">\n                <ul>\n                    ')
            if not (feed.getLink() == ''):
                out.write(u'<li>\n                        <a href="')
                out.write(quoteattr(feed.getLink()))
                out.write(u'" class="round-button-left black">\n                        <div class="round-button-right black">\n                        <div class="round-button-content black">\n                        <span>')
                out.write(_(u'VISIT WEBSITE'))
                out.write(u'</span>\n                        </div>\n                        </div>\n                        </a>\n                    </li>')
            out.write(u'\n                    <li>\n                        <a href="#" class="round-button-left black" onclick="return recommendChannel(\'')
            out.write(quoteattr(urlencode(feed.getTitle())))
            out.write(u"', '")
            out.write(quoteattr(urlencode(feed.getURL())))
            out.write(u'\');">\n                        <div class="round-button-right black">\n                        <div class="round-button-content black">\n                        <span>')
            out.write(_(u'SEND TO FRIEND'))
            out.write(u'</span>\n                        </div>\n                        </div>\n                        </a>\n                    </li>\n                    <li>\n                        <a href="#" class="round-button-left black" onclick="return showSettings();">\n                        <div class="round-button-right black">\n                        <div class="round-button-content black">\n                        <span>')
            out.write(_(u'SETTINGS'))
            out.write(u'</span>\n                        </div>\n                        </div>\n                        </a>\n                    </li>\n                </ul>\n\t    </div>')
        out.write(u'\n        </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp74028976','nextSibling',thisFeedView,up_1_handle, u'thisFeedView')
    def up_2_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n            <h1 id="main-title">')
        out.write(escape(feed.getTitle()))
        out.write(u'</h1>\n            <div id="auto-download">\n                ')
        if not (feed.getURL().startswith('dtv:directoryfeed')):
            out.write(u'<div>\n                    <div class="auto-download">\n                        <span id="auto-label">')
            out.write(_(u'AUTO DOWNLOAD'))
            out.write(u'</span>\n                        <div class="select-box-left" onclick="showSelectBoxMenu(\'auto-download-menu\');">\n                        <div class="select-box-right">\n                        ')
            if not (feed is None):
                out.write(u'<div class="select-box-mid">\n                            <span>')
                out.write(escape(feed.getAutoDownloadMode()))
                out.write(u'</span>\n                        </div>')
            out.write(u'\n                        </div>\n                        </div>\n                        \n                        <br clear="all"></br>\n                        ')
            if not (feed is None):
                out.write(u'<ul id="auto-download-menu" class="select-box-menu">\n                            <li onclick="return eventURL(\'action:setAutoDownloadMode?mode=all&feed=')
                out.write(quoteattr(urlencode(feed.getID())))
                out.write(u'\');"><a href="#"><strong>ALL</strong> - Get all videos</a></li>\n                            <li onclick="return eventURL(\'action:setAutoDownloadMode?mode=new&feed=')
                out.write(quoteattr(urlencode(feed.getID())))
                out.write(u'\');"><a href="#"><strong>NEW</strong> - Get only new videos</a></li>\n                            <li onclick="return eventURL(\'action:setAutoDownloadMode?mode=off&feed=')
                out.write(quoteattr(urlencode(feed.getID())))
                out.write(u'\');"><a href="#"><strong>OFF</strong> - Don\'t auto-download videos</a></li>\n                        </ul>')
            out.write(u'\n                    </div>\n                </div>')
        out.write(u'\n            </div>\n            ')
        if not ('feed' in localvars and feed.getURL() == 'dtv:search'):
            out.write(u'<div id="search-box-container">\n                ')
            if not (not (feed.inlineSearchTerm is None)):
                out.write(u'<div>\n                    <input value="')
                out.write(quoteattr(_('Find')))
                out.write(u'" onfocus="onSearchFocus(this)" type="search" id="search-box" onblur="endEditSearch()"></input>\n                </div>')
            out.write(u'\n                ')
            if not (not (feed.inlineSearchTerm is not None)):
                out.write(u'<div>\n                    <input onblur="endEditSearch()" searching="1" value="')
                out.write(quoteattr(feed.inlineSearchTerm))
                out.write(u'" onfocus="onSearchFocus(this)" type="search" id="search-box"></input>\n                </div>')
            out.write(u'\n            </div>')
        out.write(u'\n            </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp04429067','nextSibling',thisFeedView,up_2_handle, u'thisFeedView')
    def up_3_handle(viewName, view, tid):
        out = StringIO()
        out.write(u'<div id="')
        out.write(quoteattr(tid))
        out.write(u'">\n            ')
        if not (feed.inlineSearchTerm is None or feed.getURL().startswith('dtv:directoryfeed')):
            out.write(u'<div>\n                <div class="white-button-left save-search-channel">\n                <div class="white-button-right">\n                <div class="white-button-middle">\n                    <a href="#" onclick="return eventURL(\'action:addChannelSearchFeed?id=')
            out.write(quoteattr(urlencode(feed.getID())))
            out.write(u'\');">Save Search</a>\n                </div>\n                </div>\n                </div>\n            </div>')
        out.write(u'\n            </div>')
        out.seek(0)
        return out
    handle.addUpdate('tmplcomp62294993','nextSibling',matchingItems,up_3_handle, u'matchingItems')
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

    def up_0_handle_1(viewName, view, tid):
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
    handle_1.addUpdate('tmplcomp04348157','nextSibling',allDownloadingItems,up_0_handle_1, u'allDownloadingItems')
    def up_1_handle_1(viewName, view, tid):
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
    handle_1.addUpdate('tmplcomp14706281','nextSibling',downloadingItems,up_1_handle_1, u'downloadingItems')
    def up_2_handle_1(viewName, view, tid):
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
    handle_1.addUpdate('tmplcomp28734491','nextSibling',matchingItems,up_2_handle_1, u'matchingItems')
    def up_3_handle_1(viewName, view, tid):
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
    handle_1.addUpdate('tmplcomp31362927','nextSibling',matchingItems,up_3_handle_1, u'matchingItems')
    def up_4_handle_1(viewName, view, tid):
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
    handle_1.addUpdate('tmplcomp17952954','nextSibling',matchingItems,up_4_handle_1, u'matchingItems')
    def up_5_handle_1(viewName, view, tid):
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
            tmplcomp14189685 = {}
            tmplcomp65728528 = StringIO()
            tmplcomp65728528.write(u'<span>')
            tmplcomp65728528.write(escape(allWatchableItems.len()))
            tmplcomp65728528.write(u'</span>')
            tmplcomp65728528.seek(0)
            tmplcomp14189685['len'] = tmplcomp65728528.read()
            out.write(Template(_(u'${len} Downloaded')).substitute(tmplcomp14189685))
            out.write(u'</span>\n        </a>')
        out.write(u'\n    </div>')
        out.seek(0)
        return out
    handle_1.addUpdate('tmplcomp20770459','nextSibling',allWatchableItems,up_5_handle_1, u'allWatchableItems')
    def up_6_handle_1(viewName, view, tid):
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
    handle_1.addUpdate('tmplcomp18195195','nextSibling',watchableItems,up_6_handle_1, u'watchableItems')
    def rep_7_handle_1(this, viewName, view, tid):
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
    handle_1.addView('tmplcomp78200394','containerDiv',downloadingItems,rep_7_handle_1, u'downloadingItems')
    def rep_8_handle_1(this, viewName, view, tid):
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
    handle_1.addView('tmplcomp58784493','containerDiv',newItems,rep_8_handle_1, u'newItems')
    def rep_9_handle_1(this, viewName, view, tid):
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
    handle_1.addView('tmplcomp64243592','containerDiv',watchableItems,rep_9_handle_1, u'watchableItems')
    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_1_0 = Handle(domHandler, localvars, onUnlink = lambda:None)

    handle_1.addSubHandle(handle_1_0)
    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_1_1 = Handle(domHandler, localvars, onUnlink = lambda:None)

    handle_1.addSubHandle(handle_1_1)
    # Start of handle

    # Start user code
    # End user code

    localvars = locals()
    localvars.update(globals())
    handle_1_2 = Handle(domHandler, localvars, onUnlink = lambda:None)

    handle_1.addSubHandle(handle_1_2)
    handle.addSubHandle(handle_1)


    out = StringIO()
    out.write(u"<?xml version=\"1.0\" encoding=\"utf-8\"?>\n<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Strict//EN\" \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd\">\n")
    out.write(u'<html dtvPlatform="')
    out.write(quoteattr(urlencode(dtvPlatform)))
    out.write(u'" eventCookie="')
    out.write(quoteattr(urlencode(eventCookie)))
    out.write(u'" xmlns="http://www.w3.org/1999/xhtml">\n\n<head>\n    <base href="')
    out.write(quoteattr(feed.getBaseHref()))
    out.write(u'"></base>\n    <meta content="text/html; charset=utf-8" http-equiv="Content-Type"></meta>\n    <title>Miro Channel View</title>\n\n    <link href="')
    out.write(quoteattr(resources.url(u'css/main.css')))
    out.write(u'" type="text/css" rel="stylesheet"></link>\n    <script type="text/javascript">\n<!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n///////////////////////////////////////////////////////////////////////////////\n//// For use on your page                                                  ////\n///////////////////////////////////////////////////////////////////////////////\n\nfunction getDTVPlatform() {\n    var elt = document.getElementsByTagName("html")[0];\n    return elt.getAttribute(\'dtvPlatform\');\n}\n\nfunction loadURL(url) {\n    try {\n        document.location.href = url;\n    } catch (e) {\n        // This may happen if the backend decides to handle the url load\n        // itself.\n    }\n}\n\n// For calling from page Javascript: Cause a URL to be loaded. The\n// assumption is that the application will notice, abort the load, and\n// take some action based on the URL.\nfunction eventURL(url) {\n    if (typeof(window.frontend) == \'undefined\') {\n\t// Generic strategy: trigger a load, and hope the application\n\t// catches it and cancels it without creating a race\n\t// condition.\n        loadURL(url)\n    } else {\n\t// OS X WebKit (KHTML) strategy: pass in an Objective C object\n\t// through the window object and call a method on it.\n\twindow.frontend.eventURL(url);\n    }\n\n    return false;\n}\n\n// Calls eventURL, then calls event.stopPropagation() and\n// event.preventDefault() so that the event chain is stopped.\nfunction eventURLAndStop(url, event) {\n  eventURL(url);\n  event.stopPropagation();\n  event.preventDefault();\n}\n\nfunction recommendItem(title, url) {\n    loadURL(\'http://www.videobomb.com/index/democracyemail?url=\' + \n            url + \'&title=\' + title);\n    return false;\n}\n\nfunction recommendChannel(title, url) {\n    // See also app.py if changing this URL\n    loadURL(\'http://www.videobomb.com/democracy_channel/email_friend\' +\n        \'?url=\' + url + \'&title=\' + title);\n    return false;\n}\n\n// Start the video player. The playlist will be the items in the view\n// named by viewName. If firstItemId is the id of an item in the view,\n// playback will start on that item; otherwise playback will start on\n// the first item.\nfunction playViewNamed(viewName, firstItemId) {\n    url = \'action:playViewNamed?\';\n    url = url + \'viewName=\' + URLencode(viewName);\n    url = url + \'&firstItemId=\' + URLencode(firstItemId);\n    eventURL(url);\n    return false;\n}\n\n// You can make \'incremental search\' text boxes on your page that\n// effectively tie the text box to the \'parameter\' argument of setViewFilter,\n// with the other argumens fixed. To do this, add these two attributes to\n// the text box:\n//   onfocus="startEditSearch(this)"\n//   onblur="endEditFilter()"\n// replacing the arguments in parentheses with the desired strings.\n//\n// You\'ll also need to provide a updateSearchString function at the\n// top of your template to perform the actual update\n\nvar editSearchField = null;\nvar editSearchOldValue = \'\';\nvar editSearchTimer = null;\nvar editSearchCallback = null;\n\nfunction onSearchFocus(obj){\n  if (obj.getAttribute(\'searching\') != \'1\') {\n\tobj.value="";\n\tobj.searching = \'1\';\n  }\n  startEditSearch(obj, null);\n}\n\nfunction startEditSearch(obj, callback) {\n  editSearchOldValue = obj.value;\n\n  editSearchField = obj;\n  editSearchCallback = callback;\n  editSearchTimerTick();\n}\n\nfunction editSearchUpdate() {\n    value = editSearchField.value;\n    if (editSearchOldValue != value) {\n\turl = \'action:setSearchString?searchString=\' + URLencode(value);\n\teventURL(url);\n\teditSearchOldValue = value;\n\tif(editSearchCallback) editSearchCallback();\n    }\n}\n\nfunction editSearchTimerTick() {\n    editSearchUpdate();\n    editSearchTimer = setTimeout(editSearchTimerTick, 50);\n}\n\nfunction endEditSearch() {\n  clearTimeout(editSearchTimer);\n  editSearchUpdate();\n}\n\n// Internal use: \'URL encode\' the given string.\nfunction URLencode(str) {\n    return encodeURIComponent(str)\n}\n\nfunction URLdecode(str) {\n  return decodeURIComponent(str)\n}\n\nvar currentSelectBoxMenu = null;\nfunction showSelectBoxMenu(id) {\n    document.getElementById(id).style.display = \'block\';\n    currentSelectBoxMenu = id;\n    document.addEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\nfunction hideSelectBoxMenu(event) {\n    document.getElementById(currentSelectBoxMenu).style.display = \'\';\n    currentSelectBoxMenu = null;\n    document.removeEventListener(\'click\', hideSelectBoxMenu, true)\n}\n\n///////////////////////////////////////////////////////////////////////////////\n//// For calling by host templating code                                   ////\n///////////////////////////////////////////////////////////////////////////////\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it disappear.\nfunction hideItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'none\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Set CSS styles on the item\n// with the given ID to make it visible if it was previously hidden.\nfunction showItem(id) {\n    elt = document.getElementById(id);\n    elt.style.display = \'\';\n    forceRedisplay(elt);\n}\n\n// For calling by host templating code: Replace the item with the\n// given id with the element described by the proided XML.\nfunction changeItem(id, newXML) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.replaceChild(frag, elt);\n}\n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element immediately before the item\n// with the given id, such that the newly inserted item has the same\n// parent.\nfunction addItemBefore(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.parentNode.insertBefore(frag, elt);\n}    \n\n// For calling by host templating code: Parse the XML in newXML into a\n// new element, and insert the new element as the final child of the\n// item with the given id.\nfunction addItemAtEnd(newXML, id) {\n    elt = document.getElementById(id);\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.createContextualFragment(newXML);\n    elt.insertBefore(frag, null);\n}    \n\n// For calling by host templating code: Remove the item with the given\n// id.\nfunction removeItem(id) {\n    elt = document.getElementById(id);\n    elt.parentNode.removeChild(elt);\n}    \n\n// Internal use: Sometime if all you do is change the style on a node,\n// Safari doesn\'t update the view until your mouse is next over the\n// window. Force the issue by making a drastic change in the vicinity\n// of the given element and then reversing it.\nfunction forceRedisplay(elt) {\n    r = document.createRange();\n    r.selectNode(elt);\n    frag = r.extractContents();\n    r.insertNode(frag);\n}\n\nfunction handleContextMenuSelect(event) {\n  if(event.button == 2) {\n    var area = event.currentTarget.getAttribute("selectArea");\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var url = \'action:handleContextMenuSelect?id=\' + id + \'&area=\' + area +\n              \'&viewName=\' + viewName;\n    eventURL(url);\n  }\n  return true;\n}\n\nfunction handleSelect(event) {\n   if(event.target.tagName && event.target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n    }\n    var id = event.currentTarget.getAttribute("selectID");\n    var viewName = event.currentTarget.getAttribute("selectViewName");\n    var area = event.currentTarget.getAttribute("selectArea");\n    var shiftKey = \'0\';\n    var ctrlKey = \'0\';\n    if(event.shiftKey) shiftKey = \'1\';\n    if(event.ctrlKey || event.metaKey) ctrlKey = \'1\';\n    eventURL(\'action:handleSelect?area=\' + area + \'&viewName=\' + viewName + \n\t\'&id=\' + id + \'&shiftDown=\' + shiftKey + \'&ctrlDown=\' + ctrlKey);\n    return true;\n}\n\nfunction handleDblClick(event, viewName, id) {\n   var target = event.target;\n   while (target != undefined && target.ondblclick === null && target.tagName.toUpperCase() != \'A\') {\n       target = target.parentNode;\n   }\n\n   if(target.tagName.toUpperCase() == \'A\') {\n       // Either a link in the descrption, or a bomb/mailto/trash click\n       return true;\n   } else {\n       return eventURL(\'action:playViewNamed?viewName=\' + viewName + \n           \'&firstItemId=\' + id);\n   }\n}\n\nfunction getKeyFromEvent(evt) {\n  var key = 0;\n  if (window.event)  {\n    key = evt.keyCode;\n  } else if (evt.which) {\n  \tkey = evt.which;\n  }\n\n  return key;\n}\n\nfunction sendKeyToSearchBox(event) {\n  if(event.altKey || event.ctrlKey || event.metaKey ||\n      (event.target.tagName && event.target.tagName.toUpperCase() == \'INPUT\'))\n      return true;\n  var key = getKeyFromEvent(event);\n  if ((key == 33) || (key == 34) || (key == 35) || (key == 36) || \n      (key == 37) || (key == 38) || (key == 39) || (key == 40))\n      return true;\n  var searchBox = document.getElementById("search-box");\n  searchBox.focus();\n  return true;\n}\n\nfunction playNewVideos(event, id) {\n  eventURL(\'action:playNewVideos?id=\' + id);\n  event.stopPropagation(); // don\'t want handleSelect to deal with this event\n  return false;\n}\n\n///////////////////////////////////////////////////////////////////////////////\n///////////////////////////////////////////////////////////////////////////////\n\n-->\n</script>\n\n    <script type="text/javascript">\n    <!-- // Protect from our XML parser, which doesn\'t know to protect <script>\n\n    var settingsMode = \'closed\';\n\n    function showSettings()\n    {\n        if(settingsMode == \'open\') return hideSettings();\n        var feedSettings = document.getElementById("feed-settings");\n        feedSettings.style.display = "block";\n        settingsMode = \'open\';\n        return false;\n    }\n\n    function hideSettings()\n    {\n        var feedSettings = document.getElementById("feed-settings");\n        feedSettings.style.display = "none";\n        settingsMode = \'closed\';\n        return false;\n    }\n\n    function setExpiration()\n    {\n        var url = "action:setExpiration";\n        var idx = document.forms[\'settings\'][\'expireAfter\'].selectedIndex;\n        var value = document.forms[\'settings\'][\'expireAfter\'].options[idx].value;\n\n        url += \'?feed=\' + document.forms[\'settings\'][\'feed\'].value;\n        if (value == \'system\' || value == \'never\')\n        {\n            url += "&type=" + value + "&time=0";\n        }\n        else\n        {\n            url += "&type=feed&time=" + value;\n        }\n\n        eventURL(url);\n    }\n\n    function setMaxNew()\n    {\n        var url = "action:setMaxNew";\n\n        url += \'?feed=\' + document.forms[\'settings\'][\'feed\'].value;\n        if (document.forms[\'settings\'][\'maxOutDownloads\'].checked)\n        {\n            var maxNew = document.forms[\'settings\'][\'maxNew\'];\n            maxNew.disabled = false;\n            if(maxNew.value == \'\') maxNew.value = \'0\';\n            if(!(parseInt(maxNew.value) >= 0)) {\n               eventURL(\'action:invalidMaxNew?value=\' + escape(maxNew.value));\n               maxNew.value = \'0\';\n            }\n            url += \'&maxNew=\' + maxNew.value;\n        }\n        else\n        {\n            document.forms[\'settings\'][\'maxNew\'].disabled = true;\n            url += \'&maxNew=-1\';\n        }\n\n        eventURL(url);\n    }\n\n    -->\n</script>\n\n    <script src="')
    out.write(quoteattr(resources.url(u'templates/osxdnd.js')))
    out.write(u'" type="text/javascript"></script>\n    \n    \n\n</head>\n\n<body onkeydown="sendKeyToSearchBox(event);"')
    out.write(u" " + bodyTagExtra)
    out.write(u'>\n<div id="feed-settings">\n  ')
    out.write(u'<span id="tmplcomp55637128"/>\n</div>\n    \n\n\n<div id="main-titlebar">\n        ')
    out.write(u'<span id="tmplcomp74028976"/>\n\n        <div class="main-titlebar-left">\n            ')
    out.write(u'<span id="tmplcomp04429067"/>\n            ')
    out.write(u'<span id="tmplcomp62294993"/>\n        </div>\n</div>\n\n\n\n<div id="main-container">\n    <div t:showIf=')
    out.write(quoteAndFillAttr(u'feed.isScraped() and feed.isUpdating()',locals()))
    out.write(u' class=')
    out.write(quoteAndFillAttr(u'main-container-scraping',locals()))
    out.write(u' id="tmplcomp44240158"')
    _hideFunc = lambda : not (feed.isScraped() and feed.isUpdating())
    _dynHide = _hideFunc()
    if _dynHide:
        out.write(u" style=\"display:none\">")
    else:
        out.write(u">")
    handle.addUpdateHideOnView('tmplcomp44240158',thisFeedView,_hideFunc,_dynHide)
    out.write(u'\n    <div class="scraping-indicator">\n      <img src="')
    out.write(quoteattr(resources.url(u'images/scraping-indicator-left.gif')))
    out.write(u'" align="left"></img>\n      <img src="')
    out.write(quoteattr(resources.url(u'images/scraping-indicator-right.gif')))
    out.write(u'" align="right"></img>\n      <div class="scraping-content">')
    out.write(_(u'Looking for videos at this URL'))
    out.write(u'</div>\n    </div>\n    </div>\n    <div class="hide-channel-title">\n        ')
    out.write(u'\n\n')
    out.write(u'<span id="tmplcomp04348157"/>\n\n    ')
    out.write(u'<span id="tmplcomp14706281"/>\n    <div id="tmplcomp78200394">')
    out.write(u'</div>\n\n\n\n\n\n<div class="available-channelbar-wrap">\n    ')
    out.write(u'<span id="tmplcomp28734491"/>\n</div>\n\n')
    out.write(u'<span id="tmplcomp31362927"/>\n\n<div id="tmplcomp58784493">')
    out.write(u'</div>\n\n\n')
    out.write(u'<span id="tmplcomp17952954"/>\n\n\n\n\n<div id="tmplcomp95020927"')
    _hideFunc = lambda : not isFolder and feed.getURL().startswith('dtv:directoryfeed')
    _dynHide = _hideFunc()
    if _dynHide:
        out.write(u" style=\"display:none\">")
    else:
        out.write(u">")
    handle.addUpdateHideOnView('tmplcomp95020927',thisFeedView,_hideFunc,_dynHide)
    out.write(u'\n    ')
    out.write(u'<span id="tmplcomp20770459"/>\n    \n    ')
    out.write(u'<span id="tmplcomp18195195"/>\n    <div id="tmplcomp64243592">')
    out.write(u'</div>\n</div>\n\n\n')
    out.write(u'\n    </div>\n</div>\n\n\n</body>\n</html>')
    out.seek(0)


    return (out, handle)
