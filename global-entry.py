#!/usr/local/bin/python3

import requests
import smtplib, ssl
import datetime

locations = ['5180', '5002', '16525']

ct = datetime.datetime.now()
end_date = ct + datetime.timedelta(days=30)
str_date_time = end_date.strftime("%Y-%m-%d")

payload = {'serviceName': 'Global Entry', 'filterTimestampBy': 'before', 'timestamp' : str_date_time}

r = requests.get('https://ttp.cbp.dhs.gov/schedulerapi/slots/asLocations', params=payload)

availableLocations = []

for i in r.json():
	if str(i['id']) in locations: availableLocations.append(i['city'] + ', ' + i['state'])

if (len(availableLocations) == 0):
	print(str_date_time + ' No available times')
	quit()

nowTimestamp = ct.timestamp();
try:
	with open('GE-timestamp.txt', 'r') as f:
		contents = f.read()
		waitTimestamp = float(contents)
		if (waitTimestamp > nowTimestamp):
			print('waiting')
			quit()
except FileNotFoundError:
	print("timestamp file not created yet.")

port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "XXX@gmail.com"
receiver_email = "XXX@gmail.com"
app_email_password = "XXX-app-password"
message = """\
Subject: Open Global Entry Interview at """ + str(availableLocations) + """

login here: https://ttp.cbp.dhs.gov/
"""
context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, app_email_password)
    server.sendmail(sender_email, receiver_email, message)

waitTime = ct + datetime.timedelta(minutes=5)
waitTime = waitTime.timestamp()

with open('GE-timestamp.txt', 'w') as f:
	f.write(str(waitTime))
