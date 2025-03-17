# quest_check.py
import prompt


def ask_question(question: str, correct_answer: str) -> tuple[bool, str]:
    print(f"Question: {question}")
    user_answer = prompt.string("Your answer: ").strip()
    is_correct = user_answer == correct_answer.strip()
    return is_correct, user_answer
