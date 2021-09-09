
class RedditSecret(object):
    def __init__(self, client_id : str, client_secret : str, user_agent : str) -> None:
        self.client_id = client_id
        self.client_secret = client_secret
        self.user_agent = user_agent
