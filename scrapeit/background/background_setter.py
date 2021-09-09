from scrapeit.data.operating_system import OperatingSystem, OperatingArchitecture
import platform

class BackgroundSystem(object):

    ALLOWED_OS = [OperatingSystem.WINDOWS, OperatingSystem.MAC]
    ALLOWED_MACHINE = [OperatingArchitecture.AMD64]

    def __init__(self) -> None:
        self.system = ""
        self.machine = ""

    def determine_platform(self) -> str:
        self.system = OperatingSystem(platform.system())
        self.machine = OperatingArchitecture(platform.machine())

    def handle(self) -> None:
        if self.system not in self.ALLOWED_OS or self.machine not in self.ALLOWED_MACHINE:
            raise RuntimeError("Current OS: {} or Architecture: {}is not supported with Scrapeit".format(
                self.system, self.machine))
        