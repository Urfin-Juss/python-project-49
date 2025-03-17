from brain_games.cli import welcome_user
from brain_games.even import check_even



def main():
    print("Welcome to the Brain Games!")
    user_name = welcome_user()
    check_even(user_name)


if __name__ == "__main__":
    main()
