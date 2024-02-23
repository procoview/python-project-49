# file <game_progression.py>

from random import randint, choice

QUESTION = "What number is missing in the progression?"


def generate_progression():
    result = randint(1, 40)
    step = randint(2, 9)
    start = 0
    stop = randint(5, 10)
    result_progression = ''

    while start <= stop:
        result = result + step
        start = start + 1
        result_progression = result_progression + f'{str(result)} '

    return result_progression


def main():
    progression = generate_progression()
    list_progression = progression.split()
    result = choice(list_progression)
    print(f'Question: {progression.replace(result, "..")}')
    return result
