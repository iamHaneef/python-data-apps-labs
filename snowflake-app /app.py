import streamlit as st
import pandas as pd
from db import fetch_data

st.set_page_config(page_title="Snowflake Data", layout="wide")

#title of the app
st.title("Worker's Data")

data = fetch_data()

if data:

    columns = ["ID", "Name", "Age", "Salary"]
    df = pd.DataFrame(data, columns=columns)


    st.dataframe(df)

    st.subheader("📈 Quick Stats")

    col1, col2 , col3 = st.columns(3)

    col1.metric("Total Workers", len(df))
    col2.metric("Average Age", round(df["Age"].mean(),1))
    col3.metric("Max Salary",df["Salary"].max())

else:
    st.warning("No data found")



