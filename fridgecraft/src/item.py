from enum import Enum


class ItemCondition(Enum):
    OPENED = 'opened'
    SEALED = 'sealed'


class Item:
    def __init__(self, name: str, expiry: str, condition: str):
        self.condition = condition
        self.expiry = expiry
        self.name = name
