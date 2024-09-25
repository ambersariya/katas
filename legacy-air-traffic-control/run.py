# Example of invoking the function
from legacy_code_air_traffic import air_traffic_control_system

decision, runway, instructions = air_traffic_control_system("FL123", "commercial", 1200, 1230, "clear", None)
print(f"Decision: {decision}, Runway: {runway}, Instructions: {'; '.join(instructions)}")
