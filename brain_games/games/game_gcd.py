# file <game_gcd.py>

from random import randint

question = "Find the greatest common divisor of given numbers."


def find_gcd(a, b):
    if a > b:
        temp = b
    else:
        temp = a
    for i in range(1, temp + 1):
        if((a % i == 0) and(b % i == 0)):
            gcd = i
    return gcd


def do_gcd():
    global result
    rand_number1 = randint(0, 100)
    rand_number2 = randint(0, 100)
    result = str(find_gcd(rand_number1, rand_number2))
    print(f'Question: {rand_number1} {rand_number2}')


def main():
    do_gcd()
