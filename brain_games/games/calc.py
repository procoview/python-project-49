# file <game_calc.py>

import random
import operator

QUESTION = "What is the result of the expression?"


def is_calc(first_number, random_operation, second_number):
    return random_operation[1](first_number, second_number)


def main():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    operations = [['+', operator.add], ['-', operator.sub], ['*', operator.mul]]
    random_operation = random.choice(operations)
    result = str(is_calc(first_number, random_operation, second_number))
    question = f'{first_number} {random_operation[0]} {second_number}'
    return result, question
