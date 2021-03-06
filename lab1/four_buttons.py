# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 1, Due 2/21

import RPi.GPIO as GPIO
import time

# Set GPIO pins to use BCM and as inputs with pull-up
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    # Check each of the buttons, print, then wait
    if not GPIO.input(17):
        print "Button 17 has been pressed"
        time.sleep(.200)
    if not GPIO.input(22):
        print "Button 22 has been pressed"
        time.sleep(.200)
    if not GPIO.input(23):
        print "Button 23 has been pressed"
        time.sleep(.200)
    if not GPIO.input(27):
        print "Buttin 27 has been pressed"
        break
