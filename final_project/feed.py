# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Final Project

import datetime
import time
from twilio.rest import Client
import RPi.GPIO as GPIO
import messages

# Update PWM signal of p
def change_PWM(on_time, p):
    freq = 1000.0/(20.0+on_time)
    dc = 100.0*(on_time/(20.0+on_time))
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(dc)
    
# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Define constants
GPIO_pin = 13
on_time = 1.2
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))
p = GPIO.PWM(GPIO_pin, freq)
p.start(dc)

# Initialize desired food time
food_time = (18,24)
current_time = (datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)
while (food_time != current_time):
    # wait for feeding time
    current_time = (datetime.datetime.now().time().hour, datetime.datetime.now().time().minute)
messages.send_sms("Time for food!")

# open tank
change_PWM(2, p)
while GPIO.input(5):
    # wait for line break
    pass
# Close tank
change_PWM(1.2, p)
time.sleep(3)

p.stop()
GPIO.cleanup()
