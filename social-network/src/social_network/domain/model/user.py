from dataclasses import dataclass


@dataclass(init=True)
class User:
    username: str

    @classmethod
    def from_dto(cls, user):
        _user = cls(user.username)
        return _user
