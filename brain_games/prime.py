# check_prime
from brain_games.cli import welcome_user
from brain_games.constants import RULES_PRIME
from brain_games.core import run_game
from brain_games.utils import get_prime


def check_prime():
    user_name = welcome_user()
    run_game(get_prime, RULES_PRIME, user_name)