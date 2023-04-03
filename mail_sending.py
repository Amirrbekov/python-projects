import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

message = MIMEMultipart()

message["From"] = "amirbekovaleh@gmail.com"

message["To"] = "amirbekovvaleh04@icloud.com"

message["Subject"] = "Smtp main sending"

words = """

Sending mail with Smtp.

Valeh Amirbekov Aydin

"""

message_body = MIMEText(words,"plain")

message.attach(message_body)

try:
    mail = smtplib.SMTP("smtp.gmail.com",587)

    mail.ehlo()

    mail.starttls()

    mail.login("","")

    mail.sendmail(message["From"],message["To"],message.as_string())

    print("Mail sended in successfull....")

    mail.close()

except:
    sys.stderr.write("Something went wrong!")
    sys.stderr.flush()