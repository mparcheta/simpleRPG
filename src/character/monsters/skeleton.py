import random

from src.action import Action
from src.character import Character
from src.character.monsters.monster import Monster


class Skeleton(Monster):
    CRITICAL_CHANCE = 0.05

    def __init__(self):
        super().__init__(name="Skeleton", health=12, dmg=3)

    def choose_intent(self) -> str:
        self.current_intent = random.choice(
            [Action.ATTACK, Action.BLOCK, Action.SHIELD_ATTACK]
        )

        return self.current_intent
