import os
import random

from src.options import rock, paper, scissors

choices = (1, 2, 3)
items = {1: rock, 2: paper, 3: scissors}
winners = {rock: scissors, scissors: paper, paper: rock}


def get_user_choice():
    """Gets the user's choice."""
    print("*" * 30)
    print("1. Rock\n2. Paper\n3. Scissors \n")
    err_msg = "Invalid input. Select one of (1,2,3)"

    while True:
        try:
            user_choice = int(input("Enter your choice (1,2,3)? "))
            if user_choice not in choices:
                print(err_msg)
                continue
            break
        except ValueError:
            print(err_msg)

    return items[user_choice]


def get_computer_choice():
    """Gets the computer's choice."""
    computer_choice = random.randint(1, 3)
    return items[computer_choice]


def determine_winner(user_choice: str, computer_choice: str):
    """Determines the winner."""
    if user_choice == computer_choice:
        return "It's a Tie"
    if winners[user_choice] == computer_choice:
        return "You Wins!"
    return "Computer Wins!"


def play():
    """Plays the game."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You:", user_choice)
    print("Computer:", computer_choice)
    result = determine_winner(user_choice, computer_choice)
    result_msg = f">>> {result} <<<"
    print("-" * len(result_msg))
    print(result_msg)
    print("-" * len(result_msg))


def main():
    os.system("clear")
    print("Welcome to Game!")

    while True:
        play()
        paly_again = input("Play again (y/n)? ")
        if paly_again.lower().startswith("n"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
