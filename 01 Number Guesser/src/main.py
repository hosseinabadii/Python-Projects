
import os

from game_logic.start_game import start_game
from game_logic.input_validator import validator
from game_logic.input_checker import check_user_input


def main(start, end):
    answer, score = start_game(start, end)

    while True:
        user_input = input("Enter you guess: ")
        if user_input == "q":
            print(f"\nThe answer was {answer}")
            print("Thanks for playing...")
            break

        if not validator(user_input, start, end):
            continue

        if not check_user_input(user_input, answer):
            score -= 10
            score = max(0, score)
            continue

        print(f"\nCongratulations! The answer was {answer}")
        print(f"Your score is {score}")

        wanna_play = input('\nDo you want to play again? (y/n)')
        if wanna_play == "y":
            answer, score = start_game(start, end)
            continue

        print("\nThanks for playing...")
        break


if __name__ == "__main__":
    os.system("clear")
    main(1 ,100)
