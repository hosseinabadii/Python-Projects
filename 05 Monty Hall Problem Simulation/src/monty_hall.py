import random


def monty_hall_game(switch_doors: bool) -> bool:
    """Simulate a single Monty Hall game.

    :param switch_doors: If True, the contestant will switch their choice
        after a goat door is revealed.
    :return: True if the contestant won the car, False otherwise.
    """

    doors = ["car", "goat", "goat"]
    random.shuffle(doors)

    initial_choice = random.choice(range(3))

    # Monty reveals a door with a goat
    doors_revealed = [i for i in range(3) if i != initial_choice and doors[i] == "goat"]
    door_revealed = random.choice(doors_revealed)

    # If contestant decides to switch, their final choice is the remaining door
    if switch_doors:
        final_choice = [
            i for i in range(3) if i not in (initial_choice, door_revealed)
        ][0]
    else:
        final_choice = initial_choice

    return doors[final_choice] == "car"


def simulate_games(num_games: int = 1000) -> tuple[int]:
    """Simulate a number of Monty Hall games and print the statistics.

    :param num_games: The number of games to simulate. Defaults to 1000.
    :return: (num_wins_without_switching, num_wins_with_switching)
    """

    # Simulate games where contestant keeps and switches doors
    num_wins_without_switching = sum(
        monty_hall_game(switch_doors=False) for _ in range(num_games)
    )
    num_wins_with_switching = sum(
        monty_hall_game(switch_doors=True) for _ in range(num_games)
    )

    return num_wins_without_switching, num_wins_with_switching


if __name__ == "__main__":
    num_games = 1000
    num_wins_without_switching, num_wins_with_switching = simulate_games(num_games)
    print(
        f"Winning percentage without switching doors: {num_wins_without_switching/num_games*100}%"
    )
    print(
        f"Winning percentage with    switching doors: {num_wins_with_switching/num_games*100}%"
    )
