#!/bin/sh
# Simple shell script to populate the dock by setting up some standard applications.
DESKTOP_DIR="/usr/share/applications"

test -z ~/.kiba-dock/ || mkdir -p -- ~/.kiba-dock/
test -z ~/.kiba-dock/launcher/ || mkdir -p -- ~/.kiba-dock/launcher/

while read file; do
  if [ -e "$file" ] ; then
    printf "adding $file\n"
    cp $file ~/.kiba-dock/launcher/
  fi
done <<EOF
    $(ls $DESKTOP_DIR/gnome-terminal*.desktop)
    $(ls $DESKTOP_DIR/gimp-2.2*.desktop)
    $(ls $DESKTOP_DIR/epiphany*.desktop)
    $(ls $DESKTOP_DIR/gaim*.desktop)
    $(ls $DESKTOP_DIR/gnome-cd*.desktop)
    $(ls $DESKTOP_DIR/background*.desktop)
EOF
