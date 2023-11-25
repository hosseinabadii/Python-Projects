from src.utils import generate_memorable_password


def test_memorable_password_length():
    password = generate_memorable_password(no_of_words=3)
    assert len(password.split("-")) == 3


def test_memorable_password_separator():
    password = generate_memorable_password(separator="#")
    assert len(password.split("#")) == 4


def test_memorable_password_capitalization():
    password = generate_memorable_password(capitalization=True)
    print(password)
    assert all(word[0].isupper() for word in password.split("-"))
