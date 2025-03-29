# check_even
from brain_games.constants import RULES_EVEN
from brain_games.core import run_game
from brain_games.cli import welcome_user
from brain_games.utils import check_parity


def check_even():
    user_name = welcome_user()
    run_game(check_parity, RULES_EVEN, user_name)
