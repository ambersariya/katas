from dataclasses import dataclass


@dataclass(init=True, frozen=True)
class PaymentReference:
    value: str
