from src.character import Character
from src.character.monsters.monster import Monster
from src.character.player import Player
from src.ui import UI


class CommandLineUI(UI):
    def get_user_choice(self, enemy_intent: str) -> str:
        ...

    def game_over_screen(self, enemy: Monster):
        print(f"Game over! You died, slain by {enemy.name}!")

    def victory_screen(self, player: Player):
        print(f"Congratulations! You won the game with {player.gold} gold earned!")

    def show_stats(self, character: Character):
        print(Character)

    def show_after_fight_info(self, enemy: Monster):
        print(f"You defeated the {enemy.name} and earned {enemy.gold_drop} gold!")
        input("Press any key to continue...")
