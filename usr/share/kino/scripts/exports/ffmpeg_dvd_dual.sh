#!/bin/sh
# A Kino export script that outputs to DVD-Video with ffmpeg and mplex,
# optionally processed with dvdauthor

usage()
{
	# Title
	echo "Title: DVD-Video Dual Pass (FFMPEG)"

	# Usable?
	which ffmpeg > /dev/null
	if [ $? -eq 0 ]; then
		which mplex >/dev/null
		[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive
	else
		echo Status: Inactive
	fi

	# Type
	echo Flags: double-pass file-producer

	# Profiles
	echo "Profile: VOB"
	which dvdauthor > /dev/null
	if [ $? -eq 0 ]; then
		echo "Profile: DVD-Video directory (All only)"
	fi
}

execute()
{
	# Arguments
	normalisation="$1"
	length="$2"
	profile="$3"
	file="$4"
	smil_file="$5"
	pass="$6"
	aspect="$7"

	. "`dirname $0`/ffmpeg_utils.sh"

	# generate filename if missing
	[ "x$file" = "x" ] && file="kino_export_"`date +%Y-%m-%d_%H.%M.%S`
	file="`dirname \"$file\"`/`basename \"$file\"`"

	# Determine info arguments
	frame_rate=`[ "$normalisation" = "pal" ] && echo 25 || echo 29.97`
	audio_format="ac3"
	audio_bitrate="192$audio_kilo"

	# Build path to extract_chapters Perl script
	get_chapters="`dirname $0`/extract_chapters"

	# Prepare temporary files
	M2V="$file.m2v"
	AC3="$file.ac3"
	LOG="$file"

	# Run the command
	case "$profile" in
		"0" )
			if [ $pass -eq "1" ]; then
				ffmpeg -v 0 -f dv -i pipe: -f rawvideo -pix_fmt yuv420p pipe: \
				-vn -f $audio_format -ac 2 -ab $audio_bitrate -ar 48000 -y "$AC3" | \
				ffmpeg -v 0 -f rawvideo -pix_fmt yuv420p -s "$normalisation" -r "$normalisation" -i pipe: \
				-an -target dvd -f mpeg2video -maxrate 8000$kilo -ildct -ilme -aspect $aspect -pass 1 -passlogfile "$LOG" -y "$M2V"
			else
				if [ $pass -eq "2" ]; then
					ffmpeg -v 0 -f dv -i pipe: -an -f rawvideo -pix_fmt yuv420p pipe: | \
					ffmpeg -v 0 -f rawvideo -pix_fmt yuv420p -s "$normalisation" -r "$normalisation" -i pipe: \
					-an -target dvd -f mpeg2video -maxrate 8000$kilo $interlace -aspect $aspect -pass 2 -passlogfile "$LOG" -y "$M2V"
					mplex -v 0 -f 8 -o "$file".vob "$M2V" "$AC3"
					rm -f "$M2V" "$AC3" "$LOG-0.log"
				fi
			fi
			;;
		"1" )
			if [ $pass -eq "1" ]; then
				ffmpeg -v 0 -f dv -i pipe: -f rawvideo -pix_fmt yuv420p pipe: \
				-vn -f $audio_format -ac 2 -ab $audio_bitrate -ar 48000 -y "$AC3" | \
				ffmpeg -v 0 -f rawvideo -pix_fmt yuv420p -s "$normalisation" -r "$normalisation" -i pipe: \
				-an -target dvd -f mpeg2video -maxrate 8000$kilo $interlace -aspect $aspect -pass 1 -passlogfile "$LOG" -y "$M2V"
			else
				if [ $pass -eq "2" ]; then
					VOB=`mktemp -u $file.XXXXXX`
					mkfifo "$VOB"
					rm -rf "$file"

					ffmpeg -v 0 -f dv -i pipe: -an -f rawvideo -pix_fmt yuv420p pipe: | \
					ffmpeg -v 0 -f rawvideo -pix_fmt yuv420p -s "$normalisation" -r "$normalisation" -i pipe: \
					-an -target dvd -f mpeg2video -maxrate 8000$kilo $interlace -aspect $aspect -pass 2 -passlogfile "$LOG" -y "$M2V"
					mplex -v 0 -f 8 -o "$VOB" "$M2V" "$AC3" &

					XML=`mktemp $file-dvdauthor.XXXXXX`
					CHAPTERS="`$get_chapters -f $frame_rate -x $smil_file`"
					echo "<?xml version=\"1.0\"?>" > "$XML"
					echo "<dvdauthor><vmgm><menus><video/><audio/><subpicture lang=\"en\"/></menus></vmgm><titleset><titles><pgc pause=\"0\">" >> "$XML"
					echo "<vob file=\"$VOB\" chapters=\"$CHAPTERS\" pause=\"0\"/>" >> "$XML"
					echo "</pgc></titles></titleset></dvdauthor>" >> "$XML"
					dvdauthor -o "$file" -x "$XML"
					dvdauthor -o "$file" -T
					rm -f "$VOB" "$XML"
					rm -f "$M2V" "$AC3" "$LOG-0.log"
				fi
			fi
			;;
	esac
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
