import platform
import struct
import ctypes

from scrapeit.data.operating_system import OperatingArchitecture
from scrapeit.background.background_handler import BackgroundHandler

class WindowsBackgroundHelper(BackgroundHandler):

    ARCHITECTURE_32 = []
    ARCHITECTURE_64 = [OperatingArchitecture.AMD64]

    def __init__(self, storage_path : str, machine : OperatingArchitecture) -> None:
        super.__init__(self, storage_path)
        self.machine = machine

    def change_background(self):
        pass