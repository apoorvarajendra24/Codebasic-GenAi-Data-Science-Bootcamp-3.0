import streamlit as st
import requests
from datetime import datetime

API_URL = "http://localhost:8000"

def add_update_ui():
    selected_date = st.date_input('Enter Date', datetime(2024,8,1), label_visibility='collapsed')
    response = requests.get(f'{API_URL}/expenses/{selected_date}')
    if response.status_code == 200:
        existing_expenses = response.json()
    else:
        st.error('Failed to retrieve expenses..')
        existing_expenses = []

    # ✅ Always overwrite session state with fresh data on date change
    if 'last_date' not in st.session_state or st.session_state['last_date'] != selected_date:
        st.session_state['last_date'] = selected_date
        for i in range(5):
            if i < len(existing_expenses):
                st.session_state[f"amount_{i}"]   = existing_expenses[i]['amount']
                st.session_state[f"category_{i}"] = existing_expenses[i]['category']
                st.session_state[f"notes_{i}"]    = existing_expenses[i]['notes']
            else:
                st.session_state[f"amount_{i}"]   = 0.0
                st.session_state[f"category_{i}"] = "Shopping"
                st.session_state[f"notes_{i}"]    = ""

    categories = ['Rent','Food','Shopping','Entertainment','Other']
    expenses = []

    with st.form(key='expense_form', enter_to_submit=False):
            col1 , col2, col3 = st.columns(3)
            with col1:
                st.subheader('Amount')
            with col2:
                st.subheader('Category')
            with col3:
                st.subheader('Notes')
            
            for i in range(5):
                col1, col2, col3 = st.columns(3)

                with col1:
                    amount_input = st.number_input(label="Amount", min_value=0.0, step=1.0, key=f"amount_{i}", label_visibility='collapsed')
                with col2:
                    category_input = st.selectbox(label='Category', options=categories, key=f"category_{i}", label_visibility='collapsed')
                with col3:
                    notes_input = st.text_input(label='Notes', key=f"notes_{i}", label_visibility='collapsed')
            

                expenses.append(
                    {
                        'amount': amount_input,
                        'category': category_input,
                        'notes': notes_input
                    }
                )
            submit_button = st.form_submit_button()
            if submit_button:
                filtered_expenses = [expense for expense in expenses if expense['amount'] > 0 ]
                requests.post(f"{API_URL}/expenses/{selected_date}", json=filtered_expenses)

                if response.status_code == 200:
                    st.success("Expenses updated successfully!")
                else:
                    st.error("Failed to update Expenses!")