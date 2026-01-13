import streamlit as st
import google.generativeai as genai

st.title("Welcome")
user_input = st.text_input("Ask me anything !")


genai.configure(api_key="AIzaSyC9OT_L0M6qE7JJ0Y9ebj3xKYAjpzYVk5k")

model = genai.GenerativeModel("models/gemini-2.5-flash")

if user_input:
    response = model.generate_content(user_input)
    st.write("Response: ", response.text)