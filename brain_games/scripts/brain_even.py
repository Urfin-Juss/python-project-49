from brain_games.cli import welcome_user
from brain_games.even import check_even


def main():
    print("Welcome to the Brain Games!")
    welcome_user()
    check_even()


if __name__ == "__main__":
    main()
