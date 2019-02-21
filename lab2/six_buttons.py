# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 2, Due 3/7

import RPi.GPIO as GPIO
import time

# Set GPIO pins to use BCM and as inputs with pull-up
# For this lab, we added 2 external buttons, connected to GPIO 13 and 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    # Check each of the buttons, print, then wait
    if not GPIO.input(13):
        print "Button 13 has been pressed"
        time.sleep(.200)
    if not GPIO.input(17):
        print "Button 17 has been pressed"
        time.sleep(.200)
    if not GPIO.input(22):
        print "Button 22 has been pressed"
        time.sleep(.200)
    if not GPIO.input(23):
        print "Button 23 has been pressed"
        time.sleep(.200)
    if not GPIO.input(26):
        print "Button 26 has been pressed"
        time.sleep(.200)
    if not GPIO.input(27):
        print "Buttin 27 has been pressed"
        break
