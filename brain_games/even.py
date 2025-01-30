# check_even
import prompt
import random
# from brain_games.cli import *


def check_even(user_name):
    number = random.randint(1, 99)
    print(f'Answer "yes" if the number is even, otherwise answer "no".\nQuestion: {number}')
    even_answer = prompt.string('Answer: ')
    if number % 2 == 0 and even_answer == "yes":
        print("Correct!")
    elif number % 2 != 0 and even_answer == "no":
        print("Correct!")
    else:
        even_status = "yes" if number % 2 == 0 else "no"
        print(f"'{even_answer}' is wrong answer ;(. Correct answer was '{even_status}'.")
        print(f"Let's try again, {user_name}!")
        
    # if number % 2 != 0 and even_answer=='no':
    # else print(f"'{even_answer}' is ")


# check_even()
