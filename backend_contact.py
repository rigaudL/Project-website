import smtplib, ssl
import os 
import streamlit as st


def send_email(username, message):

    host = "smtp.gmail.com"
    port = 465
    username = "Rigaudluly21@gmail.com"
   # password = os.getenv("SMTP_PASSWORD")
    password = st.secrets["Password"]

    receiver = username
     
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port , context= context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message )