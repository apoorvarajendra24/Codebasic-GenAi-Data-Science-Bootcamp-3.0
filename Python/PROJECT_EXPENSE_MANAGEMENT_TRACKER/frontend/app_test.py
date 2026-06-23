import streamlit as st
import pandas as pd


st.title('Expense Management System')

expense_dt = st.date_input('Expense Date: ')
if expense_dt:
    st.write(f"Fetching expense for {expense_dt}")

# text elements
st.header('Streamlit Header')
st.subheader('text elements')
st.text('this is a text.')

# data display
st.subheader('data display')
st.write('a simple table')

df = pd.DataFrame({
    "date" : ['2026-08-09','2026-08-10','2026-08-11'],
    "amount" : [100,200,300]
})
st.table({'column 1' : [1,2,3], 'column 2':[4,5,6]})
st.write('data from a dataframe')
st.table(df)

# Charts
st.subheader('Charts')
st.line_chart([1,2,3,4,5,6])

# User input
st.subheader('User input')
value = st.slider('Select a value', 0,100)
st.write(f'Selected Value: {value}')


# checkbox
st.subheader('Checkbox')
if st.checkbox('show/hide'):
    st.write('checkbox is checked')

# selectbox
st.subheader("Simple select box")
option = st.selectbox('Select a number', [1,2,3,4])
st.write('Selected value :',option)

# Multiselect
st.subheader('Multiselect')
options = st.multiselect('Select multiple options',[1,2,3,4,5,6])
st.write('You selected: ',options)