# Scrape it 

Are you tired of downloading images off Reddit and setting it to your desktop wallpaper?

Look no further, here is a script that does that for you! (*Only if you are mac user.*)

Supports Resolution and multiple subreddits.

Also, runs by itself every 3 days*

## Pre-requisite

* Only on Mac (Tested on Catalina)
* Python 3.7+ (I think, i have used 3.9, but should work with 3.7)

## How to use it?

1. Create a reddit account and and create an app and get two things and make up something for user-agent:
  * `client_id`
  * `client_secret`
  * `user-agent` Something like `scrapeit <username>`
2. Run `./mac-setup.sh`; this should does following:
  * Configuration folder under `$HOME/.config/scrapeit`
  * Image folder under `$HOME/scrapeit`
  * Secret file under `$HOME/.config/scrapeit/secret.yaml`
  * Log folder under `$HOME/.config/scrapeit/log/`
  * Python virtual environment under `$HOME/scrapeit/env/scrapeit` and its dependencies
  * Cronjob Configuration running every 3 days.
3. Should be good to go

## CONFIGURATION CHANGES

Not easily configurable since this was created very quick; but following should be in your mind if you were to fork this.

Lots of configurations with this script.

`scrapeit-onescript.py`
* `SUBREDDITS` ; without `/r` just the name of subreddit
* `IMAGE_RESOLUTION_MIN`; if you don't care about resolution use this `(float('-inf'), float('-inf'))
* `IMAGE_RESOLUTION_MAX`; if you don't care about resolution use this `(float('inf'), float('inf'))
* `MAX_SEARCH`
* `MAX_IMAGE_PER_SUBREDDIT` this is per run; 2 subreddits means 4 images per run
* `MAX_IMAGE` this is overall files numbers in directory; if script sees more than `MAX_IMAGE` it will delete oldest one first
* `MAX_HISTORY` The script is using pickle to ignore reddit submission that has been searched before; this should be able to go about a million before mac goes boom boom;

### CONFIGURATION CHANGES: Moving image folder

If you are lazy just do this;
1. Create a folder that you want
2. Change `IMAGE_LOCATION` line in `scrapeit-onescript.py`

### CONFIGURATION CHANGES: Cron job; period changes

Currently, the script, `mac-setup.sh` is only looking for 3 day configuartion when de-duping; if you want more frequent or lazier cron configuration; you need to remove the entry in `crontab` and then change `CRON_JOB` variable in `mac-setup.sh`

