#!/bin/sh

set -e

LOG_OUTPUT=$HOME/.config/scrapeit/log/

cat $LOG_OUTPUT/"$(ls -1rt $LOG_OUTPUT | tail -n 1)"
