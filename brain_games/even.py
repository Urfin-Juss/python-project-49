# check_even
from brain_games.cli import welcome_user
from brain_games.core import run_game
from brain_games.utils import get_two_random_numbers


def check_even():
    user_name = welcome_user()
    run_game(check_parity, RULES_EVEN, user_name)


# even_game
RULES_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


# check_parity
def check_parity():
    number, _ = get_two_random_numbers()
    correct_answer = "yes" if number % 2 == 0 else "no"

    return number, correct_answer