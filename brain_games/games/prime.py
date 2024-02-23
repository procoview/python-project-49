# file <game_prime.py>

from random import randint

QUESTION = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def is_prime(number):
    k = 0
    for i in range(2, number):
        if (number % i == 0):
            k = k + 1
    if (k <= 0):
        return "yes"
    elif number == 0 or number == 1:
        return "no"
    else:
        return "no"


def main():
    random_number = randint(0, 100)
    result = is_prime(random_number)
    print(f'Question: {random_number}')
    return result
