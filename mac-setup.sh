#!/bin/sh

set -e

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

BOOTSTRAP_FILE="${SCRIPT_DIR}/bin/bootstrap-mac.sh"
PYTHON_VENV_TARGET="$HOME/.config/scrapeit/env/scrape-it"

echo $SCRIPT_DIR

echo "Running BOOTSTRAP script $BOOTSTRAP_FILE"

$BOOTSTRAP_FILE

echo "Creating Virutalenv for scrapeit"

DIRECTORY=$HOME/.config/scrapeit/env/scrape-it
if [ -d "$DIRECTORY" ]; then
    echo "$DIRECTORY exists."
else 
    echo "$DIRECTORY does not exist; setting up virtualenv"
    python3 -m venv $PYTHON_VENV_TARGET
fi

echo "Installing Dependencies"

$PYTHON_VENV_TARGET/bin/pip install -r $SCRIPT_DIR/requirements.txt

echo "Creating crontab file for periodic running of the script."

CRON_JOB="0 0 */3 * * $SCRIPT_DIR/mac-start.sh"

crontab -l > crontab_new || echo "" > crontab_new

echo "$CRON_JOB" >> crontab_new

crontab crontab_new

rm crontab_new

(crontab -l; echo "$CRON_JOB")|awk '!x[$0]++'|crontab -
