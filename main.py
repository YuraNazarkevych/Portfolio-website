import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Yuriy Nazarkevych")
    content = """
    Hi, I am Yura! I am a Python developer. 
    This is my portfolio website with my projects.
    I will add more information about myself in the future.
    """
    st.info(content)

message = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(message)
