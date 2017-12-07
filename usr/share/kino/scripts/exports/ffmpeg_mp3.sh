#!/bin/sh
# A Kino export script that outputs to MP3 using ffmpeg with lame

usage()
{
	# Title
	echo "Title: MP3 (FFMPEG)"

	# Usable?
	which ffmpeg > /dev/null
	mp3=0
	[ $? -eq 0 ] && mp3=`ffmpeg -formats 2> /dev/null | egrep "(Encoders:)|(.*EA.*mp3)" | grep mp3 | wc -l`
	[ "$mp3" -gt 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: single-pass file-producer

	# Profiles
	echo Profile: MP3 192kb/s, 48000 khz, Stereo
	echo Profile: MP3 128kb/s, 44100 khz, Stereo
	echo Profile: MP3 64kb/s, 32000 khz, Stereo
	echo Profile: MP3 192kb/s, 48000 khz, Mono
	echo Profile: MP3 128kb/s, 44100 khz, Mono
	echo Profile: MP3 64kb/s, 32000 khz, Mono
}

execute()
{
	# Arguments
	normalisation="$1"
	length="$2"
	profile="$3"
	file="$4"

	# generate filename if missing
	[ "x$file" = "x" ] && file="kino_export_"`date +%Y-%m-%d_%H.%M.%S`

	# Run the command
	case "$profile" in 
		"0" ) 	ffmpeg -f dv -i - -f mp3 -acodec mp3 -ab 192$audio_kilo -ar 48000 -ac 2 -y "$file".mp3 ;;
		"1" ) 	ffmpeg -f dv -i - -f mp3 -acodec mp3 -ab 128$audio_kilo -ar 44100 -ac 2 -y "$file".mp3 ;;
		"2" ) 	ffmpeg -f dv -i - -f mp3 -acodec mp3 -ab 64$audio_kilo -ar 32000 -ac 2 -y "$file".mp3 ;;
		"3" ) 	ffmpeg -f dv -i - -f mp3 -acodec mp3 -ab 192$audio_kilo -ar 48000 -ac 1 -y "$file".mp3 ;;
		"4" ) 	ffmpeg -f dv -i - -f mp3 -acodec mp3 -ab 128$audio_kilo -ar 44100 -ac 1 -y "$file".mp3 ;;
		"5" ) 	ffmpeg -f dv -i - -f mp3 -acodec mp3 -ab 64$audio_kilo -ar 32000 -ac 1 -y "$file".mp3 ;;
	esac
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
