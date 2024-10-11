from src.character.monsters.monster import Monster
from src.character.player import Player
from src.game import Action
from src.ui import UI


class FightProcessor:
    def process_fight(self, player: Player, enemy: Monster, ui: UI) -> bool:
        fight_is_ongoing = True

        while fight_is_ongoing:
            ui.show_stats(player)
            ui.show_stats(enemy)
            enemy_intent = enemy.choose_intent()
            player_choice = ui.get_user_choice(enemy_intent)

            if enemy_intent == Action.BLOCK:
                enemy.block()

            if player_choice == Action.ATTACK:
                player.attack(enemy)
            elif player_choice == Action.BLOCK:
                player.block()
            elif player_choice == Action.HEAL:
                player.heal()

            if enemy.health <= 0:
                fight_is_ongoing = False
            elif enemy_intent == Action.ATTACK:
                enemy.attack(player)

            if player.health <= 0:
                fight_is_ongoing = False

        return player.health > 0
