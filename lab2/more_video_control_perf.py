# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 2, Due 3/7

import RPi.GPIO as GPIO
import subprocess
import time

# Used to determine timeout
time_stamp = time.time()

# Set GPIO pins to use BCM and as input with pull up
# For this lab, we added 2 external buttons, connected to GPIO 13 and 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)
# Loop until 10s has elapsed
while time.time() - time_stamp < 10:
    # Check each button, send command to fifo, and wait
    # We modified the value in sleep() to observe different CPU usages
    # time.sleep(.00002)
    if not GPIO.input(13):
        subprocess.check_output("echo seek -30 0 > video_fifo", shell = True)
        time.sleep(.200)
    if not GPIO.input(17):
        subprocess.check_output("echo pause > video_fifo", shell = True)
        time.sleep(.200)
    if not GPIO.input(22):
        subprocess.check_output("echo seek 10 0 > video_fifo", shell = True)
        time.sleep(.200)
    if not GPIO.input(23):
        subprocess.check_output("echo seek -10 0 > video_fifo", shell = True)
        time.sleep(.200)
    if not GPIO.input(26):
        subprocess.check_output("echo seek 30 0 > video_fifo", shell = True)
        time.sleep(.200)
    if not GPIO.input(27):
        subprocess.check_output("echo quit > video_fifo", shell = True)
        break

