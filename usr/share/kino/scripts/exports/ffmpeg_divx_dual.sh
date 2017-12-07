#!/bin/sh
# A Kino export script that outputs to MPEG-4 AVI with ffmpeg

usage()
{
	# Title
	echo "Title: MPEG-4 AVI Dual Pass (FFMPEG)"

	# Usable?
	which ffmpeg > /dev/null
	[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: double-pass file-producer

	# Profiles
	echo "Profile: Best Quality (native size, interlace, 2240 kb/s)"
	echo "Profile: High Quality (full size, progressive, 2240 kb/s)"
	echo "Profile: Medium Quality (medium size, progressive, 1152 kb/s)"
	echo "Profile: Broadband Quality (medium size, progressive, 564 kb/s)"
	echo "Profile: Low Quality (small size, 12fps, progressive, 128 kb/s)"
}

execute()
{
	# Arguments
	normalisation="$1"
	length="$2"
	profile="$3"
	file="$4"
	pass="$6"
	aspect="$7"
	
	. "`dirname $0`/ffmpeg_utils.sh"

	# generate filename if missing
	[ "x$file" = "x" ] && file="kino_export_"`date +%Y-%m-%d_%H.%M.%S`
	
	# Determine audio codec (MP3 if avail)
	acodec="mp2"
	mp3=0
	mp3=`ffmpeg -formats 2> /dev/null | egrep "(Encoders:)|(.*EA.*mp3)" | grep mp3 | wc -l`
	[ "$mp3" -gt 0 ] && acodec="mp3"

	# Set high quality on second pass
	[ $pass -eq "2" ] && ffmpeg_generate_hq

	# Run the command
	case "$profile" in 
		"0" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" $hq \
			-g 300 -vtag DIVX $interlace -aspect $aspect -b 2048$kilo \
			-acodec "$acodec" -ab 192$audio_kilo -y "$file".avi ;;
		"1" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" $hq \
			-g 300 -vtag DIVX $progressive -s $full_res -aspect $aspect -b 2048$kilo \
			-acodec "$acodec" -ab 192$audio_kilo -y "$file".avi ;;
		"2" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" $hq \
			-g 300 -vtag DIVX $progressive -s $med_res -aspect $aspect -b 1024$kilo \
			-acodec "$acodec" -ar 44100 -ab 128$audio_kilo -y "$file".avi ;;
		"3" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" $hq \
			-g 300 -vtag DIVX $progressive -s $med_res -aspect $aspect -b 500$kilo \
			-acodec "$acodec" -ar 32000 -ab 64$audio_kilo -y "$file".avi ;;
		"4" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" $hq \
			-r 12 -g 120 -vtag DIVX $progressive -s $low_res -aspect $aspect -b 96$kilo \
			-acodec "$acodec" -ac 1 -ar 22050 -ab 32$audio_kilo -y "$file".avi ;;
	esac
	if [ $pass -eq "2" ]; then
		rm -f "$file-0.log"
	fi
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
