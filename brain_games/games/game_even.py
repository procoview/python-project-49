# file <game_even.py>

from random import randint


def even():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    i = 0
    while i < 3:
        random_number = randint(0, 100)
        if (random_number % 2 == 0):
            is_even = 'yes'
        else:
            is_even = 'no'
        print(f'Question: {random_number}')
        answer = input("Your answer: ")
        if answer == is_even:
            print("Correct!")
            i += 1
        else:
            i = 0
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{is_even}'.")
            print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    even()
