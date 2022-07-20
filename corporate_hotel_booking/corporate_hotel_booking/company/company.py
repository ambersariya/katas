from dataclasses import dataclass


@dataclass(frozen=True, init=True)
class CompanyId:
    id: str
