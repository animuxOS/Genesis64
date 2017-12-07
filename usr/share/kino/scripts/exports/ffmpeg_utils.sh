#!/bin/sh
# A Kino export script helper for ffmpeg - version handling and high quality settings

if [ "$1" != "--usage" ] && [ "x$1" != "x" ]; then 
	ffmpeg_help=`ffmpeg -h 2>&1`
	[ `echo $ffmpeg_help | grep 'bits/s' | wc -l` -gt 0 ] && kilo="000"
	[ `echo $ffmpeg_help | grep '\-ab.*bits/s' | wc -l` -gt 0 ] && audio_kilo="000"
	[ `echo $ffmpeg_help | grep '\-bufsize.*bits' | wc -l` -gt 0 ] && bufsize="*8*1024"
	ffmpeg_formats=`ffmpeg -formats 2>&1`
	aac="aac"
	[ `echo $ffmpeg_formats | egrep "(Encoders:)|(.*EA.*libfaac)" | wc -l` -gt 0 ] && aac="libfaac"
	xvid="xvid"
	[ `echo $ffmpeg_formats | egrep "(Encoders:)|(.*EV.*libxvid)" | wc -l` -gt 0 ] && xvid="libxvid"
	x264="h264"
	[ `echo $ffmpeg_formats | egrep "(Encoders:)|(.*EV.*libx264)" | wc -l` -gt 0 ] && x264="libx264"
	
	test_mv4=`echo $ffmpeg_help | grep 'mv4' | wc -l`
	interlace=`[ "$test_mv4" -gt 0 ] && echo "-ildct 1 -ilme 1" || echo "-ildct -ilme"`
	progressive="-deinterlace"
	
	if [ "$aspect" = "16:9" ]; then
		full_res=`[ "$normalisation" = "pal" ] && echo "1024x576" || echo "854x480"`
		med_res=`[ "$normalisation" = "pal" ] && echo "512x288" || echo "426x240"`
		low_res=`[ "$normalisation" = "pal" ] && echo "256x144" || echo "214x120"`
	else
		full_res=`[ "$normalisation" = "pal" ] && echo "768x576" || echo "640x480"`
		med_res=`[ "$normalisation" = "pal" ] && echo "384x288" || echo "320x240"`
		low_res=`[ "$normalisation" = "pal" ] && echo "192x144" || echo "160x120"`
	fi
fi

# Generate FFMPEG hiqh quality settings based upon version
ffmpeg_generate_hq()
{
	test_hq=`echo $ffmpeg_help | grep '\-hq' | wc -l`
	test_4mv=`echo $ffmpeg_help | grep '\-4mv' | wc -l`
	hq="-mbd 2 -cmp 2 -subcmp 2"
	qpel="-qpel"
	[ "$test_4mv" -gt 0 ] && hq="$hq -4mv"
	if [ "$test_mv4" -gt 0 ]; then
		hq="$hq -mv4 1"
		qpel="-qpel 1"
	fi
}
