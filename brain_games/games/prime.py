# file <game_prime.py>

from random import randint

QUESTION = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def main():
    random_number = randint(0, 100)
    k = 0
    for i in range(2, random_number):
        if (random_number % i == 0):
            k = k + 1
    if (k <= 0):
        result = "yes"
    else:
        result = "no"
    if random_number == 0 or random_number == 1:
        result = "no"
    print(f'Question: {random_number}')
    return result
