from src.character import Character
from src.character.monsters.monster import Monster
from src.character.monsters.monsterwithoutcrit import MonsterWithoutCrit


class Orc(MonsterWithoutCrit):
    def __init__(self):
        super().__init__(name="Orc", health=18, dmg=4)
