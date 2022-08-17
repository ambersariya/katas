from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class Discount:
    percentage: float
    amount: float

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.amount, self.percentage) == (other.amount, other.percentage)
        return NotImplemented

    def __ne__(self, other):
        if other.__class__ is self.__class__:
            return (self.amount, self.percentage) != (other.amount, other.percentage)
        return NotImplemented

    def __lt__(self, other):
        if other.__class__ is self.__class__:
            return (self.amount, self.percentage) < (other.amount, other.percentage)
        return NotImplemented

    def __le__(self, other):
        if other.__class__ is self.__class__:
            return (self.amount, self.percentage) <= (other.amount, other.percentage)
        return NotImplemented

    def __gt__(self, other):
        if other.__class__ is self.__class__:
            return (self.amount, self.percentage) > (other.amount, other.percentage)
        return NotImplemented

    def __ge__(self, other):
        if other.__class__ is self.__class__:
            return (self.amount, self.percentage) >= (other.amount, other.percentage)
        return NotImplemented
