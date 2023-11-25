<img src="./images/rock-paper-scissors.png" width="700"/>

# Rock Paper Scissors Game in Python

Welcome to this simple implementation of the classic game Rock Paper Scissors. This Python project encapsulates the game's mechanics using fundamental programming constructs such as functions and conditional statements.

The game leverages Python's built-in **random** module for generating the computer's moves, and the **os** module to clear the console, providing a clean user interface for each turn.

## Game Instructions

Before you start, understand the rules:
- Rock crushes Scissors ⇒ Rock wins
- Scissors cut Paper ⇒ Scissors win
- Paper covers Rock ⇒ Paper wins

These simple rules dictate the outcome of the game.


## Directory Structure and Files

Here's how the project files are organized:

```
02 Rock Paper Scissors/
├── src/
│   ├── main.py
│   └── options.py
├── README.md
└── requirements.txt
```

## How to Run

1. Navigate to the main project directory (`02 Rock Paper Scissors`).
2. Add the current directory to the `PYTHONPATH` and run the `main.py` script:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```

Follow the on-screen prompts to play the game.
