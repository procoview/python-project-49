# file <engine.py>

import prompt

ROUNDS_COUNT = 3


def launch_game(game):
    print("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")

    print(f"Hello, {name}!")

    play = game.QUESTION

    print(play)

    for _ in range(ROUNDS_COUNT):
        result, question = game.main()
        print(f'Question: {question}')
        answer = prompt.string("Your answer: ")
        if answer != result:
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
        print("Correct!")
    print(f"Congratulations, {name}!")
