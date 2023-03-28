import dataclasses
from enum import StrEnum


class RoomType(StrEnum):
    DOUBLE = 'Double'
    STANDARD = 'standard'


@dataclasses.dataclass(init=True)
class Room:
    number: int
    type: RoomType


@dataclasses.dataclass(eq=True)
class Hotel:
    def __init__(self, id: str, name: str):
        self.__name = name
        self.__id = id

    @property
    def id(self) -> str:
        return self.__id

    @property
    def name(self) -> str:
        return self.__name

    def add_room(self, room: Room) -> None:
        pass
