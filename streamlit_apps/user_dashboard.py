import streamlit as st
import pandas as pd

# Initialize session state

if "users" not in st.session_state:
    st.session_state.users = []

# sidebar

st.sidebar.header("User Input")

name = st.sidebar.text_input("Enter Name")
age = st.sidebar.number_input("Enter Age ", 1, 100)  # age enter b/w 1 to 100

course = st.sidebar.selectbox(
    "Select Course", ["Java", "React.js", "Python", "Node.js"]
)

# User DashBoard

st.title("User DashBoard")

st.subheader("User Data")

if st.sidebar.button("Add User"):
    st.session_state.users.append({"name": name, "age": age, "course": course})

df = pd.DataFrame(st.session_state.users)

if df.empty:
    st.warning("No User Data Added yet !!")

else:
    st.dataframe(df, use_container_width=True)
    st.success("User Data Added Successfully !!")
