import smtplib, ssl
import os 


def send_email(username, message):

    host = "smtp.gmail.com"
    port = 465
    username = "Rigaudluly21@gmail.com"
    password = os.getenv("Password")

    receiver = username
     
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port , context= context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message )