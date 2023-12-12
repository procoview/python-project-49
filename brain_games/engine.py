# file <engine.py>

def launch_game(game):
    print("Welcome to the Brain Games!")

    name = input("May I have your name? ")

    print(f"Hello, {name}!")

    question = game.question

    print(question)

    i = 0
    while i < 3:
        game.main()
        result = game.result
        answer = input("Your answer: ")
        if answer == result:
            print("Correct!")
            i += 1
        else:
            i = 0
            print(f"'{answer}' is wrong answer ;(. ", end='')
            print(f"Correct answer was '{result}'.")
            print(f"Let's try again, {name}!")
    print(f"Congratulations, {name}!")
