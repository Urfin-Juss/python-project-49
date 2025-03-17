# check_even
import random

from brain_games.quest_check import ask_question


def check_even(user_name):
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")

    count_right_answers = 0

    while count_right_answers < 3:
        number = random.randint(1, 99)
        correct_answer = "yes" if number % 2 == 0 else "no"
        is_correct, user_answer = ask_question(str(number), correct_answer)
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