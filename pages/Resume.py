

import streamlit as st
st.set_page_config(layout="wide") 


st.title("Full Stack Developer Resume")
first , second = st.columns(2)

with first:
    #st.camera_input(label= "camera")
    st.image("Resume.img", width = 800  ) # takes a img as the parameter and put it on the screen and make it an obj of "st.image()"
