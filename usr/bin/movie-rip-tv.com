#!/bin/sh

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

# Botch on errors
set -e

##############################################################################
# Load the function library
##############################################################################

prefix="/usr"
exec_prefix="${prefix}"
datadir="${prefix}/share"
bindir="${exec_prefix}/bin"

. "${datadir}/videotrans/library.sh"

##############################################################################
# Usage definition
##############################################################################

usage()
{
	echo "Usage: ${0##*/} -n series_name -s season -e episode" >&2
	echo "" >&2
	echo "-n series_name	Specifies the name of the series" >&2
	echo "-s season	Specify which season we want" >&2
	echo "-e episode	Specify which episode we want" >&2
	echo "" >&2
	exit 1
}

##############################################################################
# Temporary file name
##############################################################################

TEMP="/tmp/.video-tv.com.$$"
trap "rm -fr ${TEMP}* 2>/dev/null || :" EXIT

##############################################################################
# Cache directory name
##############################################################################

CACHE="${HOME}/.videotrans-tv.com-cache"
mkdir -- "${CACHE}" 2>/dev/null || :

##############################################################################
# Process the options
##############################################################################

series_name=""
season=""
episode=""
while getopts "n:s:e:" option
do
	case "${option}"
	in
		n)
			series_name="${OPTARG}"
			;;
		s)
			season="${OPTARG}"
			;;
		e)
			episode="${OPTARG}"
			;;
		*)
			usage
			;;
	esac
done

##############################################################################
# Get rid of all the parameters
##############################################################################

shift "`expr ${OPTIND} - 1`"

##############################################################################
# Any more arguments?
##############################################################################

[ "$#" -eq 0 ] || usage

##############################################################################
# Clean up any numbers by removing any leading zeroes in them
##############################################################################

while true
do
	case "${season}"
	in
		'0'*)
			season="${season#0}"
			;;
		*)
			break
			;;
	esac
done

while true
do
	case "${season}"
	in
		'0'*)
			season="${season#0}"
			;;
		*)
			break
			;;
	esac
done

while true
do
	case "${episode}"
	in
		'0'*)
			episode="${episode#0}"
			;;
		*)
			break
			;;
	esac
done

##############################################################################
# Did we get all the necessary parameters?
##############################################################################

[ "${series_name}" != "" ] || usage
[ "${season}" != "" ] || usage
[ "${episode}" != "" ] || usage

##############################################################################
# "Search" for the series name in tv.com
##############################################################################

web_series_name="`uriescape "${series_name}"`"
simple_series_name="`echo "${series_name}" | tr '[A-Z]' '[a-z]' | tr -dc '[a-z]'`"
cache_name="${CACHE}/homepage.${simple_series_name}"
if [ -s "${cache_name}" ]
then
	new_url="`cat "${cache_name}"`"
else
	message "Searching for series homepage at tv.com and caching the location afterwards"

	tries=20
	while [ "${tries}" -gt 0 ]
	do
		lynx -delay=0 -source "http://www.tv.com/search.php?type=11&stype=program&qs=${web_series_name}" | tr -d '' > "${TEMP}"
		if [ -s "${TEMP}" ]
		then
			break
		fi
		tries="`expr ${tries} - 1 || :`"
		if [ "${tries}" -gt 0 ]
		then
			message "Searching temporarily failed, retrying (${tries} tries left)..."
			sleep 1
		fi
	done

	# This is a page that lists a few possibilities that match the series name

	new_url=""
	grep -i -- '^[ 	]*<a class="default-image" href="[^"]*">$' < "${TEMP}" | while IFS='<">' read nothing a_class default_image href url nothing rest
	do
		echo "${url%?q=*}"
	done > "${TEMP}.2"
	new_url="`cat ${TEMP}.2 2>/dev/null || :`"
	if [ "${new_url}" = "" ]
	then
		grep -i -- '^[ 	]*<a href="[^"]*"[^>]*>.*'"${series_name}"'.*</a>' < "${TEMP}" | while IFS='<">' read nothing a_href url name rest
		do
			echo "${url%?q=*}"
			break
		done > "${TEMP}.2"
		new_url="`cat ${TEMP}.2 2>/dev/null || :`"
	fi
	if [ "${new_url}" != "" ]
	then
		echo "${new_url}" > "${cache_name}"
	fi
