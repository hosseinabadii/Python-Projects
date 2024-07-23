import pandas as pd
import streamlit as st
from loguru import logger

def plot_transactions(df: pd.DataFrame):
    df["date"] = pd.to_datetime(df["date"], dayfirst=True)
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
    result_df = pd.DataFrame(
        {
            "Income": income_df["amount"],
            "Expense": expense_df["amount"],
        }
    )
    st.line_chart(result_df, color=["#0000FF", "#FF0000"])
    logger.success("Plot created successfully.")
