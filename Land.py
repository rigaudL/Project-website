import streamlit as st

st.set_page_config("Wide")
st.title("Welcome to my Project hosting page")
first , second = st.columns(2)

with first:
    st.camera_input(label= "camera")

with second:
    st.text("HEllo i am Rigaud Luly and welcome to my website where i host \
        all my pojects and you can contact me")