from utils.number_generator import create_random_number


def start_game(start, end):
    answer = create_random_number(start, end)
    score = 100
    print(f"Enter an integer between {start} and {end}:")
    return answer, score
