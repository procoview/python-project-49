# file <game_prime.py>

from random import randint

QUESTION = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def is_prime(number):
    k = 0
    for i in range(2, number):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        return True
    elif number == 0 or number == 1:
        return True
    else:
        return False


def main():
    question = randint(0, 100)
    result = {True: 'yes', False: 'no'}
    return result[is_prime(question)], question
