import random
from abc import ABC, abstractmethod

from src.character import Character


class Monster(Character, ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name
        self.gold_drop = random.randint(10, 100)

    @abstractmethod
    def choose_intent(self):
        ...