fi

##############################################################################
# Did we find the series homepage?
##############################################################################

if [ "${new_url}" = "" ]
then
	message "ERROR: Failed to find the series homepage on tv.com"
	rm "${TEMP}"* 2>/dev/null || :
	exit 1
fi

##############################################################################
# Print some stuff
##############################################################################

message "Series homepage is at ${new_url}"
eplist="${new_url%summary.html*}episode_listings.html&season=${season}"

##############################################################################
# Fetch the episode list
##############################################################################

while true
do
	cache_name="${CACHE}/episode_list.${simple_series_name}.season${season}"
	if [ -s "${cache_name}" ]
	then
		message "Using episode list cache for season ${season}"
		cp "${cache_name}" "${TEMP}"
		used_cache="yes"
	else
		message "Fetching tv.com's episode list for season ${season} and caching it for future use afterwards"
		lynx -delay=0 -source "${eplist}" | tr -d '' > "${TEMP}"
		cp "${TEMP}" "${cache_name}"
		used_cache="no"
	fi

	found_episode=0
	new_url=""
	while read -r line
	do
		case "${line}"
		in
			*'<a href="http://www.tv.com/'*'/episode/'*'/summary.html'*'">'*'</a>')
				found_episode="`expr ${found_episode} + 1`"
				new_url="`echo "${line}" | sed -e 's,.*<a href=",,g' -e 's,">.*,,g'`"
				;;
		esac
		if [ "${found_episode}" = "${episode}" ]
		then
			break
		fi
	done < "${TEMP}"

	if [ "${found_episode}" != "${episode}" -a "${used_cache}" = "yes" ]
	then
		message "The cache for season ${season} is out-of-date, removing it so that it will be downloaded again."
		rm "${cache_name}"
		continue
	fi
	break
done

if [ "${new_url}" = "" ]
then
	message "Could not find information on season ${season}, episode ${episode}"
	exit 1
fi

##############################################################################
# Fetch the episode summary
##############################################################################

message "Fetching information on season ${season}, episode ${episode} from URL: ${new_url}"
lynx -delay=0 -source "${new_url}" | tr -d '' > "${TEMP}"

##############################################################################
# Get information from the episode's summary page
##############################################################################

