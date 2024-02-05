# file <game_calc.py>

import random

QUESTION = "What is the result of the expression?"


def is_calc(first_number, random_operation, second_number):
    if random_operation == "+":
        answer = first_number + second_number
    elif random_operation == "-":
        answer = first_number - second_number
    else:
        answer = first_number * second_number
    return answer


def main():
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    operations = ['+', '-', '*']
    random_operation = random.choice(operations)
    result = str(is_calc(first_number, random_operation, second_number))
    print(f'Question: {first_number} {random_operation} {second_number}')
    return result
