from src.character import Character
from src.character.monsters.monster import Monster
from src.character.monsters.monsterwithoutcrit import MonsterWithoutCrit


class Wolf(Monster):
    CRITICAL_CHANCE = 0.0

    def __init__(self):
        super().__init__(name="Wolf", health=7, dmg=5)
