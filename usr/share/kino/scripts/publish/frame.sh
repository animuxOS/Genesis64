#!/bin/sh
# A Kino script that publishes a frame.

frame_file="$1"
project_id="$2"
scene_title="$3"
project_title="$4"

if [ -n "$KINO_HOME" ] && [ -f "$KINO_HOME"/publish/frame.sh ]; then
	. "$KINO_HOME"/publish/frame.sh "$frame_file" "$project_id" "$scene_title" "$project_title"
elif [ -f "$HOME"/kino/publish/frame.sh ]; then
	. "$HOME"/kino/publish/frame.sh "$frame_file" "$project_id" "$scene_title" "$project_title"
else
	# detect terminal
	GNOME_TERM=`gconftool-2 --get /desktop/gnome/applications/terminal/exec`
	GNOME_ARG=`gconftool-2 --get /desktop/gnome/applications/terminal/exec_arg`
	which konsole &> /dev/null
	[ $? = 0 ] && KONSOLE=konsole
	which xterm &> /dev/null
	[ $? = 0 ] && XTERM=xterm
	MY_TERM=$( ( [ -n "$GNOME_TERM" ] && [ -n "$GNOME_DESKTOP_SESSION_ID" ] && echo $GNOME_TERM ) ||
	( [ -n "$KONSOLE" ] && [ "$KDE_FULL_SESSION" = "true" ] && echo $KONSOLE ) ||
	( [ -n "$XTERM" ] && echo $XTERM ) ||
	( [ -n "$TERMCMD" ] && echo $TERMCMD ) )
	MY_ARG="-e"
	[ "$MY_TERM" = "$GNOME_TERM" ] && MY_ARG="$GNOME_ARG"

	# detect user agents
	GNOME_BROWSER=`gconftool-2 --get /desktop/gnome/url-handlers/http/command | sed s/\"*%s\"*//`
	which konqueror &> /dev/null
	[ $? = 0 ] && KONQUEROR=konqueror
	which firefox &> /dev/null
	[ $? = 0 ] && FIREFOX=firefox
	which mozilla &> /dev/null
	[ $? = 0 ] && MOZILLA=mozilla
	MY_BROWSER=$( ( [ "$GNOME_BROWSER" != '' ] && [ -n "$GNOME_DESKTOP_SESSION_ID" ] && echo $GNOME_BROWSER ) ||
	( [ -n "$BROWSER" ] && echo $BROWSER ) ||
	( [ -n "$KONQUEROR" ] && [ "$KDE_FULL_SESSION" = "true" ] && echo $KONQUEROR ) ||
	( [ -n "$FIREFOX" ] && echo $FIREFOX ) ||
	( [ -n "$KONQUEROR" ] && echo $KONQUEROR ) ||
	( [ -n "$MOZILLA" ] && echo $MOZILLA ) )

	if [ -n "$MY_TERM" ]; then
		# Check dependencies: awk, curl, ffmpeg2theora
		which awk &> /dev/null
		[ $? -gt 0 ] && MISSING="$MISSING awk"
		which curl &> /dev/null
		[ $? -gt 0 ] && MISSING="$MISSING curl"
		if [ -n "$MISSING" ]; then
			$MY_TERM $MY_ARG sh $(dirname $0)/echo.sh "The blip.tv publishing script requires the following missing utilities:$MISSING"
		else
			$MY_TERM $MY_ARG sh $(dirname $0)/bliptv_frame.sh "$frame_file" "$scene_title" "$MY_BROWSER"
		fi
	fi
	rm -f "$frame_file"
fi
