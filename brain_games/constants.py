# constants

from brain_games.utils import get_two_random_numbers

# number_of_tries
MAX_ATTEMPTS = 3

# calc_num
NUM1, NUM2 = get_two_random_numbers()

# calc_operations
OPERATIONS = ["+", "-", "*"]
OPERATIONS_DICT = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        }

# even_game
RULES_EVEN = "Answer 'yes' if the number is even, otherwise answer 'no'."

