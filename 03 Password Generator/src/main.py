from src.utils import (
    generate_pin,
    generate_random_password,
    generate_memorable_password,
)


def main():
    print("\nExamples for 'PIN' generator:")
    print(generate_pin())
    print(generate_pin(length=12))

    print("\nExamples for 'random password' generator:")
    print(generate_random_password())
    print(generate_random_password(32, include_numbers=True))
    print(generate_random_password(32, include_symbols=True))
    print(generate_random_password(32, include_numbers=True, include_symbols=True))

    print("\nExamples for 'memorable password' generator:")
    print(generate_memorable_password(no_of_words=3))
    print(generate_memorable_password(separator="#"))
    print(generate_memorable_password(capitalization=True))
    print(generate_memorable_password(vocabulary=["book", "door", "car", "bag", "help"]))


if __name__ == "__main__":
    main()
