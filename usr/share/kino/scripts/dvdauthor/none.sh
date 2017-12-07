#!/bin/sh
# A Kino script that does nothing with a generated dvdauthor xml file.

usage()
{
	# Title
	echo "Title: Author only"

	# Usable?
	echo Status: Active
}

execute()
{
	xml="$1"
	output=`dirname "$2"`
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
