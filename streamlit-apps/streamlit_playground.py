import streamlit as st
import pandas as pd
import os

# for heading related styles

st.title("Application Title")

st.header("Header")

st.subheader("Subheader")

st.text("Text")

# sidebar

st.sidebar.header("Sidebar Header")

st.sidebar.text("Sidebar Text")

st.sidebar.subheader("Sidebar Subheader")

# for buttons

if st.button("Click Me"):
    st.write("Button Clicked")

# for checkbox

if st.checkbox("Check Me"):
    st.write("Checkbox Checked")

# for radio button

radio_button = st.radio("Select Option", ["Option 1", "Option 2", "Option 3"])

st.write("Selected Option : ", radio_button)

# for slider

slider = st.slider("Select Value", 1, 100)

st.write("Selected Value : ", slider)

# for selectbox

selectbox = st.selectbox("Select Option", ["Option 1", "Option 2", "Option 3"])

st.write("Selected Option : ", selectbox)

# for multiselect

st.multiselect("Select Option", ["Option 1", "Option 2", "Option 3"])   

#date input

st.date_input("Select Date")

#time input

st.time_input("Select Time")

# --- File Uploader (Save to Repo) ---
st.subheader("File Uploader (Save to Repo)")
uploaded_file = st.file_uploader("Select a file to upload")

if uploaded_file is not None:
    # Ensure the upload directory exists
    upload_dir = "uploads"
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
        
    # Define the save path
    file_path = os.path.join(upload_dir, uploaded_file.name)
    
    # Save the file locally
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        
    st.success(f"File saved successfully to `{file_path}`")

#color picker

st.color_picker("Select Color")

# --- Input Widgets ---
st.header("Additional Input Widgets")

number = st.number_input("Insert a number", min_value=0, max_value=100, value=25)
st.write(f"The current number is {number}")

text_input = st.text_input("Enter some text", "Type here...")
st.write(f"You entered: {text_input}")

text_area = st.text_area("Enter a long story", "Once upon a time...")
st.write(f"Story length: {len(text_area)} characters")

st.camera_input("Take a picture")

# --- Media Widgets ---
st.header("Media Widgets")
# Note: These usually require a URL or local path
st.image("https://images.unsplash.com/photo-1518770660439-4636190af475", caption="Sample Image")
# st.audio("sample.mp3") 
# st.video("sample.mp4")

# --- Layouts & Containers ---
st.header("Layouts & Containers")

col1, col2 = st.columns(2)
with col1:
    st.error("This is Column 1")
with col2:
    st.warning("This is Column 2")

tab1, tab2 = st.tabs(["Tab A", "Tab B"])
with tab1:
    st.write("Content for Tab A")
with tab2:
    st.write("Content for Tab B")

with st.expander("Click to expand detail"):
    st.write("Here is some hidden information that users can see when they click.")

# --- Status & Progress ---
st.header("Status & Progress")

if st.button("Show Success"):
    st.success("Success message!")

if st.button("Show Error"):
    st.error("Error message!")

if st.button("Celebrate"):
    st.balloons()
    st.snow()

# --- Advanced Widgets ---
st.header("Metrics & Data")
st.metric(label="Temperature", value="70 °F", delta="1.2 °F")

# --- Forms ---
st.header("Forms")
with st.form("my_form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    st.form_submit_button("Submit")
    
# --- Data Display ---
st.header("Data Display")
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
})

st.subheader("Data Editor (Editable Tables)")
edited_df = st.data_editor(df)

st.subheader("Standard Dataframe")
st.dataframe(df)

st.subheader("Static Table")
st.table(df)

st.subheader("JSON & Code")
st.json({"key": "value", "list": [1, 2, 3]})
st.code("print('Hello Streamlit!')", language='python')

# --- Chat & Modern UI ---
st.header("Chat & Modern UI")

st.chat_message("assistant").write("Hello! I'm a chat assistant. How can I help you today?")
# st.chat_input("Say something...") # Only one allowed per page, often at the bottom

st.subheader("Popover & Buttons")
with st.popover("Open Popover"):
    st.write("This is a popover container")
    st.text_input("Pop-up input")

st.link_button("Go to Streamlit Docs", "https://docs.streamlit.io")

# --- Help & Debugging ---
st.header("Help & Debugging")
st.help(st.header)
