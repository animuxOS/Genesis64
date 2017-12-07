#!/bin/sh
# A Kino export script that plays video using smilutils' rawplay

usage()
{
	# Title
	echo "Title: rawplay playback"

	# Usable?
	which rawplay > /dev/null
	[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: single-pass 

	# Profiles
	echo Profile: Full Screen, ALSA audio output
	echo Profile: Full Screen, OSS audio output
	echo Profile: Full Screen, ARTS audio output
	echo Profile: Full Screen, ESD audio output
	echo Profile: Windowed, ALSA audio output
	echo Profile: Windowed, OSS audio output
	echo Profile: Windowed, ARTS audio output
	echo Profile: Windowed, ESD audio output
}

execute()
{
	# Arguments
	normalisation="$1"
	length="$2"
	profile="$3"

	# Run the command
	case "$profile" in 
		"0" ) 	rawplay -b -f -ao alsa ;;
		"1" ) 	rawplay -b -f -ao dsp ;;
		"2" ) 	rawplay -b -f -ao artsc ;;
		"3" ) 	rawplay -b -f -ao esd ;;
		"4" ) 	rawplay -b -ao alsa ;;
		"5" ) 	rawplay -b -ao dsp ;;
		"6" ) 	rawplay -b -ao artsc ;;
		"7" ) 	rawplay -b -ao esd ;;
	esac
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
