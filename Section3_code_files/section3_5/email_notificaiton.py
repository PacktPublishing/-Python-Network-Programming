#!/usr/bin/env python3

import smtplib, os, email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = int(os.environ.get('MAIL_PORT', '587'))
MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

server = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
server.ehlo()
server.starttls()
server.ehlo()
server.login(MAIL_USERNAME, MAIL_PASSWORD)

msg = MIMEMultipart()
msg['Subject'] = "Notification Email"
body = "This is to notify You of Something"
msg.attach(MIMEText(body, 'plain'))
text = msg.as_string()


server.sendmail("ericc@a10networks.com", "eric@pythonicneteng.com", text)


