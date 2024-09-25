from typing import List, Tuple

Decision = Tuple[str, str, List[str]]

def air_traffic_control_system(
        flight_number, aircraft_type, scheduled_time, current_time, weather, emergency) -> Decision:
    decision: str = "Hold"
    runway = None
    instructions: list[str] = []

    # Handling emergencies
    if emergency:
        return handle_emergency(decision, emergency, flight_number, instructions, runway)

    # Weather considerations
    if weather == "clear":
        if current_time > scheduled_time + 30:  # Delayed flights
            decision = "Expedite Landing"
            runway = "Runway 3"
        else:
            decision = "Normal Landing"
            runway = "Runway 3"
    elif weather == "stormy":
        if aircraft_type == "large":
            decision = "Delayed Landing"
            runway = "Runway 4"
        else:
            decision = "Divert to alternate airport"
            instructions.append("Contact alternate control for landing instructions")

    # Flight prioritization based on type and schedule
    if aircraft_type == "commercial":
        if current_time <= scheduled_time:
            decision = "On-Time Landing"
            runway = "Runway 1"
        else:
            decision = "Expedite Landing"
            runway = "Runway 1"
    elif aircraft_type == "cargo":
        if current_time > scheduled_time + 60:  # Excessive delay
            decision = "Expedite Landing"
            runway = "Runway 2"
        else:
            decision = "Hold for schedule adjustment"
            instructions.append("Adjust schedule for cargo loading/unloading")

    # Additional safety instructions
    if runway:
        instructions.append("Approach " + runway + " from the north")
        instructions.append("Maintain altitude until further notice")

    return decision, runway, instructions


def handle_emergency(decision, emergency, flight_number, instructions, runway) -> Decision:
    if emergency == "medical":
        decision = "Priority Landing"
        runway = "Runway 1"
    elif emergency == "mechanical":
        decision = "Immediate Landing"
        runway = "Runway 2"
    instructions.append("Clear all paths for " + flight_number)
    return decision, runway, instructions
