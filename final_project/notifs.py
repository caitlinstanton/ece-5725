import datetime
from twilio.rest import Client
import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

# Define constants
GPIO_pin = 13
on_time = 1.5
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))

account_sid = 'AC04b78b8dc7118d877990cb3513cfb406'
auth_token = 'bca894f066779ee1b55a0b52231993ca'
client = Client(account_sid,auth_token)

food_time = (17, 11)
current_time = (datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)
while (food_time != current_time):
    current_time = (datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)
print("Time for food!")

message = client.messages.create(
	body=current_time,
	from_='+19179946042',
	to='+16465521948'
)
#print(message.sid)

# Start PWM
p = GPIO.PWM(GPIO_pin, freq)
p.start(dc)

# Continue until quit button pressed
while GPIO.input(27):
    pass

p.stop()
GPIO.cleanup()
