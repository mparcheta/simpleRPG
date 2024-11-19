import random

from src.action import Action
from src.character.monsters import Skeleton
from src.character.monsters.monster import Monster


class SkeletonWarrior(Monster):
    CRITICAL_CHANCE = 0.0

    def __init__(self):
        super().__init__(name="Skeleton Warrior", health=16, dmg=5)
        print(SkeletonWarrior.CRITICAL_CHANCE)

    def choose_intent(self) -> str:
        self.current_intent = random.choice(
            [Action.ATTACK, Action.BLOCK, Action.SHIELD_ATTACK]
        )

        return self.current_intent
