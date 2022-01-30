import smtplib
import ssl
from email.message import EmailMessage

sender_email = input("What is your email? ")
receiver_email = input("Who would you like to send this email to? ")
password = input("Enter your password: ")
subject = input("What is your subject line? ")
body = input("What is the message? ")
message = EmailMessage()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = subject
message.set_content(body)

context = ssl.create_default_context()

print("Sending Email!")

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())

print("Email Sent")