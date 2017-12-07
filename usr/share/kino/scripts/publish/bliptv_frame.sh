#!/bin/sh
#
# A Kino publishing script to upload to http://blip.tv as photo
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

getBlipTvId()
{
	echo "$@" | awk '
		BEGIN { FS = ">" }
		/item_id/ { print int($2) }
	'
}

image_file="$1"
title="$2"
browser="$3"
[ -z "$title" ] && title="Untitled"

echo Login to blip.tv
read -p "  Username: " username
stty -echo
read -p "  Password: " password
echo
stty echo

echo
echo Uploading to blip.tv
curl_file=""
result=$(curl -F "file=@${image_file}" -F "thumbnail=@${image_file}" \
	-F "skin=api" -F "section=file" -F "cmd=post" -F "post=1" \
	-F "userlogin=$username" \
	-F "password=$password" \
	-F "title=$title" \
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
