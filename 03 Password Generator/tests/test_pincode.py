import string
from src.utils import generate_pin


def test_pin_generator():
    pin = generate_pin(length=4)
    print(pin)
    assert len(pin) == 4
    assert all(char in string.digits for char in pin)
