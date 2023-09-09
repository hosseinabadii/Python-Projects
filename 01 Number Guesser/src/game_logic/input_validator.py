def validator(user_input: int, start: int, end: int) -> bool:
    try:
        number = int(user_input)
    except ValueError:
        print(f"Your input {user_input!r} is not valid. Try again...")
        return False

    if (number < start) or (number > end):
        print(f"Your input is not in range [{start}, {end}]. Try again...")
        return False

    return True
