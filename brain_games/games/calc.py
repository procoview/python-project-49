# file <game_calc.py>

import random
import operator

QUESTION = "What is the result of the expression?"


def generate_game():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    operations = [['+', operator.add], ['-', operator.sub], ['*', operator.mul]]
    operation_sign, operation = random.choice(operations)
    result = str(operation(first_number, second_number))
    question = f'{first_number} {operation_sign} {second_number}'
    return result, question
