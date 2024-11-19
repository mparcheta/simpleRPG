from src.character import Character
from src.character.monsters.monster import Monster


class Orc(Monster):
    CRITICAL_CHANCE = 0.0

    def __init__(self):
        super().__init__(name="Orc", health=18, dmg=4)
