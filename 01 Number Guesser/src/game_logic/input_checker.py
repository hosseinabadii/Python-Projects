def check_user_input(user_input: str, answer: int) -> bool:
    number = int(user_input)
    if number > answer:
        print("--- Your guess is too high!", end="")
        return False
    if number < answer:
        print("--- Your guess is too low! ", end="")
        return False

    return True
