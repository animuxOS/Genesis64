#!/bin/bash
# Copyright (c) 2005-2007, Sven Berkvens-Matthijsse
# 
# All rights reserved.
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
# 
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
# 
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# 
# * Neither the name of deKattenFabriek nor the names of its
#   contributors may be used to endorse or promote products derived from
#   this software without specific prior written permission.
# 
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

###############################################################################
# This file is sourced by various programs of the videotrans suite
###############################################################################



###############################################################################
# Function to escape strings for use in eval or substitution
###############################################################################

shellescape()
{
	echo -n "$@" | sed 's,[^-0-9a-zA-Z,./_],\\&,g'
}

###############################################################################
# Function to escape strings for use in dvdauthor <vob file="... |">
# constructions
###############################################################################

dvdauthorescape_setting=""
dvdauthorescape()
{
	# Do we need to find out whether dvdauthor has broken escaping?

	if [ "${dvdauthorescape_setting}" = "" ]
	then
		# Find out how dvdauthor needs to escape its strings. We are trying to
		# touch two files here: one named <test\> and one named <test>. A broken
		# dvdauthor will create a file called <test test> instead. Once we know
		# this, we can compensate for its behaviour.

		mkdir "${TEMP}.dvdauthor.test"
		dvdauthor -o "${TEMP}.dvdauthor.test" "cd ${TEMP}.dvdauthor.test && "'touch test\\ test '"; mplex -v 0 -V -h -f 8 -o /dev/stdout ${datadir}/videotrans/nothing.m2v ${datadir}/videotrans/silence.mp2 |" 2>|/dev/null || :

		if [ -f "${TEMP}.dvdauthor.test/test" ]
		then
			# The file "test" exists, so the escaping was correctly done by dvdauthor

			dvdauthorescape_setting="correct"
		elif [ -f "${TEMP}.dvdauthor.test/test test" ]
		then
			# dvdauthor misbehaved and created the wrong file. Compensate for this.

			dvdauthorescape_setting="incorrect"
		else
			message "ERROR: Cannot determine whether dvdauthor has correct escaping behaviour or not! Assuming that the escaping is broken."
			dvdauthorescape_setting="incorrect"
		fi
	fi

	# We know how dvdauthor behaves now

	if [ "${dvdauthorescape_setting}" = "correct" ]
	then
		echo -n "$@" | sed 's,[^-0-9a-zA-Z,./],\\&,g'
	else
		echo -n "$@" | sed 's,[^-0-9a-zA-Z'\'',./],\\\\&,g'
	fi
}

###############################################################################
# Function to escape strings for use in ImageMagick filenames
###############################################################################

imagemagick_escape()
{
	echo -n "$@" | sed 's,[\\"],\\&,g'
}

###############################################################################
# Function to escape strings for use in XML files
###############################################################################

xmlescape()
{
	echo -n "$@" | sed -e 's,&,\&amp;,g' -e 's,<,\&lt;,g' -e 's,>,\&gt;,g' -e 's,",\&quot;,g' -e "s,',\&apos;,g"
}

###############################################################################
# Function to escape strings for use in URLs/URIs
###############################################################################

uriescape()
{
	echo -n "$@" | sed -e 's,%,%25,g' -e 's,&,%26,g' -e 's,<,%3C,g' -e 's,>,%3E,g' -e 's,",%22,g' -e "s,',%27,g" -e 's, ,%20,g' -e 's,;,%3B,g' -e 's,:,%3A,g' -e 's,+,%2B,g' -e 's,\\,%5C,g' -e 's,#,%23,g'
}

###############################################################################
# Function to display a message in a nicely formatted way
###############################################################################

message()
{
	local width
	width="${COLUMNS:-80}"

	if [ "${width}" -le 5 ]
	then
		width="80"
	fi

	width="`expr ${width} - 5`"
	prefix="--> "
	echo "$@" | LC_ALL="en_US.ISO8859-15" fmt -w "${width}" | while read -r line
	do
		echo "${prefix}$line" >&2
		prefix="    "
	done
	echo "" >&2
}

###############################################################################
# Function to determine how to encode the audio
# Sets the global variables: audio_options, audio_filter_cmd, audio_encode,
# audio_ext, new_ch
###############################################################################

