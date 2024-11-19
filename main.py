from src.fight_processor import FightProcessor
from src.game import Game
from src.ui.command_line_ui import CommandLineUI


if __name__ == "__main__":
    fight_processor = FightProcessor()
    ui = CommandLineUI()
    game = Game(ui, fight_processor)

    game.run()


# 22.10
# PD - zrobić walidację inputów (dwie rzeczy: na podstawie available_options chcemy sprawdzić range, bez hardcode'u)
# Jeżeli input niepoprawny to wrzucamy info, że zły wybór i cały prompt albo sam input
# Zaimplementować resztę potworów

# 29.10
# PD zbalansować walkę (może zwiększenie many odnawialnej? albo mniejszy dmg orka np. - ogółem potestować)
# Zrobić critical damage (podwajający) na podsstawie critical chance (dla każdego gracza/monstera niech to będzie stała. Niektóre potwory nie muszą mieć crit chance - wtedy trzeba zrobic osobna klase). Co każdy atak rzucamy kostką (moduł random) i na jego podstawie podwajamy dmg, który został NA JEDNĄ TURĘ albo nie.
# Unluck hity - opcjonalnie
# Ewentualnie dodanie expa (dorzucić statystykę level)


# PD 12.11
# Zaimplementować Skeleton Warrior
