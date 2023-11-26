import random
import string
from abc import ABC, abstractmethod

import nltk

# nltk.download('words')


class PasswordGenerator(ABC):
    """Base class for generating passwords."""

    @abstractmethod
    def generate(self) -> str:
        """Subclasses should override this method to generate password."""


class PinCodeGenerator(PasswordGenerator):
    """Class to generate a numeric pin code."""

    def __init__(self, length: int = 4):
        self.length: int = length

    def generate(self) -> str:
        """Generate a numeric pin code."""
        return "".join(random.choices(string.digits, k=self.length))


class RandomPasswordGenerator(PasswordGenerator):
    """Class to generate a random password."""

    def __init__(
        self,
        length: int = 8,
        include_numbers: bool = False,
        include_symbols: bool = False,
    ):
        self.length = length

        self.characters = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        """Generate a password from specified characters."""
        return "".join(random.choices(self.characters, k=self.length))


class MemorablePasswordGenerator(PasswordGenerator):
    """Class to generate a memorable password."""

    def __init__(
        self,
        no_of_words: int = 5,
        separator: str = "-",
        capitalization: bool = False,
        vocabulary: list[str] | None = None,
    ):
        if vocabulary is None:
            vocabulary = (
                nltk.corpus.words.words()
            )  # edit this to any vocabulary list you want

        self.no_of_words: int = no_of_words
        self.separator: str = separator
        self.capitalization: bool = capitalization
        self.vocabulary: list[str] = vocabulary

    def generate(self) -> str:
        """Generate a password from a list of vocabulary words."""
        password_words = random.choices(self.vocabulary, k=self.no_of_words)
        if self.capitalization:
            password_words = [word.upper() for word in password_words]
        return self.separator.join(password_words)
