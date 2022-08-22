from enum import Enum


class ProductCategory(Enum):
    BOOK = "Book"
    VIDEO = "Video"

    def __str__(self) -> str:
        return str(self.value)
