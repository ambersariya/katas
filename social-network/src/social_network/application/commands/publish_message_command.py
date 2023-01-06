from pydantic import dataclasses
from pydantic.dataclasses import dataclass

from src.core.command import Command
from src.core.value_objects import UserId

MIN_LENGTH = 1
MAX_LENGTH = 140


@dataclass()
class PublishMessageCommand(Command):
    message: str = dataclasses.Field(..., min_length=MIN_LENGTH, max_length=MAX_LENGTH)
    publisher: UserId = dataclasses.Field(..., min_length=MIN_LENGTH)
    timeline_user: UserId = dataclasses.Field(..., min_length=MIN_LENGTH)
