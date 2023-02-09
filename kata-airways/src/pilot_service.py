from src.core.value_objects import Route, PilotName
from src.flight import FlightPairing
from src.pilot_repository import PilotRepository


class PilotService:
    def __init__(self, pilot_repository: PilotRepository):
        self.__pilot_repository = pilot_repository

    def generate_pairing(self, pilots: list[PilotName], route: Route) -> FlightPairing:
        captain = self.__pilot_repository.find_by_name(pilot_name=pilots[0])
        copilot = self.__pilot_repository.find_by_name(pilot_name=pilots[1])

        return FlightPairing(captain=captain, co_pilot=copilot)
