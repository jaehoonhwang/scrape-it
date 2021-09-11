#!/bin/sh

echo "Cleaning up files to rest"

FILE=$HOME/.config/scrapeit/checker.p
if test -f "$FILE"; then
    echo "Removing pickle dump"
    echo "$FILE exists."
    rm $FILE
fi


