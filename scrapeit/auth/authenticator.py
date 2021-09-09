
class Authenticator(object):
    """Authenticator."""

    def __init__(self) -> None:
        """__init__.

        :rtype: None
        """
        self.secrets = []

    def get_secrets(self, file):
        """get_secrets.

        :param file:
        """
        raise NotImplementedError("Can't use the base method!")

    def authenticate(self):
        """authenticate."""
        raise NotImplementedError("Can't use the base method!")
