import streamlit as st

st.title("first dashboard")

name = st.text_input("city name?")

if st.button("show"):
    st.write(f"dis yo city: {name}")
    st.success("success")

