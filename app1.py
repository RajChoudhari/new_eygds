import streamlit as st
st.title("somw basic commands")

name = st.text_input("enter your name")
if st.button("submit"):
    st.write("hello",name)