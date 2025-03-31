# utils.py

import prompt
import random
import math
from brain_games.constants import OPERATIONS, OPERATIONS_DICT
from math import gcd

# get_two_random_numbers
def get_two_random_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)

    return num1, num2


# quest_check.py
def ask_question(question: str, correct_answer: str) -> tuple[bool, str]:
    print(f"Question: {question}")
    user_answer = prompt.string("Your answer: ").strip()
    is_correct = user_answer == correct_answer.strip()

    return is_correct, user_answer


# check_parity
def check_parity():
    number, _ = get_two_random_numbers()
    correct_answer = "yes" if number % 2 == 0 else "no"

    return number, correct_answer


# get_calc_question
def get_calc_question():
    num1, num2 = get_two_random_numbers()
    operation = random.choice(OPERATIONS)
    correct_answer = str(OPERATIONS_DICT[operation](num1, num2))
    question = f"{num1} {operation} {num2}"
    return question, correct_answer


# get_gcd
def get_gcd():
    num1, num2 = get_two_random_numbers()
    question = f"{num1} {num2}"
    correct_answer = str(gcd(num1, num2))

    return question, correct_answer


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


# get_prime
def get_prime():
    number, _ = get_two_random_numbers()
    correct_answer = "yes" if is_prime(number) else "no"

    return number, correct_answer


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
