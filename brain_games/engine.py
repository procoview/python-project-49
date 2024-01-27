# file <engine.py>

def launch_game(game):
    print("Welcome to the Brain Games!")

    name = input("May I have your name? ")

    print(f"Hello, {name}!")

    question = game.QUESTION

    print(question)

    for i in range(0, 3):
        result = game.main()
        answer = input("Your answer: ")
        if answer == result:
            print("Correct!")
            i += 1
        else:
            i = 0
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")
