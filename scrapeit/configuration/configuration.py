from types import Iterator, Any
import yaml

class ConfigurationLoader(object):
    """ConfigurationLoader."""

    def __init__(self, file_location : str = ""):
        """__init__.

        :param file_location:
        :type file_location: str
        """
        self.file_location = file_location
        self.configurations = None

    def read_configuration_file(self) -> Iterator[Any]:
        """read_configuration.

        :rtype: Iterator[Any]
        """
        with open(self.file_location, "r") as stream:
            try:
                output = yaml.safe_load_all(stream)
                return output
            except yaml.YAMLError as exception:
                print("Couldn't read configuration file: {}; something is wrong: {}".format(
                    self.file_location, exception))
                raise RuntimeError("Something went wrong while trying to read configuration file.")

    def get_configurations(self) -> Iterator[Any]:
        """get_configurations.

        Lazy load configurations

        """
        if self.configurations is None:
            self.configurations = self.read_configuration_file()
        return self.configurations

    def write_configuration_file(self) -> None:
        """write_configuration_file.

        :rtype: None
        """
        with open(self.file_location, "w") as stream:
            try:
                yaml.safe_dump_all(stream)
            except yaml.YAMLError as exception:
                print("Couldn't rwrite configuration file: {} exception: {}".format(
                    self.file_location, exception))
                raise RuntimeError("Something went wrong while trying to read configuration file.")
