#!/bin/sh

mkdir -p $HOME/.config/scrapeit
mkdir -p $HOME/scrapeit

FILE=$HOME/.config/scrapeit/secret.yaml
if test -f "$FILE"; then
    echo "$FILE exists."
else 
    echo "$FILE does not exist."
    echo "client_id: <replace_me>\nclient_secret: <replace_me>\nuser_agent: <replace_me>" >> $HOME/.config/scrapeit/secret.yaml
fi

LOG_OUTPUT=$HOME/.config/scrapeit/log/

echo "CREATING LOG FOLDER AT $LOG_OUTPUT"

mkdir -p $LOG_OUTPUT
