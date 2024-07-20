import csv
from datetime import datetime

import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from data_entry import get_amount, get_category, get_date, get_description

matplotlib.use("TkAgg")


class CSV:
    CSV_FILE = "data/finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    DATE_FORMAT = "%d-%m-%Y"

    @classmethod
    def initialize_csv(cls):
        try:
            df = pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns=cls.COLUMNS)
            df.to_csv(cls.CSV_FILE, index=False)

    @classmethod
    def add_entry(cls, date, amount, category, description):
        values = [date, amount, category, description]
        new_entry = dict(zip(cls.COLUMNS, values))
        with open(cls.CSV_FILE, "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        print("Entry added successfully.")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        start_date = datetime.strptime(start_date, cls.DATE_FORMAT)
        end_date = datetime.strptime(end_date, cls.DATE_FORMAT)
        df["date"] = pd.to_datetime(df["date"], format=cls.DATE_FORMAT)
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]
        if filtered_df.empty:
            print("No Transactions found in the given date range.")
            return

        print(
            f"\nTransactions from {start_date.strftime(cls.DATE_FORMAT)} to {end_date.strftime(cls.DATE_FORMAT)}"
        )
        print(
            filtered_df.to_string(
                index=False,
                formatters={"date": lambda d: d.strftime(cls.DATE_FORMAT)},
                na_rep="empty",
            )
        )

        total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
        total_expense = filtered_df[filtered_df["category"] == "Expense"][
            "amount"
        ].sum()

        print("\nSummary")
        print("-" * 30)
        print(f"Total Income  : ${total_income:.2f}")
        print(f"Total Expense : ${total_expense:.2f}")
        print(f"Net Savings   : ${(total_income - total_expense):.2f}")
        print("-" * 30)

        return filtered_df


def add():
    CSV.initialize_csv()
    date = get_date(
        "Enter the date of transaction (dd-mm-yyyy) or press enter for today's day: ",
        allow_default=True,
    )
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_entry(date, amount, category, description)


def plot_transactions(df: pd.DataFrame):
    df.set_index("date", inplace=True)
    income_df = (
        df[df["category"] == "Income"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    expense_df = (
        df[df["category"] == "Expense"]
        .resample("D")
        .sum()
        .reindex(df.index, fill_value=0)
    )
    plt.figure(figsize=(5, 10))
    plt.plot(income_df.index, income_df["amount"], label="Income", color="g")
    plt.plot(expense_df.index, expense_df["amount"], label="Expense", color="r")
    plt.xlabel("Date")
    plt.ylabel("Amount")
    plt.grid()
    plt.legend()
    plt.show()


def main():
    while True:
        print("\n1. Add new transaction")
        print("2. View transactions and summary within a date range")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            add()
        elif choice == "2":
            start_date = get_date("Enter the start date (dd-mm-yyyy): ")
            end_date = get_date("Enter the end   date (dd-mm-yyyy): ")
            df = CSV.get_transactions(start_date, end_date)
            if (df is not None) and (
                input("Do you want to see a plot? (y/n)").lower() == "y"
            ):
                plot_transactions(df)

        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Enter 1, 2 and 3.")


if __name__ == "__main__":
    main()
