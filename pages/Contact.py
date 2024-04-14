import streamlit as st
import backend_contact as bc


st.title("Contact me")

with st.form(key="email"):
    user_email = st.text_input('your email addresss')
    
    st.info("Type Your message below")
    user_message = st.text_area("")
    user_message = f"""\\Subject:New mail from {user_email}

From ---> {user_email}
{user_message}
        
        """
    
    button       = st.form_submit_button("SUBMIT")
    
    if button:
        bc.send_email(user_email ,user_message)
        st.info("Email was sent Succesfully")