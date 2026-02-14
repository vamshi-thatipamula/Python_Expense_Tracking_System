import streamlit as st
from datetime import datetime
from add_update import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab
from analytics_dashboard import analytics_dashboard_tab

st.title("Expense Tracking System")

tab1, tab2, tab3, tab4 = st.tabs(["Add/Update", "Analytics By Category", "Analytics By Months", "Advanced Dashboard"])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()

    with tab4:
        analytics_dashboard_tab()






# expense_dt = st.date_input("Expense Date: ")
# if expense_dt:
#     st.write(f"Fetching expenses for {expense_dt}")
#
# # Text elements
# st.header("Streamlit Core Features")
# st.subheader("Text Elements")
# st.text("This is a simple text element.")
#
# # Data display
# st.subheader("Data Display")
# st.write("Here is a simple table:")
#
# df = pd.DataFrame({
#     "Date": ["2024-08-01", "2024-08-02", "2024-08-03", "2024-08-04" ],
#     "Amount": [10, 20, 30, 40]
# })
# st.table(df)
#
# st.table({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})
#
# # Charts
# st.subheader("Charts")
# st.line_chart([1, 2, 3, 4])
#
# # User Input
# st.subheader("User Input")
# value = st.slider("Select a value", 0, 100)
# st.write(f"Selected value: {value}")
#
#
# st.title("Interactive Widgets Example")
#
# # Checkbox
# if st.checkbox("Show/Hide"):
#     st.write("Checkbox is checked!")
#
# # Selectbox
# option = st.selectbox("Select a number", [1, 2, 3, 4])
# st.write(f"You selected: {option}")
#
# # Multiselect
# options = st.multiselect("Select multiple numbers", [1, 2, 3, 4])
# st.write(f"You selected: {options}")


