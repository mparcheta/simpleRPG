from abc import ABC, abstractmethod

from src.character import Character
from src.character.monsters.monster import Monster
from src.character.player import Player


class UI(ABC):
    @abstractmethod
    def victory_screen(self, player: Player):
        ...

    @abstractmethod
    def game_over_screen(self, enemy: Monster):
        ...

    @abstractmethod
    def get_user_choice(self, enemy: "Monster", player: "Player") -> str:
        ...

    @abstractmethod
    def show_stats(self, character: Character):
        ...

    @abstractmethod
    def show_after_fight_info(self, enemy: Monster):
        ...
