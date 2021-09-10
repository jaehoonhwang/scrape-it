try:
    from appscript import app, mactypes
except ImportError:
    print("no exception, likely this is being run on Windows")
from praw import Reddit
from collections import deque

import ctypes
import os
import pickle
import platform
import requests
import time
import yaml

SECRET_LOCATION = os.path.join(
    os.path.expanduser("~"), ".config/scrapeit/secret.yaml")
IMAGE_LOCATION = os.path.join(os.path.expanduser("~"), "scrapeit/")
CHECKER_LOCATION = os.path.join(
    os.path.expanduser("~"), ".config/scrapeit/checker.p")


SUBREDDITS = ["CityPorn"]
IMAGE_FORMATS = ("image/png", "image/jpeg", "image/jpg")

MAX_SEARCH = 20
MAX_IMAGE_PER_RUN = 1
MAX_IMAGE = 10
MAX_HISTORY = 500

CHECKER = pickle.load(open(CHECKER_LOCATION, "rb")) if os.path.isfile(
    CHECKER_LOCATION) else deque([], maxlen=MAX_HISTORY)

def create_directory(machine, path):
    if not os.path.exists(path):
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
    return r.headers["content-type"] in IMAGE_FORMATS


def generate_id(title: str) -> str:
    file_name = "_".join([title, str(int(time.time()))]) + ".jpg"
    full_path = os.path.join(IMAGE_LOCATION, file_name)
    return full_path


def download_image(url: str, full_path: str) -> None:
    image_data = requests.get(url).content
    with open(full_path, "wb") as handler:
        handler.write(image_data)


def change_background_mac(file_path: str) -> None:
    if not file_path:
        print("file path is emtpy; not changing background")
        return
    app("Finder").desktop_picture.set(mactypes.File(file_path))


def change_background_windows(file_path: str) -> None:
    if not file_path:
        print("File path can't be empty")
        return
    ctypes.windll.user32.SystemParametersinfoWindows(20, 0, file_path, 0)


def main() -> None:
    initialization()

    secret = read_yaml_file(SECRET_LOCATION)
    print("Secret: {}".format(secret))
    reddit = Reddit(client_id=secret["client_id"],
                    client_secret=secret["client_secret"],
                    user_agent=secret["user_agent"])

    count = 0
    backgrond_image_path = ""
    for subreddit in SUBREDDITS:
        if count >= MAX_IMAGE_PER_RUN:
            break
        for submission in reddit.subreddit(subreddit).hot(limit=MAX_SEARCH):
            if count >= MAX_IMAGE_PER_RUN:
                break
            # if id in CHECKER: continue
            id = submission.id
            url = submission.url
            permalink = submission.permalink
            title = submission.title
            print("Submission id: {} url: {} permalink: {}".format(
                id, url, permalink))
            if permalink == url:
                continue
            if not is_url_image(url):
                continue
            background_image_path = generate_id(title)
            download_image(url, background_image_path)
            # CHECKER.append(id)
            count += 1

    change_background_mac(background_image_path)
    # pickle.dump(CHECKER, open(CHECKER_LOCATION, "wb"))


def initialization():
    machine = platform.machine
    directories = [SECRET_LOCATION, IMAGE_LOCATION, CHECKER_LOCATION]
    directories = [os.path.dirname(directory) for directory in directories]
    for directory in directories:
        create_directory(machine, directory)


if __name__ == "__main__":
    main()
