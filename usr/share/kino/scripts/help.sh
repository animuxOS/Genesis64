#!/bin/sh
# A Kino script that opens a help viewer or web browser to a help page.

path="$1"
topic="$2"

# generate a full url to html page
url="${path}/${topic}.html"

# detect user agents
GNOME_BROWSER=`gconftool-2 --get /desktop/gnome/url-handlers/http/command | sed s/\"*%s\"*//`
which konqueror &> /dev/null
[ $? = 0 ] && KONQUEROR=konqueror
which firefox &> /dev/null
[ $? = 0 ] && FIREFOX=firefox
which mozilla &> /dev/null
[ $? = 0 ] && MOZILLA=mozilla
which yelp &> /dev/null
[ $? = 0 ] && YELP=yelp

# convert index to kino for docbook
[ "$topic" = "index" ] && id="kino" || id="$topic"

# invoke most appropriate user agent
( [ "$YELP" != '' ] && [ -n "$GNOME_DESKTOP_SESSION_ID" ] && $YELP "${path}/kino.xml#${id}" ) ||
( [ "$KONQUEROR" != '' ] && [ "$KDE_FULL_SESSION" = "true" ] && $KONQUEROR "$url" ) ||
( [ "$HELP_BROWSER" != '' ] && $HELP_BROWSER "$url" ) ||
( [ "$BROWSER" != '' ] && $BROWSER "$url" ) ||
( [ "$GNOME_BROWSER" != '' ] && $GNOME_BROWSER "$url" ) ||
( [ "$FIREFOX" != '' ] && $FIREFOX "$url" ) ||
( [ "$KONQUEROR" != '' ] && $KONQUEROR "$url" ) ||
( [ "$MOZILLA" != '' ] && $MOZILLA "$url" )
