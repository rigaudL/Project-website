import smtplib, ssl

# smtplib Is used to send emails
#ssl is used to keep things 
host = "smtp.gmail.com"

username = "Rigaudluly21@gmail.com"
password = "nrqy fixw psbv kmby"

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port , context= context) as server:
    server.login()
    server.sendmail()