# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 2, Due 3/7

import RPi.GPIO as GPIO
import subprocess

# Set GPIO pins to use BCM and as input with pull up
# For this lab, we added 2 external buttons, connected to GPIO 13 and 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)

def rewind30(channel):
    subprocess.check_output("echo seek -30 0 > video_fifo", shell=True)
def pause(channel):
    subprocess.check_output("echo pause > video_fifo", shell=True)
def ff10(channel):
    subprocess.check_output("echo seek 10 0 > video_fifo", shell=True)
def rewind10(channel):
    subprocess.check_output("echo seek -10 0 > video_fifo", shell=True)
def ff30(channel):
    subprocess.check_output("echo seek 30 0 > video_fifo", shell=True)

GPIO.add_event_detect(13, GPIO.FALLING, callback=rewind30, bouncetime=200)
GPIO.add_event_detect(17, GPIO.FALLING, callback=pause, bouncetime=300)
GPIO.add_event_detect(22, GPIO.FALLING, callback=ff10, bouncetime=200)
GPIO.add_event_detect(23, GPIO.FALLING, callback=rewind10, bouncetime=200)
GPIO.add_event_detect(26, GPIO.FALLING, callback=ff30, bouncetime=200)

try:
    GPIO.wait_for_edge(27, GPIO.FALLING, timeout=10000)
#    subprocess.check_output("echo quit > video_fifo", shell=True)
except KeyboardInterrupt:
    GPIO.cleanup()
GPIO.cleanup()

