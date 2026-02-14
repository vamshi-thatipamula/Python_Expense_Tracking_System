import streamlit as st
from datetime import datetime
import requests
import pandas as pd
import plotly.express as px
import plotly.io as pio

# Global Plotly Theme
pio.templates.default = "plotly_white"

API_URL = "http://localhost:8000"

def analytics_dashboard_tab():

    # Compact Dashboard Header
    st.markdown("## Expense Analytics Dashboard")

    # 1. Load All Required Data

    # Monthly Summary
    monthly_response = requests.get(f"{API_URL}/monthly_summary/")
    monthly_df = pd.DataFrame(monthly_response.json())

    if "total_spent" not in monthly_df.columns:
        st.error("Monthly summary API must return total_spent column.")
        st.write("Columns received:", monthly_df.columns)
        return

    # Category Summary
    category_response = requests.post(
        f"{API_URL}/analytics/",
        json={
            "start_date": "2024-01-01",
            "end_date": "2026-12-31"
        }
    )
    category_df = pd.DataFrame(category_response.json())

    # Top Expenses
    top_response = requests.get(f"{API_URL}/top_expenses/")
    top_df = pd.DataFrame(top_response.json())
    top_df["notes"] = top_df["notes"].fillna("No Notes")

    # Month + Category Summary
    month_cat_response = requests.get(f"{API_URL}/month_category_summary/")
    month_cat_df = pd.DataFrame(month_cat_response.json())

    if "category" not in month_cat_df.columns:
        st.error("month_category_summary must return category column.")
        st.write(month_cat_df.columns)
        return

    # 2. KPI Metrics Row (Compact)

    total_spent = monthly_df["total_spent"].sum()
    avg_monthly = monthly_df["total_spent"].mean()
    max_expense = top_df["amount"].max()

    top_category = category_df.sort_values(
        "total", ascending=False
    ).iloc[0]["category"]

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total", f"₹{total_spent:,.0f}")
    col2.metric("Avg/Month", f"₹{avg_monthly:,.0f}")
    col3.metric("Top Cat", top_category)
    col4.metric("Max", f"₹{max_expense:,.0f}")

    # 3. Create Charts (Compact Height)

    # Chart 1: Monthly Trend
    fig1 = px.line(
        monthly_df,
        x="month_name",
        y="total_spent",
        markers=True,
        title="Monthly Trend"
    )
    fig1.update_traces(line=dict(width=3))
    fig1.update_layout(height=280)

    # Chart 2: Category Donut
    fig2 = px.pie(
        category_df,
        names="category",
        values="total",
        hole=0.45,
        title="Category Split",
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig2.update_traces(textinfo="percent+label")
    fig2.update_layout(height=280)

    # Chart 3: Category Over Time
    fig3 = px.area(
        month_cat_df,
        x="month",
        y="total_spent",
        color="category",
        title="Spending Over Time",
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig3.update_layout(height=280)

    # Chart 4: Top Expenses
    fig4 = px.bar(
        top_df,
        x="amount",
        y="notes",
        orientation="h",
        title="Top Expenses",
        color="amount",
        color_continuous_scale="Blues"
    )
    fig4.update_layout(height=280)

    # 4. Dashboard Grid View (2×2 Layout)

    st.markdown("### Dashboard Overview")

    # -------- Row 1 --------
    row1_col1, row1_col2 = st.columns(2)

    with row1_col1:
        st.plotly_chart(fig1, width="stretch")

    with row1_col2:
        st.plotly_chart(fig2, width="stretch")

    # -------- Row 2 --------
    row2_col1, row2_col2 = st.columns(2)

    with row2_col1:
        st.plotly_chart(fig3, width="stretch")

    with row2_col2:
        st.plotly_chart(fig4, width="stretch")









