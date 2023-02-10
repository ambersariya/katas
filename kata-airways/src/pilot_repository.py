import random
from abc import abstractmethod
from typing import Protocol

from src.core.errors import UnknownPilotException
from src.pilot import Pilot, MAX_FLYING_HOURS_MONTH, MAX_FLYING_HOURS_WEEK


class PilotRepository(Protocol):
    @abstractmethod
    def find_by_name(self, pilot_name: str) -> Pilot:
        pass

    @abstractmethod
    def add(self, pilot: Pilot) -> None:
        pass

    @abstractmethod
    def find_by_availability(self, limit: int = 2) -> list[Pilot]:
        pass


class InMemoryPilotRepository:
    def __init__(self):
        self.__pilots = {}

    def find_by_name(self, pilot_name: str) -> Pilot:
        if pilot_name not in self.__pilots:
            raise UnknownPilotException()
        return self.__pilots[pilot_name]

    def add(self, pilot: Pilot) -> None:
        self.__pilots[pilot.name] = pilot

    def find_by_availability(self, limit: int = 2) -> list[Pilot]:
        pilots = self.__pilots.values()

        # Less than 100 hours in month
        found_pilots = [pilot for pilot in pilots if pilot.worked_month_hours < MAX_FLYING_HOURS_MONTH]

        # Less than 30 hours in week
        found_pilots = [pilot for pilot in found_pilots if pilot.worked_week_hours < MAX_FLYING_HOURS_WEEK]

        random.shuffle(found_pilots)

        return found_pilots
