# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 3, Due 3/21

import os
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO

os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb0')
os.putenv('SDL_MOUSEDRV','TSLIB')
os.putenv('SDL_MOUSEDEV','/dev/input/touchscreen')

pygame.init()
pygame.mouse.set_visible(False)
WHITE = 255,255,255
screen = pygame.display.set_mode((320,240))

def set_direction(PWM_number, direction):
    if direction == "stop":
        freq = 50
        dc = 0
    if direction == "clockwise":
        freq = 46.948
        dc = 6.103
    if direction == "counter-clockwise":
        freq = 46.083
        dc = 7.834
    PWM_number.ChangeFrequency(freq)
    PWM_number.ChangeDutyCycle(dc)

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)

left_servo = GPIO.PWM(13, 50)
right_servo = GPIO.PWM(26, 50)
left_servo.start(0)
right_servo.start(0)

GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)

left = False

def stop(channel):
    print "button 23"
    if left:
        set_direction(left_servo, "stop")
    else:
        set_direction(right_servo, "stop")
def clockwise(channel):
    print "button 22"
    if left:
        set_direction(left_servo, "clockwise")
    else:
        set_direction(right_servo, "clockwise")
def counter_clockwise(channel):
    print "button 17"
    if left:
        set_direction(left_servo, "counter-clockwise")
    else:
        set_direction(right_servo, "counter-clockwise")
def swap_servo(channel):
    print "button 19"
    global left 
    left = not left
    

GPIO.add_event_detect(17, GPIO.FALLING, callback=counter_clockwise, bouncetime=200)
GPIO.add_event_detect(19, GPIO.FALLING, callback=swap_servo, bouncetime=200)
GPIO.add_event_detect(22, GPIO.FALLING, callback=clockwise, bouncetime=200)
GPIO.add_event_detect(23, GPIO.FALLING, callback=stop, bouncetime=200)

try:
    GPIO.wait_for_edge(27, GPIO.FALLING)
except KeyboardInterrupt:
    GPIO.cleanup()
left_servo.stop()
right_servo.stop()
GPIO.cleanup()


