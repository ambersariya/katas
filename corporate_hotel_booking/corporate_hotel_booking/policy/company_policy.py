class CompanyPolicy:
    def __init__(self, company_id, room_types):
        self.room_types = room_types
        self.company_id = company_id

    def allows(self, room_type):
        return room_type in self.room_types
