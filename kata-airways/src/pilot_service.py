from src.core.errors import InsufficientPilotsException
from src.core.value_objects import Route
from src.flight import FlightPairing
from src.pilot_repository import PilotRepository


class PilotService:
    def __init__(self, pilot_repository: PilotRepository):
        self.__pilot_repository = pilot_repository

    def generate_pairing(self, route: Route) -> FlightPairing:
        available_pilots = self.__pilot_repository.find_by_availability()
        if len(available_pilots) == 0:
            raise InsufficientPilotsException()
        captain, copilot = available_pilots

        # if (captain.worked_month_hours + route.duration) >= MAX_FLYING_HOURS_MONTH \
        #         or (copilot.worked_month_hours + route.duration) >= MAX_FLYING_HOURS_MONTH:
        #     raise PilotFlyingHoursExceeded()
        #
        # if (captain.worked_week_hours + route.duration) >= MAX_FLYING_HOURS_WEEK \
        #         or (copilot.worked_week_hours + route.duration) >= MAX_FLYING_HOURS_WEEK:
        #     raise PilotFlyingHoursExceeded()

        # captain.worked_month_hours += route.duration
        # copilot.worked_month_hours += route.duration

        self.__pilot_repository.add(pilot=captain)
        self.__pilot_repository.add(pilot=copilot)

        return FlightPairing(captain=captain, co_pilot=copilot)
