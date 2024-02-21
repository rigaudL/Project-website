import streamlit as st
st.set_page_config(layout="wide") 
st.title("Welcome to my Project hosting page")
first , second = st.columns(2)

with first:
    #st.camera_input(label= "camera")
    st.image("images/download (2).jpg") # takes a img as the parameter and put it on the screen and make it an obj of "st.image()"

with second:
    text = "Hello I am Rigaud Luly and welcome to my website where I host \
            all my pojects and you can contact me."
    st.title("Rigaud Luly")
    st.write(text) # whats st.text()
    
st.text_input(label="", placeholder="My message" )

st.session_state