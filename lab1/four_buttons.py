import RPi.GPIO as GPIO
import time

print "hello"

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    time.sleep(.200)
    if not GPIO.input(17):
        print "Button 17 has been pressed"
    if not GPIO.input(22):
        print "Button 22 has been pressed"
    if not GPIO.input(23):
        print "Button 23 has been pressed"
    if not GPIO.input(27):
        print "Buttin 27 has been pressed"
        break
