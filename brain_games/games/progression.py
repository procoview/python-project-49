# file <game_progression.py>

import random

QUESTION = "What number is missing in the progression?"


def main():
    length = random.randint(5, 10)  
    start = random.randint(1, 10)  
    diff = random.randint(1, 5)  
    progression = list(range(start, start + diff * length, diff))
    result = str(random.choice(progression))
    str_progression = ', '.join(str(x) for x in progression)
    question = str_progression.replace(result, '..')
    return result, question
