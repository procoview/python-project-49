# file <game_gcd.py>

from random import randint

question = "Find the greatest common divisor of given numbers."


def do_gcd():
    global result
    rand_number1 = randint(0, 100)
    rand_number2 = randint(0, 100)
    while rand_number1 != 0 and rand_number2 != 0:
        if rand_number1 > rand_number2:
            rand_number1 = rand_number1 % rand_number2
        else:
            rand_number2 = rand_number2 % rand_number1
    result = str(rand_number1 + rand_number2)
    print(f'Question: {rand_number1} {rand_number2}')


def main():
    do_gcd()
