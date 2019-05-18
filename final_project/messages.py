# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Final Project
 
from twilio.rest import Client

account_sid = 'AC4bda313b35fa302d7ec0e1ae151c8505'
auth_token = 'aff8936c41459ba1b0f98452ead78c4d'
client = Client(account_sid,auth_token)

# Send "text" to Brandon's phone
def send_sms(text):
	message = client.messages.create(
		body=text,
		from_='+17326482248',
		to='+17326093709'
	)
	print(message.sid)
send_sms("ahhh")
