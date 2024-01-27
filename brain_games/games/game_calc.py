# file <game_calc.py>

import random
import operator

QUESTION = "What is the result of the expression?"


def main():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    operations = {"+": operator.add, "-": operator.sub, "*": operator.mul}
    random_operation = random.choice(list(operations.keys()))
    result = str(operations[random_operation](first_number, second_number))
    print(f'Question: {first_number} {random_operation} {second_number}')
    return result
