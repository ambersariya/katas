from src.core.errors import PilotFlyingHoursExceeded
from src.core.value_objects import Route, PilotName
from src.flight import FlightPairing
from src.pilot_repository import PilotRepository

MAX_FLYING_HOURS_MONTH = 100
MAX_FLYING_HOURS_WEEK = 30


class PilotService:
    def __init__(self, pilot_repository: PilotRepository):
        self.__pilot_repository = pilot_repository

    def generate_pairing(self, pilots: list[PilotName], route: Route) -> FlightPairing:
        captain = self.__pilot_repository.find_by_name(pilot_name=pilots[0])
        copilot = self.__pilot_repository.find_by_name(pilot_name=pilots[1])

        if captain.worked_month_hours >= MAX_FLYING_HOURS_MONTH \
                or copilot.worked_month_hours >= MAX_FLYING_HOURS_MONTH:
            raise PilotFlyingHoursExceeded()

        if captain.worked_week_hours >= MAX_FLYING_HOURS_WEEK \
                or copilot.worked_week_hours >= MAX_FLYING_HOURS_WEEK:
            raise PilotFlyingHoursExceeded()

        captain.worked_month_hours += route.duration
        copilot.worked_month_hours += route.duration

        self.__pilot_repository.save(pilot=captain)
        self.__pilot_repository.save(pilot=copilot)

        return FlightPairing(captain=captain, co_pilot=copilot)
