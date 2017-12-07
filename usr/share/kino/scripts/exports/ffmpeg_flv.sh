#!/bin/sh
# A Kino export script that outputs to Flash video using ffmpeg

usage()
{
	# Title
	echo "Title: Flash Dual Pass (FFMPEG)"

	# Usable?
	which ffmpeg> /dev/null
	[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive

	# Type
	echo Flags: double-pass file-producer

	# Profiles
	echo "Profile: Broadband Quality FLV (medium size, 564 kb/s)"
	echo "Profile: Low Quality FLV (small size, 12fps, 128 kb/s)"
	echo "Profile: Broadband Quality SWF+XHTML (medium size, 564 kb/s)"
	echo "Profile: Low Quality SWF+XHTML (small size, 12fps, 128 kb/s)"
}

generate_xhtml()
{
	if [ "$aspect" = "16:9" ]; then
		if [ "$profile" = "2" ]; then
			width=`[ "$normalisation" = "pal" ] && echo "512" || echo "426"`
			height=`[ "$normalisation" = "pal" ] && echo "288" || echo "240"`
		else
			width=`[ "$normalisation" = "pal" ] && echo "256" || echo "214"`
			height=`[ "$normalisation" = "pal" ] && echo "144" || echo "120"`
		fi
	else
		if [ "$profile" = "2" ]; then
			width=`[ "$normalisation" = "pal" ] && echo "384" || echo "320"`
			height=`[ "$normalisation" = "pal" ] && echo "288" || echo "240"`
		else
			width=`[ "$normalisation" = "pal" ] && echo "192" || echo "160"`
			height=`[ "$normalisation" = "pal" ] && echo "144" || echo "120"`
		fi
	fi

	cat > "$1" << EOF
<div style="text-align: center;">
  <object width="$width" height="$height" align="middle"
    codebase="http://fpdownload.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=7,0,0,0"
    classid="clsid:d27cdb6e-ae6d-11cf-96b8-444553540000">
    <param name="allowFlashAutoInstall" value="true" />
    <param name="quality" value="high" />
    <param name="bgcolor" value="#ffffff" />
    <param name="movie" value="`basename "$1" .html`.swf" />
    <embed width="$width" height="$height" align="center"
      pluginspage="http://www.macromedia.com/go/getflashplayer"
      type="application/x-shockwave-flash"
      quality="high"
      bgcolor="#ffffff"
      src="`basename "$1" .html`.swf" />
  </object>
</div>
EOF
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
	ffmpeg_generate_hq

	# generate filename if missing
	[ "x$file" = "x" ] && file="kino_export_"`date +%Y-%m-%d_%H.%M.%S`

	# Determine info arguments
	size=`[ "$normalisation" = "pal" ] && echo 352x288 || echo 352x240`
	[ $pass -eq "2" ] && ffmpeg_generate_hq
	
	# Run the command
	case "$profile" in 
		"0" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" $hq \
			-r "$normalisation" -g 300 -b 500$kilo -ac 2 -ab 64$audio_kilo $progressive -s $med_res -aspect $aspect \
			-ar 44100 -y "$file".flv ;;
		"1" ) 	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" $hq \
			-r 12.0 -g 120 -b 96$kilo -ac 1 -ab 32$audio_kilo $progressive -s $low_res -aspect $aspect \
			-ar 22050 -y "$file".flv ;;
		"2" )	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" $hq \
			-r "$normalisation" -g 300 -b 500$kilo -ac 2 -ab 64$audio_kilo $progressive -s $med_res -aspect $aspect \
			-ar 44100 -y "$file".swf
			[ $pass -eq "2" ] && generate_xhtml "$file".html
			;;
		"3" )	ffmpeg -f dv -i pipe: -pass $pass -passlogfile "$file" $hq \
			-r 12.0 -g 120 -b 96$kilo -ac 1 -ab 32$audio_kilo $progressive -s $low_res -aspect $aspect \
			-ar 22050 -y "$file".swf
			[ $pass -eq "2" ] && generate_xhtml "$file".html
			;;
	esac
	[ $pass -eq "2" ] && rm -f "$file-0.log"
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
