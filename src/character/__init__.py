from abc import ABC, abstractmethod


class Character(ABC):
    @abstractmethod
    def __init__(self, max_health: int, dmg_range: tuple[int, int]):
        self.health = max_health
        self.max_health = max_health
        self.dmg_range = dmg_range

    @abstractmethod
    def attack(self, other_character: "Character"):
        ...

    @abstractmethod
    def block(self):
        ...

    @abstractmethod
    def __str__(self):
        ...
