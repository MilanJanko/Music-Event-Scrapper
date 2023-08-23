import smtplib, ssl
import envvar
from email.message import EmailMessage


def send_email(message):
    host = 'smtp.gmail.com'
    port = 465
    context = ssl.create_default_context()

    username = envvar.username
    password = envvar.password
    receiver = envvar.receiver

    msg = EmailMessage()
    msg['Subject'] = 'New Music Event'
    msg['From'] = 'Milan Jankovic'
    msg.set_content(message)

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, msg.as_string())
