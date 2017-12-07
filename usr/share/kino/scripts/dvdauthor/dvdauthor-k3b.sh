#!/bin/sh
# A Kino script that invokes K3B on a generated dvdauthor xml file.

usage()
{
	# Title
	echo "Title: Burn with K3B"

	# Usable?
	which dvdauthor > /dev/null && which k3b > /dev/null
	[ $? -eq 0 ] && echo Status: Active || echo Status: Inactive
}

execute()
{
	xml="$1"
	output="$2"

	dvdauthor -o "$output" -x "$xml" && \
	k3b --videodvd "$output"/*
}

[ "$1" = "--usage" ] || [ -z "$1" ] && usage "$@" || execute "$@"
