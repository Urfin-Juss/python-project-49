# check_calc
import random

from brain_games.cli import welcome_user
from brain_games.core import run_game
from brain_games.utils import get_two_random_numbers


def check_calc():
    user_name = welcome_user()
    run_game(get_calc_question, RULES_CALC, user_name)


# calc_game
RULES_CALC = "What is the result of the expression?"

# calc_operations
OPERATIONS = ["+", "-", "*"]
OPERATIONS_DICT = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        }


# get_calc_question
def get_calc_question():
    num1, num2 = get_two_random_numbers()
    operation = random.choice(OPERATIONS)
    correct_answer = str(OPERATIONS_DICT[operation](num1, num2))
    question = f"{num1} {operation} {num2}"
    return question, correct_answer
