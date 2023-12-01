# file <game_even.py>

from random import randint

question = "Answer \"yes\" if the number is even, otherwise answer \"no\"."


def do_even():
    global result
    random_number = randint(0,100)
    if (random_number % 2 == 0):
        result = 'yes'
    else:
        result = 'no'
    print(f'Question: {random_number}')
    return result

        
def main():
    do_even()
