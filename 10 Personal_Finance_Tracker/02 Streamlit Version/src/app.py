import pandas as pd
import streamlit as st
from main import CSV
from plotting import plot_transactions

DATE_FORMAT = "%d-%m-%Y"
st.title(":moneybag: Personal Finance Tracker")

st.sidebar.title(":white_check_mark: Select one of the following")

radio_options = {
    1: "Add new transaction",
    2: "View transactions and summary within a date range",
}
choice = st.sidebar.radio(
    "Select one of the following",
    [1, 2],
    index=None,
    format_func=lambda x: radio_options[x],
    label_visibility="collapsed",
)
if choice == 1:
    date = st.date_input(":date: Date").strftime(DATE_FORMAT)  # type: ignore
    amount = st.number_input(":arrow_right: Amount", min_value=1)
    category = st.selectbox(":arrow_right: Category", ["Income", "Expense"])
    description = st.text_input(":arrow_right: Description")

    if st.button("Submit"):
        CSV.add_entry(date, amount, category, description)
        st.success("Entry added successfully.")

elif choice == 2:
    start_date = st.date_input(":date: Start Date").strftime(DATE_FORMAT)  # type: ignore
    end_date = st.date_input(":date: End Date").strftime(DATE_FORMAT)  # type: ignore
    plotting = st.checkbox(" :chart_with_upwards_trend: Do you want plotting?")

    if st.button("Submit"):
        result = CSV.get_transactions(start_date, end_date)
        if result is None:
            st.warning("No Transactions found in the given date range.")
        else:
            df: pd.DataFrame = result["filtered_df"]
            total_income = result["total_income"]
            total_expense = result["total_expense"]
            st.write(f"\nTransactions from {start_date} to {end_date}")
            df["date"] = df["date"].dt.strftime(DATE_FORMAT)
            st.write(df.set_index("date"))

            st.write(
                pd.DataFrame(
                    [
                        ("Total Income", total_income),
                        ("Total Expense", total_expense),
                        ("Net Savings", (total_income - total_expense)),
                    ],
                    columns=["Summary", "Amount"],
                ).set_index("Summary")
            )
            if plotting:
                pass
                plot_transactions(df)
