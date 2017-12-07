#!/bin/sh
# A Kino export script that outputs to MPEG-4 part 2 AVI using mencoder with Xvid

usage()
{
	# Title
	echo "Title: XviD MPEG-4 AVI Single Pass (MEncoder)"

	# Usable?
	command -v mencoder 1> /dev/null 2>&1
	[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: single-pass file-producer

	# Profiles
	echo "Profile: High Quality (full size, VBR, QPEL)"
	echo "Profile: High Quality (full size, 2240 kb/s)"
	echo "Profile: Medium Quality (medium size, VBR)"
	echo "Profile: Medium Quality (medium size, 1152 kb/s)"
	echo "Profile: Broadband Quality (medium size, 564 kb/s)"
}

execute()
{
	# Arguments
	normalisation="$1"
	length="$2"
	profile="$3"
	file="$4"
	aspect="$7"

	# generate filename if missing
	[ "x$file" = "x" ] && file="kino_export_"`date +%Y-%m-%d_%H.%M.%S`

	if [ "$aspect" = "16:9" ]; then
		full_res=`[ "$normalisation" = "pal" ] && echo "1024:576" || echo "854:480"`
		med_res=`[ "$normalisation" = "pal" ] && echo "512:288" || echo "426:240"`
		low_res=`[ "$normalisation" = "pal" ] && echo "256:144" || echo "214:120"`
	else
		full_res=`[ "$normalisation" = "pal" ] && echo "768:576" || echo "640:480"`
		med_res=`[ "$normalisation" = "pal" ] && echo "384:288" || echo "320:240"`
		low_res=`[ "$normalisation" = "pal" ] && echo "192:144" || echo "160:120"`
	fi

	# Run the command
	# Note that the -cache 8192 parameter is required to force mencoder
	# to recognize the DV stream on STDIN.
	case "$profile" in 
		"0" )   mencoder - -demuxer rawdv -quiet -cache 8192 -aspect $aspect -vf harddup,pp=ci,scale=$full_res -ovc xvid -oac mp3lame -lameopts preset=standard -xvidencopts fixed_quant=2:qpel -o "$file".avi ;;
		"1" )   mencoder - -demuxer rawdv -quiet -cache 8192 -aspect $aspect -vf harddup,pp=ci,scale=$full_res -ovc xvid -oac mp3lame -lameopts preset=192 -xvidencopts bitrate=2048 -o "$file".avi ;;
		"2" )   mencoder - -demuxer rawdv -quiet -cache 8192 -aspect $aspect -vf harddup,pp=ci,scale=$med_res -af-adv force=1 -srate 44100 -ovc xvid -oac mp3lame -lameopts preset=medium -xvidencopts fixed_quant=4 -o "$file".avi ;;
		"3" )   mencoder - -demuxer rawdv -quiet -cache 8192 -aspect $aspect -vf harddup,pp=ci,scale=$med_res -af-adv force=1 -srate 44100 -ovc xvid -oac mp3lame -lameopts preset=128 -xvidencopts bitrate=1024:pass= -o "$file".avi ;;
		"4" )   mencoder - -demuxer rawdv -quiet -cache 8192 -aspect $aspect -vf harddup,pp=ci,scale=$med_res -af-adv force=1 -srate 32000 -ovc xvid -oac mp3lame -lameopts preset=64 -xvidencopts bitrate=500 -o "$file".avi ;;
	esac
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
