def validator(user_input: str, start: int, end: int) -> bool:
    try:
        number = int(user_input)
    except ValueError:
        print(f"--- Your guess {user_input!r} is not valid. Try again...")
        return False

    if (number < start) or (number > end):
        print(f"--- Your guess is not in range [{start}, {end}]. Try again...")
        return False

    return True
