from abc import abstractmethod
from typing import Protocol

from src.core.errors import UnknownPilotException
from src.core.value_objects import PilotName
from src.pilot import Pilot


class PilotRepository(Protocol):
    @abstractmethod
    def find_by_name(self, pilot_name: PilotName) -> Pilot:
        pass

    @abstractmethod
    def add(self, pilot: Pilot) -> None:
        pass


class InMemoryPilotRepository:
    def __init__(self):
        self.__pilots = {}

    def find_by_name(self, pilot_name: PilotName) -> Pilot:
        if pilot_name not in self.__pilots:
            raise UnknownPilotException()
        return self.__pilots[pilot_name]

    def add(self, pilot: Pilot) -> None:
        self.__pilots[pilot.name] = pilot
