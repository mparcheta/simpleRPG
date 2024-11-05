from src.action import Action
from src.character import Character
from src.character.monsters.monster import Monster
import random


class Player(Character):
    HEAL_MANA_COST = 6
    MANA_REPLENISH_VALUE = 1
    CRITICAL_CHANCE = 0.2

    def __init__(self):
        super().__init__(max_health=15, dmg_range=(2, 4))
        self.max_mana = 10
        self.mana = self.max_mana
        self.gold = 0
        self.can_block_next_turn = True

    def attack(self, enemy: Monster):
        damage = self.determine_damage()  # equivalent do Character.determine_damage()
        reduced_damage = max(damage - enemy.current_block, 0)
        enemy.health -= reduced_damage

    def block(self):
        self.is_blocking = True

    def heal(self):
        heal_amount = 5
        self.health = min(self.max_health, self.health + heal_amount)

        self.mana -= Player.HEAL_MANA_COST

    def reset_block(self):
        if self.is_blocking:
            self.can_block_next_turn = False
        else:
            self.can_block_next_turn = True
        self.is_blocking = False

    def replenish_mana(self):
        self.mana = min(self.max_mana, self.mana + Player.MANA_REPLENISH_VALUE)

    def end_turn(self):
        self.replenish_mana()
        self.reset_block()

    @property
    def available_choices(self):
        choices = [Action.ATTACK]
        # Każda selekcja dodaje nam dostępne akcje
        if self.can_block_next_turn:
            choices.append(Action.BLOCK)
        if self.mana >= Player.HEAL_MANA_COST:
            choices.append(Action.HEAL)

        return choices

    @staticmethod
    def is_critical() -> bool:
        if random.random() < Player.CRITICAL_CHANCE:
            return True

    def __str__(self):
        # damage = f"{self.dmg_range[0]}-{self.dmg_range[1]}" equivalent poniżej
        damage = "-".join(map(str, self.dmg_range))
        return f"Player (HP: {self.health}, Mana: {self.mana}, DMG: {damage}, Gold: {self.gold})"
