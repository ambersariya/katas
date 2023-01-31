import dataclasses
from datetime import datetime

DOB_FORMAT = "%Y-%m-%d"


@dataclasses.dataclass(init=True, frozen=True, eq=True)
class Employee:
    name: str
    dob: datetime

    @property
    def age(self):
        today = datetime.now()
        timediff = today - self.dob
        return timediff.days / 365

#
# class Employees:
#     def __init__(self):
#         self.__employees: list[Employee] = []
#
#     def __eq__(self, other: Employees):
#         length_matches = len(self) == len(other)
#         contents_match = set(other.__employees) == set(self.__employees)
#         return length_matches and contents_match
#
#     def __len__(self):
#         return len(self.__employees)
#
#     def __getitem__(self, item):
#         return self.__employees[item]
#
#     def add_employees(self, *employee: Employee):
#         for e in employee:
#             self.__employees.append(e)
