import random


def start_game(start, end):
    answer = random.randint(start, end)
    print(f"Enter an integer between {start} and {end}:")

    return answer
