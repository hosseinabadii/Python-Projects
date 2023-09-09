def check_user_input(user_input: int, answer: int) -> bool:
    user_input = int(user_input)
    if user_input > answer:
        print(f"Your input {user_input} is too high!")
        return False
    if user_input < answer:
        print(f"Your input {user_input} is too low!")
        return False

    return True
