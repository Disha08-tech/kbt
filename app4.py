import streamlit as st

st.title("simple chatbot")

Question=st.text_input("Ask me anything")

if st.button("send"):
    st.write("you asked",)