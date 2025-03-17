# check_calc
import random

from brain_games.quest_check import ask_question


def check_calc(user_name):
    count_right_answers = 0
    while count_right_answers < 3:
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
        operation = random.choice(["+", "-", "*"])
        operations_dict = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
        }
        correct_answer = str(operations_dict[operation](number1, number2))
        question = f"{number1} {operation} {number2}"
        is_correct, user_answer = ask_question(question, correct_answer)
        if is_correct:
            print("Correct!")
            count_right_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
