from twilio.rest import Client
import socket

account_sid = 'ACca7bb1631080e074755b158782952729'
auth_token = '7b033d60148eb46db0b0db6a6e3df06e'
client = Client(account_sid,auth_token)

def send_sms(text):
	message = client.messages.create(
		body=text,
		from_='+19179050866',
		to='+16465521948'
	)
	print(message.sid)