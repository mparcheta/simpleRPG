from src.action import Action
from src.character import Character
from src.character.monsters.monster import Monster
from src.character.player import Player
from src.ui import UI


class CommandLineUI(UI):
    def get_user_choice(self, enemy: "Monster", player: "Player") -> str:
        print(f"{enemy.name} is going to {self.format_action(enemy.current_intent)}")
        available_options = player.available_choices

        valid_choices = list(map(str, range(1, len(available_options) + 1)))
        choice = self.get_user_input(available_options, "What do you want to do: ")
        while not self.is_input_valid(choice, valid_choices):
            print("Wrong answer! Please type the correct one.")
            choice = self.get_user_input(available_options, "What do you want to do: ")

        return available_options[int(choice) - 1]

    def game_over_screen(self, enemy: Monster):
        print(f"Game over! You died, slain by {enemy.name}!")

    def victory_screen(self, player: Player):
        print(f"Congratulations! You won the game with {player.gold} gold earned!")

    def show_stats(self, character: Character):
        print(character)

    def show_after_fight_info(self, enemy: Monster):
        print(f"You defeated the {enemy.name} and earned {enemy.gold_drop} gold!")
        input("Press any key to continue...")

    def get_user_input(self, available_options: list[str], prompt: str) -> str:
        print(prompt)
        for i, option in enumerate(available_options, start=1):
            print(f"{i}. {self.format_action(option)}")

        choice = input("> ")

        return choice

    @staticmethod
    def format_action(action: str) -> str:
        action_dict = {
            Action.ATTACK: "Attack",
            Action.BLOCK: "Block",
            Action.HEAL: "Heal",
        }

        return action_dict.get(action, action)

    @staticmethod
    def is_input_valid(user_choice: str, valid_choices: list[str]) -> bool:
        return user_choice in valid_choices
