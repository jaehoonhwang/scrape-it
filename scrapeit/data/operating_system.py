from typing import Any

import enum

class OperatingSystem(enum.Enum):
    MAC = "Darwin"
    WINDOWS = "Windows"
    DEFAULT = "Other"

    @classmethod
    def _missing_(cls, value: object) -> Any:
        return OperatingSystem.DEFAULT

class OperatingArchitecture(enum.Enum):
    AMD64 = "AMD64"
    DEFAULT = "NOT_SUPPORTED"

    @classmethod
    def _missing_(cls, value: object) -> Any:
        return OperatingArchitecture.DEFAULT