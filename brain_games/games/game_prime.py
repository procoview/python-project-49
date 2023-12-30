# file <game_prime.py>

from random import randint

question = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def do_prime():
    global result
    random_number = randint(0, 100)
    k = 0
    for i in range(2, random_number):
        if (random_number % i == 0):
            k = k + 1
    if (k <= 0):
        result = "yes"
    else:
        result = "no"
    print(f'Question: {random_number}')
    return result


def main():
    do_prime()
