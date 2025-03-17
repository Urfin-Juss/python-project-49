from brain_games.calc import check_calc
from brain_games.cli import welcome_user


def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    check_calc(user_name)


if __name__ == "__main__":
    main()
