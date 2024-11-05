import random

from src.character.monsters.monster import Monster


class MonsterWithoutCrit(Monster):
    CRITICAL_CHANCE = 0.0

    def __init__(self, name: str, health: int, dmg: int):
        super().__init__(name, health, dmg)

    def determine_damage(self) -> int:
        return random.randint(*self.dmg_range)
