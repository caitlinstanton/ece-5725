# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 3, Due 3/21

import RPi.GPIO as GPIO

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

# Define constants (for stopping)
GPIO_pin = 13
freq = 46.5116279
dc = 6.97674419

# Start PWM
p = GPIO.PWM(GPIO_pin, freq)
p.start(dc)

# Continue until quit button pressed
while GPIO.input(27):
    pass

p.stop()
GPIO.cleanup()
