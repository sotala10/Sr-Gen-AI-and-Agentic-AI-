import streamlit as st

st.title("My First Streamlit App")
st.write("Hello, Streamlit!")

st.header("select a number")
number = st.slider("Pick a number", 0, 100, 25)

st.subheader("Result:")
squared_number = number ** 2
st.write(f"The square of {number} is {squared_number}.")

