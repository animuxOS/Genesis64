#!/bin/sh
# A Kino export script that outputs to DVD-Video with ffmpeg and mplex,
# optionally processed with dvdauthor

usage()
{
	# Title
	echo "Title: DVD-Video Single Pass (FFMPEG)"

	# Usable?
	which ffmpeg > /dev/null
	if [ $? -eq 0 ]; then
		which mplex >/dev/null
		[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive
	else
		echo Status: Inactive
	fi

	# Type
	echo Flags: single-pass file-producer

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
	M2V="`mktemp \"$file\".XXXXXX`"
	AC3="`mktemp \"$file\".XXXXXX`"

	# Run the command
	case "$profile" in
		"0" )
			ffmpeg -v 0 -f dv -i pipe: -f rawvideo -pix_fmt yuv420p pipe: \
			-vn -f $audio_format -ac 2 -ab $audio_bitrate -ar 48000 -y "$AC3" | \
			ffmpeg -v 0 -f rawvideo -pix_fmt yuv420p -s "$normalisation" -r "$normalisation" -i pipe: \
			-an -target dvd -f mpeg2video -maxrate 8000$kilo $interlace -aspect $aspect -y "$M2V"
			mplex -v 0 -f 8 -o "$file".vob "$M2V" "$AC3"
			;;
		"1" )
			VOB=`mktemp -u $file.XXXXXX`
			mkfifo "$VOB"
			rm -rf "$file"

			ffmpeg -v 0 -f dv -i pipe: -f rawvideo -pix_fmt yuv420p pipe: \
			-vn -f $audio_format -ac 2 -ab $audio_bitrate -ar 48000 -y "$AC3" | \
			ffmpeg -v 0 -f rawvideo -pix_fmt yuv420p -s "$normalisation" -r "$normalisation" -i pipe: \
			-an -target dvd -f mpeg2video -maxrate 8000$kilo $interlace -aspect $aspect -y "$M2V"
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
			;;
	esac
	rm -f "$M2V" "$AC3"
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
