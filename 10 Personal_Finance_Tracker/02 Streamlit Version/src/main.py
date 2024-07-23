import csv
from datetime import datetime
from pathlib import Path

import pandas as pd
from loguru import logger

ROOT_PATH = Path(__file__).resolve().parent.parent


class CSV:
    CSV_FILE = ROOT_PATH / "data/finance_data.csv"
    COLUMNS = ["date", "amount", "category", "description"]
    DATE_FORMAT = "%d-%m-%Y"

    def __init__(self):
        if not self.CSV_FILE.exists():
            df = pd.DataFrame(columns=self.COLUMNS)
            df.to_csv(self.CSV_FILE, index=False)
            logger.info("New database is created.")
        else:
            logger.info("Database already exists.")

    @classmethod
    def add_entry(cls, date, amount, category, description):
        values = [date, amount, category, description]
        new_entry = dict(zip(cls.COLUMNS, values))
        with open(cls.CSV_FILE, "a") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=cls.COLUMNS)
            writer.writerow(new_entry)
        logger.success("Entry added successfully.")

    @classmethod
    def get_transactions(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        start_date = datetime.strptime(start_date, cls.DATE_FORMAT)
        end_date = datetime.strptime(end_date, cls.DATE_FORMAT)
        df["date"] = pd.to_datetime(df["date"], format=cls.DATE_FORMAT)
        mask = (df["date"] >= start_date) & (df["date"] <= end_date)
        filtered_df = df.loc[mask]
        if filtered_df.empty:
            logger.info("No Transactions found in the given date range.")
            return

        total_income = filtered_df[filtered_df["category"] == "Income"]["amount"].sum()
        total_expense = filtered_df[filtered_df["category"] == "Expense"][
            "amount"
        ].sum()

        return {
            "filtered_df": filtered_df,
            "total_income": total_income,
            "total_expense": total_expense,
        }
