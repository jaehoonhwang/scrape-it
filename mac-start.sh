#!/bin/sh

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
OUTPUT_LOG="$HOME/.config/scrapeit/log"
PYTHON_VENV_TARGET="$HOME/.config/scrapeit/env/scrape-it"
LOG_FILE="$(date +%s).log"

echo "" >> $OUTPUT_LOG/$LOG_FILE

echo "RUNNING SCRIPT"
$PYTHON_VENV_TARGET/bin/python $SCRIPT_DIR/scrapeit-onescript.py &> $OUTPUT_LOG/$LOG_FILE

