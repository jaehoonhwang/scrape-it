from scrapeit.data.site_type import SiteType

class SequencerInterface(object):
    """SequencerInterface."""

    def __init__(self, configuration_file : str = "", storage_directory : str = "", site_type : SiteType = SiteType.OTHER):
        """__init__.

        :param configuration_file:
        :type configuration_file: str
        :param storage_directory:
        :type storage_directory: str
        :param site_type:
        :type site_type: SiteType
        """
        self.configuration_file = configuration_file
        self.storage_directory= storage_directory
        self.site_type = site_type

    def authenticate(self):
        """authenticate."""
        raise NotImplementedError("Can't use this method without overriding")

    def browse(self):
        """browse."""
        raise NotImplementedError("Can't use this method without overriding")

    def save(self):
        """save."""
        raise NotImplementedError("Can't use this method without overriding")

    def filter(self):
        """filter."""
        raise NotImplementedError("Can't use this method without overriding")
