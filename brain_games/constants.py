# constants


# number_of_tries
MAX_ATTEMPTS = 3


# calc_operations
OPERATIONS = ["+", "-", "*"]
OPERATIONS_DICT = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y,
        }


# even_game
RULES_EVEN = "Answer 'yes' if the number is even, otherwise answer 'no'."


# calc_game
RULES_CALC = "What is the result of the expression?"


# gcd_game 
RULES_GCD = "Find the greatest common divisor of given numbers."


# progression_const
RULES_PROGRESSION = "What number is missing in the progression?"