<img src="./images/password-generator.png" width=800>

# Python Password Generator

This is a simple Python project that provides tools to generate various types of secure passwords and PINs. There are three main types of generators included:

1. PIN Generator
2. Random Password Generator
3. Memorable Password Generator

Each type of generator can be customized with parameters such as length, inclusion of numbers or symbols, separator characters, word capitalization, and custom vocabulary for memorable passwords.


## Directory Structure and Files

Here's how the project files are organized:

```
03 Password Generator/
├── src/
│   ├── main.py
│   └── utils.py
├── tests/
│   ├── test_memorable_password.py
│   └── test_pincode.py
│   └── test_random_password.py
├── README.md
└── requirements.txt
```

## How to Run

1. Navigate to the main project directory (`03 Password Generator`).
2. Add the current directory to the `PYTHONPATH` and run the `main.py` script:
```bash
export PYTHONPATH=$PYTHONPATH:$(pwd)
python src/main.py
```

## Running Tests

This project uses the `pytest` module for testing. If you haven't already, install `pytest` using the following command:

```bash
pip install pytest
```

To run the tests, navigate to the project folder and run:

```bash
pytest tests
```

This will discover and run all the test cases located in the `tests` directory.


### PIN Generator

The PIN generator will create a numeric PIN code. By default, the PIN is 4 digits long, but you can specify a different length when calling `generate_pin` function.

### Random Password Generator

The random password generator creates a password using uppercase and lowercase letters by default, with the option to add numbers and special characters. You can set the desired password length and specify whether to include numbers and/or symbols.

### Memorable Password Generator

Generate a password that is easier to remember by combining a specified number of words from a vocabulary list with a chosen separator. You can also choose to capitalize the first letter of each word and provide your own custom vocabulary list.
