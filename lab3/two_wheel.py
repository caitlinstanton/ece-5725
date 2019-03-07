# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 3, Due 3/21

import RPi.GPIO as GPIO

def set_direction(PWM_number, direction):
    if direction = "stop":
        freq = 50
        dc = 0
    if direction = "clockwise":
        freq = 46.948
        dc = 6.103
    if direction = "counter-clockwise":
        freq = 46.083
        dc = 7.834
    PWM_number.ChangeFrequency(freq)
    PWM_number.ChangeDutyCycle(dc)