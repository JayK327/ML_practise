import streamlit as st
import pandas as pd
import numpy as np

##Title
st.title("My First Streamlit App")

#Simple Text
st.text("This is simple text in Streamlit")

df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':['A','B','C','D']
})

st.write("Dataframe Example:")
st.write(df)
st.dataframe(df.style.highlight_max(axis=0))

#Create a line chart
chart_data=pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)
st.line_chart(chart_data)