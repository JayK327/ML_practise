import streamlit as st
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
import numpy as np

@st.cache_data
def load_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species']=iris.target
    return df,iris.target_names

df,target_name=load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:, :-1],df['species'])

st.sidebar.title("Iris Flower Species Prediction")
sepal_length=st.sidebar.slider("Sepal Length (cm)",float(df['sepal length (cm)'].min()),float(df['sepal length (cm)'].max()),float(df['sepal length (cm)'].mean()))
sepal_width=st.sidebar.slider("Sepal Width (cm)",float(df['sepal width (cm)'].min()),float(df['sepal width (cm)'].max()),float(df['sepal width (cm)'].mean()))
petal_length=st.sidebar.slider("Petal Length (cm)",float(df['petal length (cm)'].min()),float(df['petal length (cm)'].max()),float(df['petal length (cm)'].mean()))
petal_width=st.sidebar.slider("Petal Width (cm)",float(df['petal width (cm)'].min()),float(df['petal width (cm)'].max()),float(df['petal width (cm)'].mean()))

input_data=np.array([[sepal_length,sepal_width,petal_length,petal_width]])


#Prediction
prediction=model.predict(input_data)
prediction_species=target_name[prediction[0]]

st.write("## Prediction Results")
st.write(f"The predicted species is: **{prediction_species}**")