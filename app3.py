import streamlit as st
st.title("calci")
num1 = st.number_input("enter first num")
num2 = st.number_input("enter second num")

operations = st.selectbox("choose operation",["add","sub","mul","div"])
if st.button("calculate"):
    if operations=="add":
         st.write("addition is",num1+num2)
    elif operations=="sub":
         st.write("subtraction is",num1-num2)
    elif operations=="mul":
         st.write("multiplication is",num1*num2)
    else:
         st.write("division is",num1/num2)