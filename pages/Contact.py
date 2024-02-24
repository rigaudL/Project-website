import streamlit as st

st.title("Contact me")

with st.form(key="email"): #component that has other stuff inside like st.colum and must have a key inside (id for the component)
    user_email = st.text_input('your email addresss')
    
    st.info("Type Your message below")
    user_message = st.text_area("")
    
    
    button       = st.form_submit_button("SUBMIT")
    # st.form_submit_button is a boolean and returnd true or false values
    
    if button:
        print("The user has submitted the message \n")
        print(user_message)
        
