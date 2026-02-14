import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"

def analytics_months_tab():
    response = requests.get(f"{API_URL}/monthly_summary/")

    if response.status_code != 200:
        st.error("Monthly summary API failed.")
        return

    monthly_summary = response.json()

    df = pd.DataFrame(monthly_summary)

    # Rename correct columns
    df.rename(columns={
        "expense_month": "Month Number",
        "month_name": "Month Name",
        "total_spent": "Total"
    }, inplace=True)

    df_sorted = df.sort_values(by="Month Number")

    st.title("Expense Breakdown By Months")

    # Bar chart
    st.bar_chart(
        df_sorted.set_index("Month Name")["Total"],
        width="stretch",
        height=400
    )

    df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)

    st.table(df_sorted[["Month Name", "Total"]])