audio_params()
{
	# Get all the parameters in local variables with logical names

	local speedup
	speedup="$1"
	local force_or_auto # Value may be: "ac3", "mp2" or "auto"
	force_or_auto="$2"
	local dest_file

	# Check forcing of audio type
	if [ "${force_or_auto}" = "mp2" ]
	then
		new_ch="2"
	else
		force_or_auto="ac3"
		if [ "${ch}" = "" ]
		then
			new_ch="2"
		elif [ "${ch}" -le 2 ]
		then
			new_ch="2"
		else
			new_ch="${ch}"
		fi
	fi

	# Get destination file

	if [ "$#" -lt 3 ]
	then
		dest_file="${TEMP}.wav"
	else
		dest_file="`shellescape "$3"`"
	fi

	# Calculate to which rate to convert to speed up the audio

	local new_rate
	if [ "${speedup}" != "" ]
	then
		new_rate="`echo "scale=15; ( 48000 / ${speedup} ) + 0.5" | bc`"
		new_rate="${new_rate%.*}"
	else
		new_rate="48000"
	fi

	# Message that gets displayed eventually

	local msg
	msg=""

	# Check for AC3 audio codec in the source

	local audio_type

	case "${audio_codec}"
	in
		a52)
			audio_type="AC3"
			;;
		*[!0-9]*)
			audio_type="${audio_codec}"
			;;
		?*)
			audio_type="non-standard"
			;;
		"")
			audio_type="unknown"
			;;
	esac

	if [ "${ch}" = "" ]
	then
		msg="${msg}Source has no audio at all. Creating silence from /dev/zero for the entire duration of the video stream, at 48000Hz with ${new_ch} channels. "
		new_rate="48000"
		audio_options="-channels ${new_ch} -ao pcm:waveheader:file=${dest_file} -srate ${new_rate} -audiofile /dev/zero -audio-demuxer 20"
	elif [ "${new_rate}" != "48000" ]
	then
		msg="${msg}Source has 48000Hz ${audio_type} audio with ${ch} channels. Converting it to a ${new_rate}Hz WAV with ${new_ch} channels using mplayer because the pitch of the audio needs to be adjusted. "
		audio_options="-channels ${new_ch} -ao pcm:waveheader:file=${dest_file} -af resample=${new_rate}:0:2,volnorm"
	elif [ "${new_ch}" != "${ch}" ]
	then
		msg="${msg}Source has 48000Hz ${audio_type} audio with ${ch} channels. No resampling is necessary, but converting to ${new_ch} channels. Using mplayer to save as WAV. "
		audio_options="-channels ${new_ch} -ao pcm:waveheader:file=${dest_file} -af volnorm"
	else
		msg="${msg}Source has 48000Hz ${audio_type} audio with ${ch} channels. No resampling is necessary and the number of channels does not change. Using mplayer to save as WAV. "
		audio_options="-channels ${new_ch} -ao pcm:waveheader:file=${dest_file} -af volnorm"
	fi

	if [ "${new_rate}" != "48000" ]
	then
		msg="${msg}Changing the pitch of the audio to 48000Hz using movie-fakewavspeed. "
		audio_filter_cmd="${bindir}/movie-fakewavspeed 48000"
	else
		audio_filter_cmd="cat"
	fi

	if [ "$#" -lt 3 ]
	then
		if [ "${force_or_auto}" = "ac3" ]
		then
			msg="${msg}Converting the audio from WAV to AC3 with ${new_ch} channels using ffmpeg. "
			if [ "${audio_bitrate_override}" != "auto" -a "${audio_bitrate_override}" != "" ]
			then
				audio_encode="ffmpeg -y -v 0 -f wav -i /dev/stdin -ab ${audio_bitrate_override}k -ar 48000 -ac ${new_ch} `shellescape "${output}.ac3"`"
			elif [ "${new_ch}" = "2" ]
			then
				audio_encode="ffmpeg -y -v 0 -f wav -i /dev/stdin -ab 192k -ar 48000 -ac ${new_ch} `shellescape "${output}.ac3"`"
			else
				audio_encode="ffmpeg -y -v 0 -f wav -i /dev/stdin -ab 448k -ar 48000 -ac ${new_ch} `shellescape "${output}.ac3"`"
			fi
			audio_ext="ac3"
		else
			msg="${msg}Converting the audio from WAV to MP2 using mp2enc. "
			if [ "${audio_bitrate_override}" != "auto" -a "${audio_bitrate_override}" != "" ]
			then
				audio_encode="mp2enc -v 0 -b ${audio_bitrate_override} -o `shellescape "${output}.mp2"` -r 48000 -s -e"
			else
				audio_encode="mp2enc -v 0 -b 224 -o `shellescape "${output}.mp2"` -r 48000 -s -e"
			fi
			audio_ext="mp2"
		fi
	fi

	message "${msg}"
}

###############################################################################
# Function to identify the parameters of a video file
# Sets the global variables: x, y, ch, fps, s_aspect, audio_rate,
# audio_bitrate, audio_codec
###############################################################################

