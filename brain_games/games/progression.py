# file <game_progression.py>

from random import randint

QUESTION = "What number is missing in the progression?"


def generate_progression(start, end, step):
    numbers = list(range(start, end, step))
    return numbers


def main():
    start_num = randint(1, 10)
    end_num = randint(20, 30)
    step_size = 2
    progression = generate_progression(start_num, end_num, step_size)
    index = randint(0, 9)
    result = str(progression[index])
    str_progression = ', '.join(progression)
    filtered_progression = str_progression.replace(result, '..')
    print(f'Question: {filtered_progression}')
    return result
