import streamlit as st


st.title("Simple Registration Form")


with st.form("my_form"):
    
    name = st.text_input("Enter your Name")
    email = st.text_input("Enter your Email")
    age = st.number_input("Enter your Age", min_value=1, max_value=100)
    gender = st.radio("Select Gender", ["Male", "Female", "Other"])
    
    submit = st.form_submit_button("Submit")


if submit:
    st.success("Form Submitted Successfully!")
    st.write("### Submitted Details:")
    st.write("Name:", name)
    st.write("Email:", email)
    st.write("Age:", age)
    st.write("Gender:", gender)