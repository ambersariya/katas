from abc import abstractmethod
from typing import Protocol

from src.core.value_objects import PilotName
from src.pilot import Pilot


class PilotRepository(Protocol):
    @abstractmethod
    def find_by_name(self, pilot_name: PilotName) -> Pilot:
        pass

    @abstractmethod
    def save(self, pilot: Pilot) -> None:
        pass


class InMemoryPilotRepository:
    def find_by_name(self, pilot_name: PilotName) -> Pilot:
        raise NotImplementedError()

    def save(self, pilot: Pilot) -> None:
        raise NotImplementedError()
