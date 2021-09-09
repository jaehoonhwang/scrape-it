from typing import Dict

from scrapeit.data.secret.reddit import RedditSecret

class Secret(object):
    def __init__(self, version : str, reddit_secret : RedditSecret) -> None:
        self.version = version
        self.reddit_secret = RedditSecret
