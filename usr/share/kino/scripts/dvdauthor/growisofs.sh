#!/bin/sh
# A Kino script that invokes growisofs on a generated dvdauthor xml file.

DVD_DEVICE="${DVD_DEVICE:-/dev/dvd}"

usage()
{
	# Title
	echo "Title: Burn to $DVD_DEVICE with growisofs"

	# Usable?
	which dvdauthor > /dev/null && \
	which growisofs > /dev/null
	[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive
}

execute()
{
	xml="$1"
	output="$2"
	label=`basename "$2"`

	dvdauthor -o "$output" -x "$xml" && \
	growisofs -dvd-compat -Z "$DVD_DEVICE" -dvd-video -V "$label" "$output"
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
