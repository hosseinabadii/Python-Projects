import string
from src.utils import generate_random_password


def test_random_password_check_defaults():
    password = generate_random_password()
    assert len(password) == 8
    assert any(char in string.ascii_letters for char in password)
    assert any(char not in string.digits for char in password)
    assert any(char not in string.punctuation for char in password)


def test_random_password_lenght():
    password = generate_random_password(length=12)
    assert len(password) == 12


def test_random_password_numbers():
    password = generate_random_password(64, include_numbers=True)
    assert any(char in string.digits for char in password)


def test_random_password_symbols():
    password = generate_random_password(64, include_symbols=True)
    assert any(char in string.punctuation for char in password)


def test_random_password_numbers_symbols():
    password = generate_random_password(64, include_numbers=True, include_symbols=True)
    assert any(char in string.ascii_letters for char in password)
    assert any(char in string.digits for char in password)
    assert any(char in string.punctuation for char in password)
