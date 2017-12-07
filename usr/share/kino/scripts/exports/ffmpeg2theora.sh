#!/bin/sh
# A Kino export script that outputs to Ogg Theora using ffmpeg2theora
# http://v2v.cc/~j/ffmpeg2theora/
# written by jan gerber <j@v2v.cc>
# profiles added by Dan Dennedy

usage()
{
	# Title
	echo "Title: Ogg Theora (ffmpeg2theora)"

	# Usable?
	which ffmpeg2theora > /dev/null
	[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: single-pass file-producer
	
	# Profiles
	echo "Profile: Best Quality (native size)"
	echo "Profile: High Quality (full size)"
	echo "Profile: Medium Quality (medium size)"
	echo "Profile: Broadband Quality (medium size, 564 Kbps)"
	echo "Profile: Low Quality (small size, 128Kbps)"
}

execute()
{
	# Arguments
	normalisation="$1"
	length="$2"
	profile="$3"
	file="$4"
	project="$5"
	aspect="$7"

	# generate filename if missing
	[ "x$file" = "x" ] && file="kino_export_"`date +%Y-%m-%d_%H.%M.%S`

	# Create metadata options
	title=`awk '/title="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /title=/) z = y + 1; print x[z]; exit}' "$project"`
	artist=`awk '/author="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /author=/) z = y + 1; print x[z]; exit}' "$project"`
	location=`awk '/abstract="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /abstract=/) z = y + 1; print x[z]; exit}' "$project"`
	copyright=`awk '/copyright="/ {split($0, x, "\""); z = 0; for (y in x) if (x[y] ~ /copyright=/) z = y + 1; print x[z]; exit}' "$project"`

	# some versions seem to not overwrite existing files correctly
	rm "$file".ogg

	if [ "$aspect" = "16:9" ]; then
		if [ "$normalisation" = "pal" ]; then
			full_res_x="1024"
			full_res_y="576"
			med_res_x="512"
			med_res_y="288"
			low_res_x="256"
			low_res_y="144"
		else
			full_res_x="856"
			full_res_y="480"
			med_res_x="424"
			med_res_y="240"
			low_res_x="216"
			low_res_y="120"
		fi
	else
		if [ "$normalisation" = "pal" ]; then
			full_res_x="768"
			full_res_y="576"
			med_res_x="384"
			med_res_y="288"
			low_res_x="192"
			low_res_y="144"
		else
			full_res_x="640"
			full_res_y="480"
			med_res_x="320"
			med_res_y="240"
			low_res_x="160"
			low_res_y="120"
		fi
	fi

	# Run the command
	case "$profile" in 
		"0" ) 	ffmpeg2theora -f dv --aspect $aspect --deinterlace -v 10 -a 10 \
				--title "$title" --artist "$artist" --location "$location" --copyright "$copyright" \
				-o "$file".ogg - ;;
		"1" ) 	ffmpeg2theora -f dv -x $full_res_x -y $full_res_y --aspect $aspect --deinterlace -v 7 -a 3 \
				--title "$title" --artist "$artist" --location "$location" --copyright "$copyright" \
				-o "$file".ogg - ;;
		"2" ) 	ffmpeg2theora -f dv -x $med_res_x -y $med_res_y --aspect $aspect --deinterlace -v 7 -a 3 -H 44100 \
				--title "$title" --artist "$artist" --location "$location" --copyright "$copyright" \
				-o "$file".ogg - ;;
		"3" ) 	ffmpeg2theora -f dv -x $med_res_x -y $med_res_y --aspect $aspect --deinterlace -v 5 -V 500 -K 200 -a 3 -A 64 -H 32000 \
				--title "$title" --artist "$artist" --location "$location" --copyright "$copyright" \
				-o "$file".ogg - ;;
		"4" ) 	ffmpeg2theora -f dv -x $low_res_x -y $low_res_y --aspect $aspect --deinterlace -v 1 -V 84 -K 300 -a 0 -A 44 -H 22050 \
				--title "$title" --artist "$artist" --location "$location" --copyright "$copyright" \
				-o "$file".ogg - ;;
	esac
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
