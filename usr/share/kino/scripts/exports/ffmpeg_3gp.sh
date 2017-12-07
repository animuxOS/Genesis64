#!/bin/sh
# A Kino export script that outputs to 3GPPv5 using ffmpeg, optionally hinted
# with gpac's MP4Box.

usage()
{
	# Title
	echo "Title: MPEG-4 3GPP Mobile (FFMPEG)"

	# Usable?
        test=`ffmpeg -formats 2> /dev/null | egrep "(Encoders:)|(.*EA.*aac)" | grep aac | wc -l`
        [ "$test" -gt 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: double-pass file-producer
	
        # Profiles
	which MP4Box > /dev/null
	if [ $? -eq 0 ]; then
		echo "Profile: 2.5G Unhinted"
		echo "Profile: 2.5G Hinted"
		echo "Profile: 3G Unhinted"
		echo "Profile: 3G Hinted"
	fi
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

	# only do high quality on second pass
	[ $pass -eq "2" ] && ffmpeg_generate_hq

	# Run the command
	if [ "$profile" -ge "0" ] && [ "$profile" -le "1" ]; then 
		ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" -f 3gp \
		-vcodec mpeg4 $hq -b 30$kilo -minrate 0 -maxrate 32$kilo -bufsize 20$bufsize \
		-r 5 $progressive -s qcif -aspect $aspect -g 10 \
		-acodec $aac -ab 12$audio_kilo -ar 8000 -ac 1 -y "$file".3gp
	else
		ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" -f 3gp \
		-vcodec mpeg4 $hq -b 90$kilo -minrate 0 -maxrate 100$kilo -bufsize 40$bufsize \
		-r 12 $progressive -s qcif -aspect $aspect -g 24 \
		-acodec $aac -ab 20$audio_kilo -ar 12000 -ac 1 -y "$file".3gp
	fi
	
	if [ $pass -eq "2" ]; then
		rm -f "$file-0.log"
		if [ $profile -eq "1" ] || [ $profile -eq "3" ]; then
			MP4Box -hint -latm "$file".3gp 1>&2
		fi
	fi
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
