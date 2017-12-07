#!/bin/sh
# A Kino script that tries to convert anything to raw pcm audio for Dub and Mix

file="$1"

if [ "${file%ogg}" = "$file" ]
then exec ffmpeg -i "$file" -f s16le -ar 44100 -ac 2 -
else exec oggdec "$file" -o - | ffmpeg -i - -f s16le -ar 44100 -ac 2 -
fi
