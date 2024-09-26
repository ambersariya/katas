import pytest
from legacy_code_air_traffic import air_traffic_control_system


@pytest.mark.parametrize("flight_number, aircraft_type, scheduled_time, current_time, weather, emergency, expected_decision, expected_runway, expected_instructions", [
    ("FL123", "commercial", 1200, 1200, "clear", None, "On-Time Landing", "Runway 1", ["Approach Runway 1 from the north", "Maintain altitude until further notice"]),
    ("FL124", "commercial", 1200, 1231, "clear", None, "Expedite Landing", "Runway 1", ["Approach Runway 1 from the north", "Maintain altitude until further notice"]),
    ("FL125", "commercial", 1200, 1231, "stormy", None, "Expedite Landing", "Runway 1", ['Contact alternate control for landing instructions',
                                                                                         'Approach Runway 1 from the north',
                                                                                         'Maintain altitude until further notice']),
    ("FL126", "cargo", 1200, 1301, "clear", None, "Expedite Landing", "Runway 2", ["Approach Runway 2 from the north", "Maintain altitude until further notice"]),
    ("FL127", "cargo", 1200, 1200, "clear", None, "Hold for schedule adjustment", "Runway 3", ["Adjust schedule for cargo loading/unloading", "Approach Runway 3 from the north", "Maintain altitude until further notice"]),
    ("FL128", "large", 1200, 1200, "stormy", None, "Delayed Landing", "Runway 4", ["Approach Runway 4 from the north", "Maintain altitude until further notice"]),
    ("FL129", "small", 1200, 1200, "stormy", None, "Divert to alternate airport", None, ["Contact alternate control for landing instructions"]),
    ("FL130", "large", 1200, 1200, "clear", "medical", "Priority Landing", "Runway 1", ["Clear all paths for FL130"]),
    ("FL131", "large", 1200, 1200, "clear", "mechanical", "Immediate Landing", "Runway 2", ["Clear all paths for FL131"]),
])

def test_air_traffic_control_system(flight_number, aircraft_type, scheduled_time, current_time, weather, emergency, expected_decision, expected_runway, expected_instructions) -> None:
    decision, runway, instructions = air_traffic_control_system(flight_number, aircraft_type, scheduled_time, current_time, weather, emergency)
    assert decision == expected_decision
    assert runway == expected_runway
    assert instructions == expected_instructions
