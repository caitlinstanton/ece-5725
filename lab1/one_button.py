# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 1, Due 2/21

import RPi.GPIO as GPIO
import time

# Set GPIO to use BCM and as input with pull-up
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
# needs  Ctrl-C to stop
while True:
    # Check button (active low), print, then wait
    if not GPIO.input(17):
        print "Button 17 has been pressed"
        time.sleep(.200)
