# check_even
import random
import prompt
from brain_games.cli import welcome_user


def check_even():
    number = random.randint(1, 99)
    even_answer = prompt.string(
        f'Answer "yes" if the number is even, otherwise answer "no".\nQuestion: {number}\nAnswer: '
    )
    if number % 2 == 0 and even_answer == "yes":
        print("Correct!")
    else:
        print(
            f"'{even_answer}' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {welcome_user()}!"
        )

    # if number % 2 != 0 and even_answer=='no':
    # else print(f"'{even_answer}' is ")


check_even()
