from scrapeit.data.configuration.authentication import Authentication
from scrapeit.data.configuration.general import General
from scrapeit.data.configuration.interval import Interval
from scrapeit.data.configuration.locations import Locations

class Configuration(object):

    def __init__(self, version : str, general : General, authentication : Authentication,
                 locations : Locations, interval : Interval) -> None:
        self.version = version
        self.general = general
        self.authentication = authentication
        self.locations = locations
        self.interval = interval
