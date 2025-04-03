# utils.py
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
