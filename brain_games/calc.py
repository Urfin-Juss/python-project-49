# check_calc
import random

import prompt


def check_calc(user_name):
    count_right_answers = 0
    while count_right_answers < 3:
        number1 = random.randint(1, 99)
        number2 = random.randint(1, 99)
        operation = random.choice(['+', '-', '*'])
        #
        operations_dict = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y
        }
        print(
            f'What is the result of the expression?'
            f'\nQuestion: {number1} {operation} {number2}'
        )
        calc_answer = prompt.string("Your answer: ")

        if operations_dict[operation](number1, number2) == calc_answer:
            print("Correct!")
            count_right_answers += 1
        else:
            print(f"'{calc_answer}' is wrong answer ;(. Correct answer was \n"
                f"'{operations_dict[operation](number1, number2)}'.\n")
                f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
