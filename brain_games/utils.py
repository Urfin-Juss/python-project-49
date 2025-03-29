# utils.py

import prompt
import random


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

#check_parity
def check_parity():
    number, _ = get_two_random_numbers()
    correct_answer = "yes" if number % 2 == 0 else "no"

    return number, correct_answer

