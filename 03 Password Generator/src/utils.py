import random
import string


def generate_pin(length: int = 4) -> str:
    """
    Generate a numeric pin code.
    """
    return "".join(random.choices(string.digits, k=length))


def generate_random_password(
    length: int = 8, include_numbers: bool = False, include_symbols: bool = False
) -> str:
    """
    Generate a random password.
    """
    characters = string.ascii_letters

    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    return "".join(random.choices(characters, k=length))


def generate_memorable_password(
    no_of_words: int = 4,
    separator: str = "-",
    capitalization: bool = False,
    vocabulary: list[str] | None = None,
) -> str:
    """
    Generate a memorable password from a list of vocabulary words.
    """
    if vocabulary is None:
        vocabulary = [
            "apple",
            "banana",
            "cherry",
            "dates",
        ]  # edit this to any vocabulary list you want

    password_words = random.sample(vocabulary, no_of_words)

    if capitalization:
        password_words = [word.capitalize() for word in password_words]

    return separator.join(password_words)
