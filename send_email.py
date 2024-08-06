import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "yuranazarkevych767@gmail.com"
password = "fzwz bhdg tsbn dzjo"

receiver = "yuranazarkevych767@gmail.com"
my_context = ssl.create_default_context()

message = """\
Subject: Job offer
Hi!
How are you?
Bye!
"""
with smtplib.SMTP_SSL(host, port, context=my_context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
