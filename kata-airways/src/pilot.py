from src.core.value_objects import PilotName


class Pilot:
    def __init__(self, pilot_name: PilotName, worked_month_hours: float, worked_week_hours: float):
        self.name = pilot_name
        self.worked_month_hours: float = worked_month_hours
        self.worked_week_hours: float = worked_week_hours
