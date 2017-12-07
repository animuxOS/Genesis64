#!/bin/sh
# A Kino export script that outputs to MPEG-4 part 2 AVI using ffmpeg with Xvid

usage()
{
	# Title
	echo "Title: XviD MPEG-4 AVI Single Pass (FFMPEG)"

	# Usable?
	xvid=`ffmpeg -formats 2> /dev/null | egrep "(Encoders:)|(.*EV.*xvid)" | grep xvid | wc -l`
	[ "$xvid" -gt 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: single-pass file-producer

	# Profiles
	echo "Profile: Best Quality (native size, interlace, VBR)"
	echo "Profile: High Quality (full size, progressive, VBR, QPEL)"
	echo "Profile: Medium Quality (medium size, progressive, VBR)"
	echo "Profile: Broadband Quality (medium size, progressive, 564 kb/s)"
	echo "Profile: Low Quality (small size, progressive, 12fps, 128 kb/s)"
}

execute()
{
	# Arguments
	normalisation="$1"
	length="$2"
	profile="$3"
	file="$4"
	aspect="$7"

	. "`dirname $0`/ffmpeg_utils.sh"
	ffmpeg_generate_hq

	# generate filename if missing
	[ "x$file" = "x" ] && file="kino_export_"`date +%Y-%m-%d_%H.%M.%S`
	
	# Determine audio codec (MP3 if avail)
	acodec="mp2"
	mp3=0
	mp3=`ffmpeg -formats 2> /dev/null | egrep "(Encoders:)|(.*E.*mp3)" | grep mp3 | wc -l`
	[ "$mp3" -gt 0 ] && acodec="mp3"

	# Run the command
	case "$profile" in 
		"0" ) 	ffmpeg -f dv -i pipe: $hq $interlace \
			-vcodec $xvid -g 300 -aspect $aspect -qscale 2 \
			-acodec "$acodec" -ab 192$audio_kilo -y "$file".avi ;;
		"1" ) 	ffmpeg -f dv -i pipe: $hq $progressive -s $full_res \
			-vcodec $xvid -g 300 -aspect $aspect -qscale 2 $qpel \
			-acodec "$acodec" -ab 192$audio_kilo -y "$file".avi ;;
		"2" ) 	ffmpeg -f dv -i pipe: $hq $progressive -s $med_res \
			-vcodec $xvid -g 300 -aspect $aspect -qscale 4 \
			-acodec "$acodec" -ar 44100 -ab 128$audio_kilo -y "$file".avi ;;
		"3" ) 	ffmpeg -f dv -i pipe: $hq $progressive -s $med_res \
			-vcodec $xvid -g 300 -aspect $aspect -b 500$kilo \
			-acodec "$acodec" -ar 32000 -ab 64$audio_kilo -y "$file".avi ;;
		"4" ) 	ffmpeg -f dv -i pipe: $hq -r 12 -g 120 $progressive -s $low_res \
			-vcodec $xvid -aspect $aspect -b 96$kilo \
			-acodec "$acodec" -ac 1 -ar 22050 -ab 32$audio_kilo -y "$file".avi ;;
	esac
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
