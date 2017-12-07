#!/bin/sh
# A Kino script that invokes dvdauthor on a generated dvdauthor xml file.

usage()
{
	# Title
	echo "Title: Create DVD-Video (dvdauthor)"

	# Usable?
	which dvdauthor > /dev/null
	[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive
}

execute()
{
	xml="$1"
	output="$2"

	dvdauthor -o "$output" -x "$xml"
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
