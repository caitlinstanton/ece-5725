import RPi.GPIO as GPIO
import time

# Set GPIO to use BCM and as input with pull-up
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_UP)
# needs  Ctrl-C to stop
while True:
    # Check button (active low), print, then wait
    if not GPIO.input(5):
        print "Test"
        time.sleep(.200)

