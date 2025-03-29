from brain_games.constants import MAX_ATTEMPTS
from brain_games.utils import ask_question

def run_game(get_logic: callable, rules: str, user_name): 
    
    print(rules)
    count_right_answers = 0

    while count_right_answers < MAX_ATTEMPTS:
        number, correct_answer = get_logic()
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
