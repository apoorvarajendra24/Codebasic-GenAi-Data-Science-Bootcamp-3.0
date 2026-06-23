from click import pass_obj
import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import plotly.express as px


API_URL = "http://localhost:8000"

def analytics_ui():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024,8,1))
    
    with col2:
        end_date = st.date_input("End Date", datetime(2024,8,5))

    if st.button("Get Analytics"):
        payload = {
            "start_date" : start_date.strftime("%Y-%m-%d"),
            "end_date" : end_date.strftime("%Y-%m-%d")
        }
        response = requests.post(f"{API_URL}/analytics", json = payload)
        response = response.json()
        #st.write(response)

        data = {
            "Category" : list(response.keys()),
            "Total" : [response[category]["total"] for category in response],
            "Percentage" : [response[percentage]["percentage"] for percentage in response]
        }

        df = pd.DataFrame(data)
        df = df.sort_values(by="Percentage", ascending=False)
        df['Total'] = df["Total"].map("{:.2f}".format)
        df['Percentage'] = df["Percentage"].map("{:.2f}".format)
        
        fig = px.bar(
            df,
            x="Category",
            y="Percentage",
            title="Expense Breakdown By Category",
            text="Percentage",
            color="Percentage",
            color_continuous_scale="Blues"
        )

        fig.update_traces(texttemplate='%{text:.1f}%', textposition='outside')
        fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Percentage (%)",
        showlegend=False,
        coloraxis_showscale=False
        )
        
        st.title("Expense Breakdown By Category")
        #st.bar_chart(data=df.set_index("Category")['Percentage'])

        st.plotly_chart(fig, use_container_width=True)        
        st.table(df)