#!/bin/sh
# A Kino script that invokes qdvdauthor on a generated dvdauthor xml file.

usage()
{
	# Title
	echo "Title: Open in 'Q' DVD-Author"

	# Usable?
	which qdvdauthor > /dev/null
	[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive
}

execute()
{
	xml="$1"
	output="$2"

	qdvdauthor -a -d "$xml" &
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
