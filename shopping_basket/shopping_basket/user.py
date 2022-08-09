from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class UserId:
    value: str


@dataclass(init=True, frozen=True)
class User:
    id: UserId
