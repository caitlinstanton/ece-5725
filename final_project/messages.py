from twilio.rest import Client
import socket

account_sid = 'AC04b78b8dc7118d877990cb3513cfb406'
auth_token = 'bca894f066779ee1b55a0b52231993ca'
client = Client(account_sid,auth_token)

def send_sms(text):
	message = client.messages.create(
		body=text,
		from_='+19179946042',
		to='+16465521948'
	)
	print(message.sid)