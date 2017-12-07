#!/bin/sh
# A Kino export script that outputs to VCD compliant MPEG-1

usage()
{
	# Title
	echo "Title: VCD (FFMPEG)"

	# Usable?
	which ffmpeg > /dev/null
	[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: single-pass file-producer
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

	. "`dirname $0`/ffmpeg_utils.sh"

	# Determine info arguments
	size=`[ "$normalisation" = "pal" ] && echo 352x288 || echo 352x240`
	video_bitrate=1152$kilo
	audio_bitrate=224$audio_kilo

	# Run the command
	ffmpeg -f dv -i - -f vcd -deinterlace -r "$normalisation" -s "$size" -b "$video_bitrate" -acodec mp2 -ab "$audio_bitrate" -y "$file".mpeg
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
