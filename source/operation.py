from enum import Enum


class Operation(Enum):
    INSERT = 1
    VIEW = 2
    UPDATE = 3
    REMOVE = 4
    QUIT = 0
