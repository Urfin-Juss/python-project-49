# check_calc

from brain_games.cli import welcome_user
from brain_games.constants import RULES_CALC
from brain_games.core import run_game
from brain_games.utils import get_calc_question


def check_calc():
    user_name = welcome_user()
    run_game(get_calc_question, RULES_CALC, user_name)
