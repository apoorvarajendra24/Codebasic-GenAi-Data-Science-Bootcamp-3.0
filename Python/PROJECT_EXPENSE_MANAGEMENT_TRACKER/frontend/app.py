import streamlit as st
from datetime import datetime
import requests

from add_update_ui import add_update_ui
from analytics_ui import analytics_ui

API_URL = "http://localhost:8000"

st.title("Expense Tracking System")

# Add tabs
tab1 , tab2 = st.tabs(['ADD/UPDATE','ANALYTICS'])

with tab1:
    add_update_ui()

with tab2:
    analytics_ui()