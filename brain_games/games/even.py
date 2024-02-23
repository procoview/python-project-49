# file <game_even.py>

from random import randint

QUESTION = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def main():
    question = randint(0, 100)
    result = 'yes' if question % 2 == 0 else 'no'
    return result, question
