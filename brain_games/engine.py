# file <engine.py>

import prompt


def launch_game(game):
    prompt.string("Welcome to the Brain Games!")

    name = prompt.string("May I have your name? ")

    print(f"Hello, {name}!")

    question = game.QUESTION

    prompt.string(question)

    for i in range(0, 3):
        result = game.main()
        answer = prompt.string("Your answer: ")
        if answer == result:
            prompt.string("Correct!")
            i += 1
        else:
            i = 0
            prompt.string(f"'{answer}' is wrong answer ;(. ", end='')
            prompt.string(f"Correct answer was '{result}'.")
            prompt.string(f"Let's try again, {name}!")
            return
    prompt.string(f"Congratulations, {name}!")
