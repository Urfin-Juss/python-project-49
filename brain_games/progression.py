# check_progression
from brain_games.cli import welcome_user
from brain_games.constants import RULES_PROGRESSION
from brain_games.core import run_game
from brain_games.utils import get_progression


def check_progression():
    user_name = welcome_user()
    run_game(get_progression, RULES_PROGRESSION, user_name)