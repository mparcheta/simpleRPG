from src.character import Character
from src.character.monsters.monster import Monster
from src.character.monsters.monsterwithoutcrit import MonsterWithoutCrit


class Wolf(MonsterWithoutCrit):
    def __init__(self):
        super().__init__(name="Wolf", health=7, dmg=5)
