from dataclasses import dataclass


@dataclass(init=True, eq=True)
class Employee:
    employee_id: str
    company_id: str
