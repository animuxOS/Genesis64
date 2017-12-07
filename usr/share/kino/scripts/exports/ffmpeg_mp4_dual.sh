#!/bin/sh
# A Kino export script that outputs to MPEG-4 part 2 MP4 using ffmpeg

usage()
{
	# Title
	echo "Title: MPEG-4 MP4 Dual Pass (FFMPEG)"

	# Usable?
	aac=`ffmpeg -formats 2> /dev/null | egrep "(Encoders:)|(.*EA.*aac)" | grep aac | wc -l`
	[ "$aac" -gt 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: double-pass file-producer

	# Profiles
	echo "Profile: Best Quality (native size, interlace, 2240 kb/s)"
	echo "Profile: High Quality (full size, progressive, 2240 kb/s)"
	echo "Profile: Medium Quality (medium size, progressive, 1152 kb/s)"
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
	project="$5"
	pass="$6"
	aspect="$7"

	. "`dirname $0`/ffmpeg_utils.sh"

	# generate filename if missing
	[ "x$file" = "x" ] && file="kino_export_"`date +%Y-%m-%d_%H.%M.%S`
	
	# Variable parameters
	hq=""
	[ $pass -eq "2" ] && ffmpeg_generate_hq

	# Create metadata options
	title=`awk '/title="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /title=/) z = y + 1; print x[z]; exit}' "$project"`
	author=`awk '/author="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /author=/) z = y + 1; print x[z]; exit}' "$project"`
	comment=`awk '/abstract="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /abstract=/) z = y + 1; print x[z]; exit}' "$project"`
	copyright=`awk '/copyright="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /copyright=/) z = y + 1; print x[z]; exit}' "$project"`
	
	# Run the command
	case "$profile" in 
		"0" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" \
			-g 300 $hq $interlace -aspect $aspect -b 2048$kilo -ab 192$audio_kilo \
			-title "$title" -author "$author" -comment "$comment" -copyright "$copyright" \
			-y "$file".mp4 ;;
		"1" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" \
			-g 300 $hq $progressive -s $full_res -aspect $aspect -b 2048$kilo -ab 192$audio_kilo \
			-title "$title" -author "$author" -comment "$comment" -copyright "$copyright" \
			-y "$file".mp4 ;;
		"2" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" \
			-g 300 $hq $progressive -s $med_res -aspect $aspect -b 1024$kilo -ab 128$audio_kilo -ar 44100 \
			-title "$title" -author "$author" -comment "$comment" -copyright "$copyright" \
			-y "$file".mp4 ;;
		"3" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" \
			-g 300 $hq $progressive -s $med_res -aspect $aspect -b 500$kilo -g 60 -ab 64$audio_kilo -ar 32000 \
			-title "$title" -author "$author" -comment "$comment" -copyright "$copyright" \
			-y "$file".mp4 ;;
		"4" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" \
			$hq -r 12 -g 120 $progressive -s $low_res -aspect $aspect -b 96$kilo -ac 1 -ab 32$audio_kilo -ar 22050 \
			-title "$title" -author "$author" -comment "$comment" -copyright "$copyright" \
			-y "$file".mp4 ;;
	esac
	[ $pass -eq "2" ] && rm -f "$file-0.log"
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
