# file <engine.py>

import prompt

COUNTER = 3

def launch_game(game):
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")

    print(f"Hello, {name}!")

    question = game.QUESTION

    print(question)

    for i in range(0, COUNTER):
        result = game.main()
        answer = prompt.string("Your answer: ")
        if answer == result:
            print("Correct!")
        else:
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
