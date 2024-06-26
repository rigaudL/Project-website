import streamlit as st
import pandas 
st.set_page_config(layout="wide") 


st.title("Welcome to my Project hosting page")
first , second = st.columns(2)

with first:
    st.image("ME.img", width = 490   )

with second:
    text = "Hello! My name is Rigaud Luly, and I'm thrilled to welcome you to my portfolio website. Here, I showcase a diverse range of projects that I've worked on, spanning various technologies and industries. Whether you're here to explore my projects, learn more about my skills and experiences, or get in touch for potential collaboration opportunities, I'm excited to have you here. Feel free to browse through my portfolio and don't hesitate to reach out—I'm always eager to connect and discuss new opportunities. Welcome, and thank you for visiting!"

    st.title("Me")
    st.info(text)
    
st.info("Below, you'll discover a curated collection of my projects, each accompanied by detailed descriptions and direct links for further exploration. From web applications to machine learning models, these projects showcase my expertise and passion for technology. I invite you to delve into each project, explore its intricacies, and witness the creativity and innovation that went into its development. Whether you're a fellow enthusiast, potential employer, or simply curious explorer, I hope you find inspiration and insight in my work. Dive in, and let's embark on a journey through innovation together!")

df = pandas.read_csv("data2.csv", sep = ";")

col3 , space_col, col4 = st.columns([1.5 , 0.5 , 1.5])

with col3:
    for index, row in df[3:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source Code]({row['url']})")
        
with space_col:
    pass
with col4:
    for index, row in df[:3].iterrows():
        st.header(row["title"]) 
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[source Code]({row['url']})")
        
        
        

    