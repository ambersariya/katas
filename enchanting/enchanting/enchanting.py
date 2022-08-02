import random
from dataclasses import dataclass
import random
from typing import Protocol, Optional


@dataclass(init=True, frozen=True)
class Enchantment:
    prefix: str
    attribute: str


@dataclass(init=True, frozen=True)
class AttackDamage:
    min: int
    max: int


class MagicBook:
    def __init__(self):
        self._enchantments = [
            Enchantment(prefix="Icy", attribute="+5 ice damage"),
            Enchantment(prefix="Inferno", attribute="+5 fire damage"),
            Enchantment(prefix="Vampire", attribute="+5 lifesteal"),
            Enchantment(prefix="Quick", attribute="+5 agility"),
            Enchantment(prefix="Angry", attribute="+5 strength"),
        ]

    def random_enchantment(self) -> Optional[Enchantment]:
        return random.choice([None] + self._enchantments)


class Weapon(Protocol):
    def apply_enchantment(self, enchantment: Enchantment):
        raise NotImplementedError()

    def description(self):
        raise NotImplementedError()


class Dagger(Weapon):
    enchantment: Optional[Enchantment]

    def __init__(self, name: str, attack_damage: AttackDamage, attack_speed):
        self.attack_speed = attack_speed
        self.attack_damage = attack_damage
        self.name = name

    def apply_enchantment(self, enchantment: Enchantment):
        self.enchantment = enchantment

    def description(self):
        # come back to the exposed internals of attack damage
        if self.enchantment:
            return f"""{self.enchantment.prefix} {self._default_description()}{self.enchantment.attribute}
"""
        return self._default_description()

    def _default_description(self):
        return f"""{self.name}
{self.attack_damage.min} - {self.attack_damage.max} attack damage
{self.attack_speed} attack speed
"""


class Durance:
    def __init__(self, magic_book: MagicBook, weapon: Weapon):
        self.weapon = weapon
        self.magic_book = magic_book

    def enchant(self):
        enchantment = self.magic_book.random_enchantment()
        self.weapon.apply_enchantment(enchantment=enchantment)

    def describe_weapon(self):
        return self.weapon.description()