mplayer_identify()
{
	local input
	input="$1"

	local audio_only
	audio_only="$2"

	# Read the movie properties from the input file.
	# -channels 6 is included to find out the real number of channels,
	# mplayer will downsample to 2 channels by default if this option is not
	# specified, but will not upsample if the stream has less than 6 channels
	# if the option IS specified, so this does what we want.

	message "Finding properties for <${input}>"
	input_escape="`shellescape "${input}"`"
	if ! mplayer -channels 6 -vo null -ao null -identify -frames 0 -slave \
		-nojoystick -nolirc -- "${input}" 2>"${TEMP}".err > "${TEMP}" < /dev/null
	then
		message "ERROR: mplayer -identify failed for <${input}>" >&2
		message "Error dump follows:" >&2
		cat "${TEMP}".err >&2 || true
		return 1
	fi

	x=""
	y=""
	ch=""
	fps=""
	s_aspect=""
	audio_rate=""
	audio_bitrate=""
	audio_codec=""
	audio_format=""
	while IFS="=" read name value
	do
		if [ "${name}" = "ID_VIDEO_WIDTH" -a "${x}" = "" ] ; then x="${value}" ; fi
		if [ "${name}" = "ID_VIDEO_HEIGHT" -a "${y}" = "" ] ; then y="${value}" ; fi
		if [ "${name}" = "ID_AUDIO_NCH" ] ; then if [ "${ch}" = "" ] ; then ch="${value}" ; elif [ "${ch}" -lt "${value}" ] ; then ch="${value}" ; fi ; fi
		if [ "${name}" = "ID_AUDIO_CODEC" -a "${audio_codec}" = "" ] ; then audio_codec="${value}" ; fi
		if [ "${name}" = "ID_AUDIO_FORMAT" -a "${audio_format}" = "" ] ; then audio_format="${value}" ; fi
		if [ "${name}" = "ID_VIDEO_FPS" -a "${fps}" = "" ] ; then fps="${value}" ; fi
		if [ "${name}" = "ID_VIDEO_ASPECT" -a "${s_aspect}" = "" ] ; then s_aspect="${value}" ; fi
		if [ "${name}" = "ID_AUDIO_RATE" -a "${audio_rate}" = "" ] ; then audio_rate="${value}" ; fi
		if [ "${name}" = "ID_AUDIO_BITRATE" -a "${audio_bitrate}" = "" ] ; then audio_bitrate="${value}" ; fi
	done < "${TEMP}" || true

	# Did we get the properties from the file?

	if [ "${audio_only}" = "" ]
	then
		if [ "${x}" = "" -o "${y}" = "" ]
		then
			message "ERROR: Cannot find video size for <${input}>. mplayer's error output will follow:"
			cat "${TEMP}" "${TEMP}".err >&2 || true
			return 1
		fi

		if [ "${fps}" != "" -a "${fps%.*}" -ge "100" ]
		then
			message "ERROR: Cannot convert movies with variable frame rates (yet). The reported framerate is ${fps} fps, which does not make sense."
			return 1
		fi
	else
		if [ "${ch}" = "" ]
		then
			message "ERROR: Cannot find audio properties for <${input}>. mplayer's error output will follow:"
			cat "${TEMP}" "${TEMP}".err >&2 || true
			return 1
		fi
	fi

	rm -f "${TEMP}"

	# Done

	return 0
}

###############################################################################
# A function to check filenames
###############################################################################

check_filenames()
{
	local	check_input

	for check_input
	do
		if [ "${check_input}" != "${check_input#-}" ]
		then
			message "ERROR: The filename <${check_input}> starts with a minus sign, which will cause problems with various programs. Please rename this file to something that does not start with a minus sign."
			return 1
		fi

		should_be_empty="`echo -n "${check_input}" | tr -d '[ -~]'`"
		if [ "${should_be_empty}" != "" ]
		then
			message "ERROR: The filename <${check_input}> contains at least one non-US-ASCII character that will cause problems with various programs. Please rename this file to something that contains only US-ASCII characters. The character(s) that will cause problems is/are <${should_be_empty}>."
			return 1
		fi

		should_be_empty="`echo -n "${check_input}" | tr -dc ':,\\\\'`"
		if [ "${should_be_empty}" != "" ]
		then
			message "ERROR: The filename <${check_input}> contains at least one character that will cause problems with various programs. Please rename this file to something that does not contain comma's, colons (:) or backslashes. The character(s) that will cause problems is/are <${should_be_empty}>."
			return 1
		fi
	done

	# No problematic filenames found
	return 0
}

# vim:ts=2:sw=2
