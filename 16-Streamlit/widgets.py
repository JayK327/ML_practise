import streamlit as st

st.title("Streamlit Widgets Example")
name=st.text_input("Enter your name:")
age=st.slider("Select your age:",0,100,25)
option=st.selectbox("Select your favorite color:",["Red","Green","Blue","Yellow"])

if name:
    st.write(f"Hello, {name}, Your age is {age}!")
    st.write(f"Your favorite color is {option}.")

data=st.dataframe({'Name':['Alice','Bob','Charlie'],'Age':[24,30,22]})
uploaded_file=st.file_uploader("Upload a CSV file:",type=['csv'])