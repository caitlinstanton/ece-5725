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
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0
screen = pygame.display.set_mode((320,240))

panic_resume = "panic stop"
game_buttons = {'clockwise':(40,180),'counter':(130,180),'stop':(210,180), \
    'swap':(280,180),panic_resume:(40,80),'quit':(280,80)}
screen.fill(BLACK)

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

left = False
code_running = True

def stop():
    print "button 23"
    if left:
        set_direction(left_servo, "stop")
    else:
        set_direction(right_servo, "stop")
def clockwise():
    print "button 22"
    if left:
        set_direction(left_servo, "clockwise")
    else:
        set_direction(right_servo, "clockwise")
def counter_clockwise():
    print "button 17"
    if left:
        set_direction(left_servo, "counter-clockwise")
    else:
        set_direction(right_servo, "counter-clockwise")
def swap_servo():
    print "button 19"
    global left 
    left = not left

while code_running:    
    screen.fill(BLACK)
    for my_text, text_pos in game_buttons.items(): 
        if my_text == "panic stop":
            text_surface = my_font.render(my_text,True,RED)
        else if my_text == "resume":
            text_surface = my_font.render(my_text,True,GREEN)
        else:
            text_surface = my_font.render(my_text,True,WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface,rect)


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


