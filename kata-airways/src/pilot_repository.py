from abc import abstractmethod
from typing import Protocol

from src.core.value_objects import PilotName


class PilotRepository(Protocol):
    @abstractmethod
    def find_by_name(self, pilot_name: PilotName):
        pass


class InMemoryPilotRepository:
    def find_by_name(self, pilot_name: PilotName):
        raise NotImplementedError()
