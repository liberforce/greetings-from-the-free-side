from enum import Enum, auto


class ProcessingStatus(Enum):
    UNDEFINED = auto()
    SKIPPED = auto()
    SUCCESS = auto()
    FAILURE = auto()
