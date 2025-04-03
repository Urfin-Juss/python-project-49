# check_progression
import random

from brain_games.cli import welcome_user
from brain_games.core import run_game
from brain_games.utils import get_two_random_numbers


def check_progression():
    user_name = welcome_user()
    run_game(get_progression, RULES_PROGRESSION, user_name)


# progression_const
RULES_PROGRESSION = "What number is missing in the progression?"


# get_progression
def get_progression():
    while True:
        start, step = get_two_random_numbers()
        length = random.randint(5, 10)
        progression = gen_progression(start, step, length)
        if is_valid_progression(progression):
            break

    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    question = " ".join(map(str, progression))
    return question, correct_answer


# gen_progression
def gen_progression(start, step, length):
    return [start + step * i for i in range(length)]


# valid_progression
def is_valid_progression(progression):
    return all(0 <= num <= 100 for num in progression)
