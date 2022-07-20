class EmployeePolicy:
    def __init__(self, employee_id, room_types):
        self.room_types = room_types
        self.employee_id = employee_id

    def allows(self, room_type):
        return room_type in self.room_types
