import RPi.GPIO as GPIO
import time

print "hello"

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    if not GPIO.input(17):
        print "Button 17 has been pressed"
        time.sleep(.200)
