# utils.py

import math
import random

import prompt


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
