

import streamlit as st
st.set_page_config(layout="wide") 


st.title("Full Stack Developer Resume")
first , second = st.columns(2)

with first:
    st.image("Resume.img", width = 800  )
