import streamlit as st

st.title("Welcome to basic streamlit app")

age =st.slider("select your age", 1 , 100)
city =st.selectbox("select your city",["Delhi","Mumbai","Nashik"])

if st.button("show details"):
    st.write("age",age)
    