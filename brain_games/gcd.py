# check_gcd
from brain_games.cli import welcome_user
from brain_games.constants import RULES_GCD
from brain_games.core import run_game
from brain_games.utils import get_gcd


def check_gcd():
    user_name = welcome_user()
    run_game(get_gcd, RULES_GCD, user_name)
