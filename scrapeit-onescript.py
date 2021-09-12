from PIL import ImageFile
from praw import Reddit
from collections import deque

import ctypes
import os
import pickle
import platform
import requests
import subprocess
import time
import urllib.request
import yaml

SECRET_LOCATION = os.path.join(
    os.path.expanduser("~"), ".config/scrapeit/secret.yaml")
IMAGE_LOCATION = os.path.join(os.path.expanduser("~"), "scrapeit/")
CHECKER_LOCATION = os.path.join(
    os.path.expanduser("~"), ".config/scrapeit/checker.p")


SUBREDDITS = ["CityPorn", "natureporn"]
FILENAME_SPEARATOR = "_"
IMAGE_FORMATS = ("image/png", "image/jpeg", "image/jpg")
IMAGE_FORMATS_EXT = (".png", ".jpeg", ".jpg")
IMAGE_RESOLUTION_MIN = (1680, 1050)
IMAGE_RESOLUTION_MAX = (float('inf'), float('inf'))

MAX_SEARCH = 20
MAX_IMAGE_PER_SUBREDDIT = 2
MAX_IMAGE = 20
MAX_HISTORY = 500

CHECKER = pickle.load(open(CHECKER_LOCATION, "rb")) if os.path.isfile(
    CHECKER_LOCATION) else deque([], maxlen=MAX_HISTORY)

APPLE_SCRIPT = """/usr/bin/osascript<<END
tell application "System Events"
    set desktopCount to count of desktops
    repeat with desktopNumber from 1 to desktopCount
        tell desktop desktopNumber
            set pictures folder to "%s"
            set picture rotation to 2 -- using interval
            set change interval to 300
            set random order to true
        end tell
    end repeat
end tell
END"""

def create_directory(path, **kwargs):
    if not os.path.exists(path):
        print("Path {} does not exist; attempting to create one".format(path))
        # create a directory
        os.makedirs(path)

    return


def read_yaml_file(file_path: str) -> dict[str, str]:
    with open(file_path, "r") as stream:
        try:
            output = yaml.safe_load(stream)
            return output
        except yaml.YAMLError as exception:
            print("Couldn't read configuration file: {}; something is wrong: {}".format(
                file_path, exception))
            raise RuntimeError(
                "Something went wrong while trying to read configuration file.")


def is_url_image(url: str) -> bool:
    r = requests.head(url)
    if "content_type" not in r.headers: return False
    return r.headers["content-type"] in IMAGE_FORMATS


def get_image_resolution(url : str):
    # https://tinyurl.com/2ez7uz65
    # get file size *and* image size (None if not known)
    file = urllib.request.urlopen(url)
    size = file.headers.get("content-length")
    if size: size = int(size)
    p = ImageFile.Parser()
    while True:
        data = file.read(1024)
        if not data:
            break
        p.feed(data)
        if p.image:
            return size, p.image.size
    file.close()
    return size, (-1, -1)

def generate_id(title: str) -> str:
    title = "".join([ch for ch in title if ch.isalpha()])
    title = "_".join(title.split("\s+"))
    file_name = FILENAME_SPEARATOR.join([str(int(time.time())), title]) + ".jpg"
    full_path = os.path.join(IMAGE_LOCATION, file_name)
    return full_path


def download_image(url: str, full_path: str) -> None:
    image_data = requests.get(url).content
    with open(full_path, "wb") as handler:
        handler.write(image_data)


def change_background_mac() -> None:
    script = APPLE_SCRIPT%IMAGE_LOCATION
    subprocess.Popen(script, shell=True)


def change_background_windows(file_path: str) -> None:
    if not file_path:
        print("File path can't be empty")
        return
    ctypes.windll.user32.SystemParametersinfoWindows(20, 0, file_path, 0)

def maintain_directory():
    files = [os.path.join(IMAGE_LOCATION, file)for file in os.listdir(IMAGE_LOCATION) 
             if os.path.isfile(os.path.join(IMAGE_LOCATION, file)) and
             any([ext in file for ext in IMAGE_FORMATS_EXT])]
    file_numbers = len(files)

    if file_numbers <= MAX_IMAGE:
        print("maintain_directory:: no Action needed since {} path contains {} files".format(IMAGE_LOCATION, file_numbers))
        return

    files = sorted(files)

    for delete_file in files[:MAX_IMAGE]:
        print("File: {} will be deleted".format(delete_file))
        os.remove(delete_file)

def main() -> None:
    system = platform.system()
    initialization(system=system)

    secret = read_yaml_file(SECRET_LOCATION)
    print("Secret: {}".format(secret))
    reddit = Reddit(client_id=secret["client_id"],
                    client_secret=secret["client_secret"],
                    user_agent=secret["user_agent"])

    for subreddit in SUBREDDITS:
        count = 0
        for submission in reddit.subreddit(subreddit).hot(limit=MAX_SEARCH):
            if count >= MAX_IMAGE_PER_SUBREDDIT:
                break
            id = submission.id
            title = submission.title
            if id in CHECKER: 
                print("Skipping id: {} and title: {}".format(id, title))
                continue
            url = submission.url
            permalink = submission.permalink
            print("Submission id: {} url: {} permalink: {}".format(
                id, url, permalink))
            if permalink == url:
                print("ignoring self-made post")
                continue
            if not is_url_image(url):
                print("ignoring non image link")
                continue
            _, image_resolution = get_image_resolution(url)
            if IMAGE_RESOLUTION_MIN[0] <= image_resolution[0] <= IMAGE_RESOLUTION_MAX[0] and \
                IMAGE_RESOLUTION_MIN[1] <= image_resolution[1] <= IMAGE_RESOLUTION_MAX[1]:
                background_image_path = generate_id(title)
                download_image(url, background_image_path)
                CHECKER.append(id)
                count += 1
            else:
                print("image has {}x{} resolution; does not meet resolution requirement".format(image_resolution[0], image_resolution[1]))

    change_background_mac()

    # CLEANUP
    pickle.dump(CHECKER, open(CHECKER_LOCATION, "wb"))
    maintain_directory()

def initialization(*args, **kwargs):
    directories = [SECRET_LOCATION, IMAGE_LOCATION, CHECKER_LOCATION]
    directories = [os.path.dirname(directory) for directory in directories]
    for directory in directories:
        create_directory(directory, **kwargs)


if __name__ == "__main__":
    main()
