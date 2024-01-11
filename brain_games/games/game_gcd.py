# file <game_gcd.py>

from random import randint
import math

QUESTION = "Find the greatest common divisor of given numbers."


def do_gcd():
    global result
    rand_number1 = randint(0, 100)
    rand_number2 = randint(0, 100)
    result = str(math.gcd(rand_number1, rand_number2))
    print(f'Question: {rand_number1} {rand_number2}')
    return result


def main():
    do_gcd()
