# check_gcd
from math import gcd

from brain_games.cli import welcome_user
from brain_games.core import run_game
from brain_games.utils import get_two_random_numbers


def check_gcd():
    user_name = welcome_user()
    run_game(get_gcd, RULES_GCD, user_name)


# gcd_game 
RULES_GCD = "Find the greatest common divisor of given numbers."


# get_gcd
def get_gcd():
    num1, num2 = get_two_random_numbers()
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))

    return question, correct_answer