# file <game_prime.py>

from random import randint

QUESTION = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def is_prime(number):
    i = 2
    while number % i != 0:
        i = i + 1
    if number == i:
        return True


def main():
    question = randint(0, 100)
    result = 'yes' if is_prime(question) else 'no'
    return result, question