cleanup_html()
{
	sed -e 's,[ 	][ 	]*, ,g' \
		-e 's,^[ 	]*,,' -e 's,[ 	]*$,,' \
		-e 's/,\&nbsp;//g' \
		-e 's,\&nbsp;, ,g' \
		-e 's,\&quot;,",g' \
		-e 's,\&apos;,'\'',g' \
		-e 's,\&lt;,<,g' \
		-e 's,\&gt;,<,g' \
		-e 's,“,`,g' \
		-e "s,”,',g" \
		-e 's,\&amp;,\&,g' -e 's,\&#38;,\&,g'
}

remove_html()
{
	sed -e 's,<br>,\
,g' -e 's,<br />,\
,g' -e 's,<[^>]*>,,g'
}

title="`grep -i '[	 ]<h1>.*</h1>' < "${TEMP}" | head -1 | sed -e 's,^.*<h1>*,,' -e 's,</h1>.*,,' | cleanup_html`"
message "Gathering information for episode <${title}>"

episode_number="`grep -i '<span class="f-bold f-666">Episode Number: ' < "${TEMP}" | sed -e 's,^.*<span class="f-bold f-666">Episode Number: ,,' -e 's, .nbsp;.nbsp; Season Num.*,,'`"

first_aired="`grep '.nbsp;.nbsp; First Aired:' < "${TEMP}" | sed -e 's,^.*.nbsp;.nbsp; First Aired: ,,' -e 's,.nbsp;.nbsp; Prod Code:.*$,,'`"

production_code="`grep '.nbsp;.nbsp; Prod Code:' < "${TEMP}" | sed -e 's,^.*.nbsp;.nbsp; Prod Code: ,,' -e 's,</span>.*$,,'`"

writers="`grep -A 3 'Writer:$' < "${TEMP}" | tail -1 | remove_html | cleanup_html`"

director="`grep -A 3 'Director:$' < "${TEMP}" | tail -1 | remove_html | cleanup_html`"

story="`grep -A 3 'Story:$' < "${TEMP}" | tail -1 | remove_html | cleanup_html`"

guest_stars="`grep -A 3 'Guest Star:$' < "${TEMP}" | tail -1 | remove_html | cleanup_html`"

recurring_role="`grep -A 3 'Recurring Role:$' < "${TEMP}" | tail -1 | remove_html | cleanup_html`"

stars="`grep -A 3 '    Star:$' < "${TEMP}" | tail -1 | remove_html | cleanup_html`"

synopsis="`grep -A 3 '<div id="main-col">$' < "${TEMP}" | tail -1 | remove_html | cleanup_html`"
case "${synopsis}"
in
	*[!\ \	]*)
		;;
	*)
		synopsis="`grep -A 9 '<div id="main-col">$' < "${TEMP}" | tail -1 | remove_html | cleanup_html`"
		;;
esac

echo "" >&2

##############################################################################
### Dump information
##############################################################################

dump()
{
	dump_title="$1"
	eval echo "\"\${$2}\"" |
	{
		blankline="no"
		first="yes"
		seen_title="no"
		while read -r line
		do
			case "${line}"
			in
				'')
					if [ "${blankline}" = "no" -a "${first}" = "no" ]
					then
						echo ""
						blankline="yes"
					fi
					;;
				*)
					if [ "${seen_title}" = "no" ]
					then
						echo "${dump_title}"
						echo ""
						seen_title="yes"
					fi
					echo "    ${line}" | LC_ALL="en_US.ISO8859-15" fmt -w 60
					blankline="no"
					first="no"
					;;
			esac
		done
		if [ "${seen_title}" = "yes" ]
		then
			echo ""
		fi
	}
}

dump_list()
{
	sed 's/[ 	]*/\
/g' | while IFS='' read -r line
	do
		echo -n "${line}" | fmt -w 56 |
		{
			IFS='' read -r line2
			echo "    ${line2}"
			while IFS='' read -r line2
			do
				echo "        ${line2}"
			done
		}
	done
	echo ""
}

echo "${title}"
echo "#ffff00 Title:"
echo "    ${title}"
echo ""
echo "#ff00ff Episode number:"
echo "    ${episode_number} (season ${season}, episode ${episode})"
if [ "${first_aired}" != "" ]
then
	echo "#ff00ff First aired:"
	echo "    ${first_aired}"
fi
if [ "${production_code}" != "" ]
then
	echo "#ff00ff Production code:"
	echo "    ${production_code}"
fi
echo ""

case "${writers}"
in
	'')
		;;
	*''*)
		echo "#ff0000 Writers:"
		echo -n "${writers}" | dump_list
		;;
	*)
		echo "#ff0000 Writer:"
		echo -n "${writers}" | dump_list
		;;
esac

if [ "${story}" != "" ]
then
	echo "#ff0000 Story:"
	echo -n "${story}" | dump_list
fi

case "${director}"
in
	'')
		;;
	*''*)
		echo "#ff0000 Directors:"
		echo -n "${director}" | dump_list
		;;
	*)
		echo "#ff0000 Director:"
		echo -n "${director}" | dump_list
		;;
esac

if [ "${guest_stars}" != "" ]
then
	echo "#ff0000 Guest stars:"
	echo -n "${guest_stars}" | dump_list
fi

if [ "${recurring_role}" != "" ]
then
	echo "#ff0000 Recurring roles:"
	echo -n "${recurring_role}" | dump_list
fi

if [ "${stars}" != "" ]
then
	echo "#ff0000 Stars:"
	echo -n "${stars}" | dump_list
fi

dump "#ff0000 Synopsis:" synopsis

exit 0

# vim:ts=2:sw=2
