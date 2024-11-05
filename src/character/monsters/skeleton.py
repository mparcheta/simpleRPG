from src.character import Character
from src.character.monsters.monster import Monster


class Skeleton(Monster):
    CRITICAL_CHANCE = 0.05

    def __init__(self):
        super().__init__(name="Skeleton", health=12, dmg=2)
