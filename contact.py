import smtplib, ssl

# smtplib Is used to send emails
#ssl is used to keep things 
host = "smtp.gmail.com"
port = 465
username = "Rigaudluly21@gmail.com"
password = "nrqyfixwpsbvkmby"

receiver = "Rigaudlulynil@gmail.com"

context = ssl.create_default_context()
message = """
Hi how are you

ok?


"""

with smtplib.SMTP_SSL(host, port , context= context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message )