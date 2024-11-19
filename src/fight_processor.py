from src.character.monsters.monster import Monster
from src.character.player import Player
from src.action import Action
from src.ui import UI


class FightProcessor:
    def process_fight(self, player: Player, enemy: Monster, ui: UI) -> bool:
        fight_is_ongoing = True

        while fight_is_ongoing:
            ui.show_stats(player)
            ui.show_stats(enemy)
            enemy_intent = enemy.choose_intent()
            player_choice = ui.get_user_choice(enemy, player)

            if enemy_intent in (Action.BLOCK, Action.SHIELD_ATTACK):
                enemy.block()

            if player_choice == Action.ATTACK:
                player.attack(enemy)
            elif player_choice == Action.BLOCK:
                player.block()
            elif player_choice == Action.HEAL:
                player.heal()
            elif player_choice == Action.FIRE_BALL:
                player.fireball_attack(enemy)

            if enemy.health <= 0:
                fight_is_ongoing = False
            elif enemy_intent in (Action.ATTACK, Action.SHIELD_ATTACK):
                enemy.attack(player)

            if player.health <= 0:
                fight_is_ongoing = False

            enemy.end_turn()
            player.end_turn()

        return player.health > 0
