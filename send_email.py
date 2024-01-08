import smtplib
import ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    context = ssl.create_default_context()
    username = "fzappuser@gmail.com"
    password = os.getenv("EMAIL_APP_PASSWORD")
    receiver = "fzebib@gmail.com"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
