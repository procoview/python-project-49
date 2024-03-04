# file <game_progression.py>

import random

QUESTION = "What number is missing in the progression?"


def main():
    length = random.randint(5, 10)  
    start = random.randint(1, 10)  
    diff = random.randint(1, 5)  
    progression = list(range(start, start + diff * length, diff))
    random_index = random.randint(0, len(progression) - 1)
    result = str(progression[random_index])
    progression[random_index] = '..'
    question = ', '.join(str(x) for x in progression)
    return result, question
