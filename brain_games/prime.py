# check_prime
import math

from brain_games.cli import welcome_user
from brain_games.core import run_game
from brain_games.utils import get_two_random_numbers


def check_prime():
    user_name = welcome_user()
    run_game(get_prime, RULES_PRIME, user_name)


# prime_game
RULES_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'


# get_prime
def get_prime():
    number, _ = get_two_random_numbers()
    correct_answer = "yes" if is_prime(number) else "no"

    return number, correct_answer


# gen_progression
def gen_progression(start, step, length):
    return [start + step * i for i in range(length)]


# valid_progression
def is_valid_progression(progression):
    return all(0 <= num <= 100 for num in progression)


def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    limit = int(math.sqrt(number)) + 1
    for i in range(5, limit, 2):
        if number % i == 0:
            return False

    return True