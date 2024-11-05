import random
from abc import ABC, abstractmethod

from src.character import Character
from src.action import Action


class Monster(Character, ABC):
    CRITICAL_CHANCE = 0.1

    @abstractmethod
    def __init__(self, name: str, health: int, dmg: int):
        self.current_block = 0
        self.name = name
        self.gold_drop = random.randint(10, 100)
        self.current_intent = None
        super().__init__(max_health=health, dmg_range=(dmg, dmg))

    def choose_intent(self) -> str:
        self.current_intent = random.choice([Action.ATTACK, Action.BLOCK])
        return self.current_intent

    def attack(self, player: "Character"):
        # self.current_block = 0 reset blocka - lepiej zrobić to jako oddzielna metode (napisana nizej)
        if player.is_blocking:
            return

        player.health -= self.determine_damage()

    def block(self):
        self.current_block = random.randint(1, 3)

    def reset_block(self):
        self.current_block = 0

    def end_turn(self):
        self.reset_block()

    def __str__(self):
        return f"{self.name} (HP: {self.health}, DMG: {self.dmg_range[0]})"
