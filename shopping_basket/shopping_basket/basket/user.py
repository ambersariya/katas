from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class UserId:
    value: str

    def __str__(self) -> str:
        return self.value


@dataclass(init=True, frozen=True)
class User:
    id: UserId
