# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 1, Due 2/21

import RPi.GPIO as GPIO
import subprocess
import time

# Set GPIO pins to use BCM and as input with pull up
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
while True:
    # Check each button, send command to fifo, and wait
    if not GPIO.input(17):
        subprocess.check_output("echo pause > video_fifo", shell = True)
        time.sleep(.200)
    if not GPIO.input(22):
        subprocess.check_output("echo seek 10 0 > video_fifo", shell = True)
        time.sleep(.200)
    if not GPIO.input(23):
        subprocess.check_output("echo seek -10 0 > video_fifo", shell = True)
        time.sleep(.200)
    if not GPIO.input(27):
        subprocess.check_output("echo quit > video_fifo", shell = True)
        break
