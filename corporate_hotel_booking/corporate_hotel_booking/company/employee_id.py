from dataclasses import dataclass


@dataclass(frozen=True, init=True)
class EmployeeId:
    _id: str
