#!/bin/sh

echo "Cleaning up files to rest"

FILE=$HOME/.config/scrapeit/checker.p
if test -f "$FILE"; then
    echo "Removing pickle dump"
    echo "$FILE exists."
    rm $FILE
fi

PYTHON_VENV_TARGET="$HOME/.config/scrapeit/env/scrape-it"
if [-d $PYTHON_VENV_TARGET]; then
    echo "Virtual Environment exists; deleting it"
    rm -rf $PYTHON_VENV_TARGET
fi

