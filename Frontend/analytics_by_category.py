import streamlit as st
from datetime import datetime
import requests
import pandas as pd


API_URL = "http://localhost:8000"


def analytics_category_tab():
    col1, col2 = st.columns(2)

    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))

    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics/", json=payload)

        if response.status_code != 200:
            st.error("Analytics API failed.")
            st.write(response.text)
            return

        response_data = response.json()

        # Convert LIST → DataFrame
        df = pd.DataFrame(response_data)

        # Rename columns for display
        df.rename(columns={
            "category": "Category",
            "total": "Total",
            "percentage": "Percentage"
        }, inplace=True)

        df_sorted = df.sort_values(by="Percentage", ascending=False)

        st.title("Expense Breakdown By Category")

        if df_sorted.empty:
            st.warning("No expense data available.")
            return

        # Bar chart
        st.bar_chart(
            df_sorted.set_index("Category")["Percentage"],
            width="stretch",
            height=400
        )

        # Format values
        df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
        df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

        st.table(df_sorted)


