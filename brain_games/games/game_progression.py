# file <game_progression.py>

from random import randint

question = "What number is missing in the progression?"


def do_progression():
    global result
    num = randint(1, 50)
    nums = []
    for i in range(0, 10):
        nums.append(num)
        num += 2
    index = randint(0, 9)
    result = str(nums[index])
    print(f'Question: ', end="")
    for i in range(0, 10):
        if i == index:
            print('..', end=" ")
        else:
            print(nums[i], end=" ")
    return result


def main():
    do_progression()
