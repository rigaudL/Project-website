import streamlit as st
import pandas 
st.set_page_config(layout="wide") 
st.title("Welcome to my Project hosting page")
first , second = st.columns(2)

with first:
    #st.camera_input(label= "camera")
    st.image("download (2).jpg", width = 300) # takes a img as the parameter and put it on the screen and make it an obj of "st.image()"

with second:
    text = "Hello I am Rigaud Luly and welcome to my website where I host \
            all my pojects and you can contact me."

    st.title("Rigaud Luly")
    st.info(text) # whats st.text()? .write() lets me write whats in () on screen
    
st.info("Below you can find my contact information!")

df = pandas.read_csv("data.csv", sep = ";")

col3 , space_col, col4 = st.columns([1.5 , 0.5 , 1.5])

with col3:
    for index, row in df[10:].iterrows():
        st.header(row["title"]) # could be .write as well but .header gives me a bold header text \
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[source Code]()")
        
with space_col:
    pass
with col4:
    for index, row in df[:10].iterrows():
        st.header(row["title"]) # could be .write as well but .header gives me a bold header text \
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write("[source Code]()")
        
        
        

    