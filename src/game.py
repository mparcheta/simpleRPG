from src.character.monsters.monster import Monster
from src.character.player import Player
from src.fight_processor import FightProcessor
from src.ui.command_line_ui import UI


class Action:
    ATTACK = "atk"
    BLOCK = "blk"
    HEAL = "heal"


class Game:
    def __init__(self, ui: UI, fight_processor: FightProcessor):
        self.player = Player()
        self.ui = ui
        self.fight_processor = fight_processor
        self.running = True
        self.current_monster: Monster = None
        self.floor = 1

    def run(self):
        while self.running:
            if not self.current_monster:
                self.select_next_monster()

            fight_is_won = self.fight_processor.process_fight(self.player, self.current_monster, self.ui)

            if fight_is_won:
                self.player.gold += self.current_monster.gold_drop

                if self.floor == 10:
                    self.ui.victory_screen(self.player)
                    self.running = False
                else:
                    self.ui.show_after_fight_info(self.current_monster)
                    self.floor += 1

                self.current_monster = None
            else:
                self.ui.game_over_screen(self.current_monster)
                self.running = False

    def select_next_monster(self):
        ...
