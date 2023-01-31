import dataclasses
from datetime import datetime

DOB_FORMAT = "%Y-%m-%d"


@dataclasses.dataclass(init=True, frozen=True, eq=True)
class Employee:
    name: str
    dob: datetime

    @property
    def age(self) -> int:
        today = datetime.now()
        timediff = today - self.dob
        return int(timediff.days / 365)
