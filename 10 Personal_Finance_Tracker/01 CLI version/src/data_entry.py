from datetime import datetime

DATE_FORMAT = "%d-%m-%Y"
CATEGORIES = {"I": "Income", "E": "Expense"}


def get_date(prompt, allow_default=False):
    date_str = input(prompt)
    if allow_default and not date_str:
        return datetime.today().strftime(DATE_FORMAT)
    try:
        valid_date = datetime.strptime(date_str, DATE_FORMAT)
        return valid_date.strftime(DATE_FORMAT)
    except ValueError:
        print(
            f"Invalid date format: {date_str!r}\nPlease enter the date in dd-mm-yyyy format."
        )
        return get_date(prompt, allow_default)


def get_amount():
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError(f"Amount must be non-negetive non-zero value: {amount}")
        return amount
    except ValueError as e:
        print(e)
        return get_amount()


def get_category():
    category = input("Enter the category. 'I' for Income or 'E' for Expense: ").upper()
    if category not in CATEGORIES:
        print("Invalid category. Please enter 'I' for Income or 'E' for Expense.")
        return get_category()
    return CATEGORIES[category]


def get_description():
    return input("Enter a description (optional): ")
