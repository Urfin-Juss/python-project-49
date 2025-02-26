# check_even
import random

import prompt


def check_even(user_name):
    count_right_answers = 0
    while count_right_answers < 3:
        number = random.randint(1, 99)
        print(
            f'Answer "yes" if the number is even, otherwise answer '
            f'"no".\nQuestion: {number}'
        )
        even_answer = prompt.string("Answer: ")
        if number % 2 == 0 and even_answer == "yes":
            print("Correct!")
            count_right_answers += 1
        elif number % 2 != 0 and even_answer == "no":
            print("Correct!")
            count_right_answers += 1
        else:
            even_status = "yes" if number % 2 == 0 else "no"
            print(
                f"'{even_answer}' is wrong answer ;(. Correct answer "
                f"was '{even_status}'."
            )
            print(f"Let's try again, {user_name}!")
    print(f"Congratulations, {user_name}!")



