import dataclasses
import datetime


@dataclasses.dataclass(frozen=True)
class CreationDate:
    created_at: datetime.datetime
