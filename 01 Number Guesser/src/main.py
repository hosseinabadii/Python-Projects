import os


from game_logic.start_game import start_game
from game_logic.input_validator import validator
from game_logic.input_checker import check_user_input


def main(start: int, end: int, score: int) -> None:
    print(f"Your initial score is {score}")
    answer = start_game(start, end)

    while True:
        user_input = input("\n--- Enter your guess: ")
        if user_input == "q":
            print(f"\nThe answer was {answer}")
            print("Thanks for playing...")
            break

        if not validator(user_input, start, end):
            continue

        if not check_user_input(user_input, answer):
            score -= 10
            print(f"(score={score})")
            if score <= 0:
                print("\n>>> Game Over <<<")
                print("Your score is zero.")
                print(f"The answer was {answer}")
                print("Thanks for playing!")
                break
            continue

        print(f"\nCongratulations! The answer was {answer}")
        score += 80
        print(f"You won 80 points! (score={score})")

        wanna_play = input("\nDo you want to play again?(y/n)? ")
        if wanna_play == "y":
            answer = start_game(start, end)
            continue

        print("\nThanks for playing!")
        break


if __name__ == "__main__":
    os.system("clear")
    print("Welcome to Number Guesser game!")
    main(start=1, end=100, score=70)
