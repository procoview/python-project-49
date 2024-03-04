# file <game_progression.py>

import random

QUESTION = "What number is missing in the progression?"


def main():
    length = random.randint(5, 10)  
    start = random.randint(1, 10)  
    diff = random.randint(1, 5)  
    progression = list(range(start, start + diff * length, diff))
    index = random.randint(0, 9)
    result = str(progression[index])
    str_progression = ', '.join(str(x) for x in progression)
    filtered_progression = str_progression.replace(result, '..')
    print(f'Question: {filtered_progression}')
    return result
