from src.character import Character
from src.character.monsters.monster import Monster


class Goblin(Monster):
    CRITICAL_CHANCE = 0.1

    def __init__(self):
        super().__init__(name="Goblin", health=10, dmg=2)
