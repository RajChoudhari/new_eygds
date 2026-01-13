import streamlit as st
st.title("some basic command like slider and button")
age =st.slider("what is your age",1,100)
city=st.selectbox("choose your city",["pune","mumbai","nashik","solapur"])
if st.button("show details"):
    st.write("your age is",age)
    st.write("your city is",city)
    