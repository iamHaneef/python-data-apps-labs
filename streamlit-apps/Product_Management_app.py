import streamlit as st
import pandas as pd

st.title("Product Management System")

st.set_page_config(layout="wide")

# Initialize session state

if "products" not in st.session_state:
    st.session_state.products = []

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Add User")

    with st.form("Left form"):
        Product_name = st.text_input("Enter The Name")
        Product_price = st.number_input("Enter The Price")
        Product_quantity = st.number_input("Enter The Quantity", 1, 50)
        Product_category = st.selectbox(
            "Select the Product Category",
            ["Electronics", "Hardware Product", "Software Product"],
        )
        button = st.form_submit_button("Add Product")

        if button:
            if Product_name == "":
                st.error("Please Enter The Product Name")

            else:
                st.session_state.products.append(
                    {
                        "product_name": Product_name,
                        "product_price": Product_price,
                        "product_quantity": Product_quantity,
                        "product_category": Product_category,
                    }
                )
            st.success("Product Added Successfully")

        else:
            st.write("Please Add Product")


with col2:
    st.subheader("Product List")
    df = pd.DataFrame(st.session_state.products)

    if df.empty:
        st.error("No Product Data is Added")
    else:
        st.dataframe(df, use_container_width=True)
