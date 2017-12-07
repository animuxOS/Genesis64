#!/bin/sh
# A Kino export script that outputs to H.264 MP4 using ffmpeg with x264

usage()
{
	# Title
	echo "Title: H.264 MP4 Single Pass (FFMPEG)"

	# Usable?
	aac=`ffmpeg -formats 2> /dev/null | egrep "(Encoders:)|(.*EA.*aac)" | grep aac | wc -l`
	h264=`ffmpeg -formats 2> /dev/null | egrep "(Encoders:)|(.*EV.*264)" | grep 264 | wc -l`
	[ "$aac" -gt 0 ] && [ "$h264" -gt 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: single-pass file-producer

	# Profiles
	echo "Profile: Best Quality (native size, interlace, VBR)"
	echo "Profile: High Quality (full size, progressive, VBR)"
	echo "Profile: Medium Quality (medium size, progressive, VBR)"
	echo "Profile: Broadband Quality (medium size, progressive, 564 kb/s)"
	echo "Profile: 3G Mobile Quality (176x144, progressive, 12fps, 128 kb/s)"
}

execute()
{
	# Arguments
	normalisation="$1"
	length="$2"
	profile="$3"
	file="$4"
	project="$5"
	pass="$6"
	aspect="$7"

	. "`dirname $0`/ffmpeg_utils.sh"
	ffmpeg_generate_hq
	test_lf=`echo $ffmpeg_help | grep '\-lf' | wc -l`
	[ "$test_lf" -gt 0 ] && hq="$hq -lf"
	test_flags=`echo $ffmpeg_help | grep '\-flags' | wc -l`
	[ "$test_flags" -gt 0 ] && hq="$hq -flags +loop"

	# generate filename if missing
	[ "x$file" = "x" ] && file="kino_export_"`date +%Y-%m-%d_%H.%M.%S`
	
	# Create metadata options
	title=`awk '/title="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /title=/) z = y + 1; print x[z]; exit}' "$project"`
	author=`awk '/author="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /author=/) z = y + 1; print x[z]; exit}' "$project"`
	comment=`awk '/abstract="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /abstract=/) z = y + 1; print x[z]; exit}' "$project"`
	copyright=`awk '/copyright="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /copyright=/) z = y + 1; print x[z]; exit}' "$project"`
	
	# Run the command
	case "$profile" in 
		"0" ) 	ffmpeg -f dv -i pipe: \
			-vcodec h264 -g 300 $hq $interlace -aspect $aspect -qscale 2 -ab 192$audio_kilo \
			-title "$title" -author "$author" -comment "$comment" -copyright "$copyright" \
			-y "$file".mp4 ;;
		"1" ) 	ffmpeg -f dv -i pipe: \
			-vcodec h264 -g 300 $hq $progressive -s $full_res -aspect $aspect -qscale 2 -ab 192$audio_kilo \
			-title "$title" -author "$author" -comment "$comment" -copyright "$copyright" \
			-y "$file".mp4 ;;
		"2" ) 	ffmpeg -f dv -i pipe: \
			-vcodec h264 -g 300 $hq $progressive -s $med_res -aspect $aspect -qscale 4 -ab 128$audio_kilo -ar 44100 \
			-title "$title" -author "$author" -comment "$comment" -copyright "$copyright" \
			-y "$file".mp4 ;;
		"3" ) 	ffmpeg -f dv -i pipe: \
			-vcodec h264 -g 300 $hq $progressive -s $med_res -aspect $aspect -b 500$kilo -ab 64$audio_kilo -ar 32000 \
			-title "$title" -author "$author" -comment "$comment" -copyright "$copyright" \
			-y "$file".mp4 ;;
		"4" ) 	ffmpeg -f dv -i pipe: \
			-vcodec h264 $hq -r 12 -g 120 $progressive -s qcif -aspect $aspect -b 90$kilo -minrate 0 -maxrate 100$kilo -bufsize 40$bufsize \
			-ac 1 -ab 28$audio_kilo -ar 16000 \
			-title "$title" -author "$author" -comment "$comment" -copyright "$copyright" \
			-y "$file".mp4 ;;
	esac
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
