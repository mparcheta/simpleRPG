import random
from abc import ABC, abstractmethod


class Character(ABC):
    CRITICAL_CHANCE = 0.1
    CRITICAL_MULTIPLIER = 2

    @abstractmethod
    def __init__(self, max_health: int, dmg_range: tuple[int, int]):
        self.health = max_health
        self.max_health = max_health
        self.dmg_range = dmg_range
        self.is_blocking = False

    def determine_damage(self) -> int:
        base_damage = random.randint(*self.dmg_range)
        if random.random() < self.CRITICAL_CHANCE:
            print(f"Critical hit of {self}!")
            return base_damage * self.CRITICAL_MULTIPLIER
        return base_damage

    @abstractmethod
    def attack(self, other_character: "Character"): ...

    @abstractmethod
    def block(self): ...

    @abstractmethod
    def __str__(self): ...
