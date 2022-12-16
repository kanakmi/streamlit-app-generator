def buildCode(appTitle, task, model_endpoint, model_description):
    code = f"""
from transformers import pipeline
import streamlit as st
st.title("{appTitle}")
st.write("{model_description}")

user_input = st.text_input("Enter your input text here")

clicked = st.button('Submit')

if clicked:
    model = pipeline(task="{task}", model="{model_endpoint}")
    st.write("Output:")
    st.write(model(user_input))
"""

    return code