import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"


def add_update_tab():
    st.title("Add / Update Expenses")

    # Date selector
    selected_date = st.date_input(
        "Enter Date",
        datetime(2024, 8, 1),
        label_visibility="collapsed"
    )

    # Convert date to string for API
    date_str = selected_date.strftime("%Y-%m-%d")

    # ---------- GET existing expenses ----------
    try:
        response = requests.get(f"{API_URL}/expenses/{date_str}")
        response.raise_for_status()
        existing_expenses = response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Failed to retrieve expenses: {e}")
        existing_expenses = []

    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    # ---------- Expense Form ----------
    with st.form(key="expense_form"):

        col1, col2, col3 = st.columns(3)
        col1.text("Amount")
        col2.text("Category")
        col3.text("Notes")

        expenses = []

        for i in range(5):

            # Load existing values if present
            if i < len(existing_expenses):
                amount = existing_expenses[i].get("amount", 0.0)
                category = existing_expenses[i].get("category", "Shopping")
                notes = existing_expenses[i].get("notes", "")
            else:
                amount = 0.0
                category = "Shopping"
                notes = ""

            col1, col2, col3 = st.columns(3)

            # FIX: Keys must include date_str
            with col1:
                amount_input = st.number_input(
                    "Amount",
                    min_value=0.0,
                    step=1.0,
                    value=float(amount),
                    key=f"amount_{date_str}_{i}",
                    label_visibility="collapsed"
                )

            with col2:
                category_input = st.selectbox(
                    "Category",
                    options=categories,
                    index=categories.index(category),
                    key=f"category_{date_str}_{i}",
                    label_visibility="collapsed"
                )

            with col3:
                notes_input = st.text_input(
                    "Notes",
                    value=notes,
                    key=f"notes_{date_str}_{i}",
                    label_visibility="collapsed"
                )

            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        # Submit button
        submit_button = st.form_submit_button("Save Expenses")

        # ---------- POST updated expenses ----------
        if submit_button:

            # Remove empty rows
            filtered_expenses = [
                expense for expense in expenses if expense["amount"] > 0
            ]

            # Prevent empty submission
            if not filtered_expenses:
                st.warning("Please enter at least one expense before saving.")
                return

            try:
                response = requests.post(
                    f"{API_URL}/expenses/{date_str}",
                    json=filtered_expenses
                )
                response.raise_for_status()

                st.success("Expenses updated successfully!")

            except requests.exceptions.RequestException as e:
                st.error(f"Failed to update expenses: {e}")


