import streamlit as st
from buildCode import buildCode

st.title("Streamlit App Generator")

st.sidebar.image("Hugging Face.jpg")
st.sidebar.write("Generating Streamlit Apps with Hugging Face Models has never been easier. Just enter your model details and we will generate a Streamlit App for you.")
st.sidebar.write("This app is built using Streamlit and Hugging Face. You can find the source code on GitHub.")
st.sidebar.write("Made with ❤️ by [Kanak Mittal](https://twitter.com/Kanakmi)")

with st.form("Enter your Model details here"):
    appTitle = st.text_input("Enter App Title")
    tasks = ["text-classification", "ner", "summarization"]
    task = st.selectbox("Select Task", tasks)
    model_endpoint = st.text_input("Enter Hugging Face Model Endpoint")
    model_description = st.text_input("Enter Model Description")
    c1, c2, c3 = st.columns(3)
    submit = c2.form_submit_button("Generate Streamlit App")

if submit:
    st.balloons()
    code = buildCode(appTitle, task, model_endpoint, model_description)
    with open("streamlit_app.py", "w") as file:
        file.write(code)
    file.close()

    st.subheader("Streamlit App Generated Successfully")
    st.code(code)