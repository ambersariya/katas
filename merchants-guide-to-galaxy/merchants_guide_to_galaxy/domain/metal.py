import dataclasses

from merchants_guide_to_galaxy.domain.intergalactic_symbols import IntergalacticSymbol


@dataclasses.dataclass(init=True, frozen=True)
class Metal(IntergalacticSymbol):
    pass
