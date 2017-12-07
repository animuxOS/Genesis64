#!/bin/sh
#
# A Kino publishing script to upload to http://blip.tv as Ogg Theora
# Copyright (C) 2007 Dan Dennedy <dan@dennedy.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.
#

POST_URL='http://blip.tv/'
EDIT_URL='http://blip.tv/file/post/'

getXmlAttributeValue()
{
	attribute="$1"
	filename="$2"
	echo "$@" | awk "
		/${attribute}=\"/ {
			split(\$0, x, \"\\\"\");
			z = 0;
			for (y in x) {
				if (x[y] ~ /${attribute}=/) {
					z = y + 1;
					print x[z];
					exit
				}
			}
		}
	" "$filename"
}

getBlipTvId()
{
	echo "$@" | awk '
		BEGIN { FS = ">" }
		/item_id/ { print int($2) }
	'
}

project_file="$1"
browser="$2"

path=$(dirname "$project_file")
base=$(basename "$project_file" '.kino')
base=$(basename "$base" '.smil')
base=$(basename "$base" '.xml')
ogg_file="${path}/${base}.ogg"

echo Login to blip.tv
read -p "  Username: " username
stty -echo
read -p "  Password: " password
echo
stty echo

title=$(getXmlAttributeValue 'title' "$project_file")
[ -z "$title" ] && title="Untitled"
author=$(getXmlAttributeValue 'author' "$project_file")
[ -z "$author" ] && author="Anonymous"
abstract=$(getXmlAttributeValue 'abstract' "$project_file")
copyright=$(getXmlAttributeValue 'copyright' "$project_file")
copyright=$(echo $copyright | awk '{print int($0)}')
[ -z "$copyright" ] || [ "$copyright" = "0" ] && copyright="-1"

echo
echo Transcoding "$project_file"
echo to "$ogg_file"
aspect=$(kino2raw "$project_file" aspect)
normalisation=$(kino2raw "$project_file" normalisation)
if [ "$aspect" = "16:9" ]; then
	if [ "$normalisation" = "pal" ]; then
		full_res_x="1024"
		full_res_y="576"
		med_res_x="512"
		med_res_y="288"
	else
		full_res_x="856"
		full_res_y="480"
		med_res_x="424"
		med_res_y="240"
	fi
else
	if [ "$normalisation" = "pal" ]; then
		full_res_x="768"
		full_res_y="576"
		med_res_x="384"
		med_res_y="288"
	else
		full_res_x="640"
		full_res_y="480"
		med_res_x="320"
		med_res_y="240"
	fi
fi
kino2raw "$project_file" |
	ffmpeg2theora -f dv -p preview --deinterlace -o "$ogg_file" --artist "$author" --title "$title" --location "$abstract" -
	# Example of custom output
	# ffmpeg2theora -f dv --aspect "$aspect" --deinterlace -x $full_res_x -y $full_res_y -K 200 -v 5 -S 2 -a 2 -o "$ogg_file" --artist "$author" --title "$title" --location "$abstract" -

echo
echo Uploading to blip.tv
curl_file="file=@${ogg_file};type=application/ogg"
result=$(curl -F "$curl_file" \
	-F "skin=api" -F "section=file" -F "cmd=post" -F "post=1" \
	-F "userlogin=$username" \
	-F "password=$password" \
	-F "title=$title" \
	-F "description=$abstract" \
	-F "license=$copyright" \
	"$POST_URL")
echo
post_id=$(getBlipTvId "$result")
if [ -n "$post_id" ]; then
	echo 'Close the window when you are finished editing your post.'
	echo
	$browser "${EDIT_URL}${post_id}/"
else
	echo $result
	echo 'Close the window when you are finished reading this error.'
fi
read
