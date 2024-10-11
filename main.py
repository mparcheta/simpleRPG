from src.fight_processor import FightProcessor
from src.game import Game
from src.ui.command_line_ui import CommandLineUI


if __name__ == '__main__':
    fight_processor = FightProcessor()
    ui = CommandLineUI()
    game = Game(ui, fight_processor)

    game.run()
