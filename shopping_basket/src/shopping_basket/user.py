import dataclasses


@dataclasses.dataclass(frozen=True)
class UserID:
    id: str
