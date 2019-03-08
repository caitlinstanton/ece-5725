# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 3, Due 3/21

import os
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
from collections import deque
import time

#os.putenv('SDL_VIDEODRIVER','fbcon')
#os.putenv('SDL_FBDEV','/dev/fb0')
#os.putenv('SDL_MOUSEDRV','TSLIB')
#os.putenv('SDL_MOUSEDEV','/dev/input/touchscreen')

pygame.init()
# pygame.mouse.set_visible(True)
WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0
screen = pygame.display.set_mode((320,240))
button_font = pygame.font.Font(None,30)
data_font = pygame.font.Font(None,20)
game_buttons = {'Left History':(40,20,data_font),'Right History':(260,20,data_font),\
        'STOP':(160,80,button_font),'Quit':(160,180,button_font)}
screen.fill(BLACK)

# Function for setting direction of a servo
# PWM_number is a pointer to a GPIO.PWM object
# Direction is a string equal to one of: - "stop"
#                                        - "clockwise"
#                                        - "counter-clockwise"
def set_direction(PWM_number, direction):
    # Set freq and dc based on desired direction
    if direction == "stop":
        freq = 50
        dc = 0
    if direction == "clockwise":
        freq = 46.948
        dc = 6.103
    if direction == "counter-clockwise":
        freq = 46.083
        dc = 7.834
    # Update servo with new values
    PWM_number.ChangeFrequency(freq)
    PWM_number.ChangeDutyCycle(dc)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(26,GPIO.OUT)
GPIO.setup(17,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(19,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(27,GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Initialize servo objects
left_servo = GPIO.PWM(13, 50)
right_servo = GPIO.PWM(26, 50)
left_servo.start(0)
right_servo.start(0)

# Left vs Right servo selected
left = False
stopped = False

left_log = deque([])
left_log.append(("Stop", 0))
left_log.append(("Stop", 0))
left_log.append(("Stop", 0))
right_log = deque([])
right_log.append(("Stop", 0))
right_log.append(("Stop", 0))
right_log.append(("Stop", 0))

initial_time = time.time()

# Interrupt function calls
def stop(channel):
    if not stopped:
        if left:
            left_log.append(("Stop", int(time.time() - initial_time)))
            left_log.popleft()
            set_direction(left_servo, "stop")
        else:
            right_log.append(("Stop", int(time.time() - initial_time)))
            right_log.popleft()
            set_direction(right_servo, "stop")
def clockwise(channel):
    if not stopped:
        if left:
            left_log.append(("Clkwise", int(time.time() - initial_time)))
            left_log.popleft()
            set_direction(left_servo, "clockwise")
        else:
            right_log.append(("Clkwise", int(time.time() - initial_time)))
            right_log.popleft()
            set_direction(right_servo, "clockwise")
def counter_clockwise(channel):
    if not stopped:
        if left:
            left_log.append(("Counter-Clk", int(time.time() - initial_time)))
            left_log.popleft()
            set_direction(left_servo, "counter-clockwise")
        else:
            right_log.append(("Counter-Clk", int(time.time() - initial_time)))
            right_log.popleft()
            set_direction(right_servo, "counter-clockwise")
def swap_servo(channel):
    if not stopped:
        global left 
        left = not left
    
# Attach interrupts to falling edges
GPIO.add_event_detect(17, GPIO.FALLING, callback=counter_clockwise, bouncetime=200)
GPIO.add_event_detect(19, GPIO.FALLING, callback=swap_servo, bouncetime=200)
GPIO.add_event_detect(22, GPIO.FALLING, callback=clockwise, bouncetime=200)
GPIO.add_event_detect(23, GPIO.FALLING, callback=stop, bouncetime=200)

left_coords = [(40,60), (40,100), (40,160)]
right_coords = [(260,60), (260,100), (260,160)]
code_running = True
while code_running:    
    for my_text, text_data in game_buttons.items(): 
        text_surface = text_data[2].render(my_text,True,WHITE)
        rect = text_surface.get_rect(center=(text_data[0], text_data[1]))
        screen.blit(text_surface,rect)
    for n in range(3):
        direction = left_log[n][0]
        time = left_log[n][1]
        text_surface = data_font.render(direction + " " + str(time),True,WHITE)
        rect = text_surface.get_rect(center=left_coords[n])
        screen.blit(text_surface,rect)
    for n in range(3):
        direction = right_log[n][0]
        time = right_log[n][1]
        text_surface = data_font.render(direction + " " + str(time),True,WHITE)
        rect = text_surface.get_rect(center=right_coords[n]
        screen.blit(text_surface,rect)
    pygame.display.flip()
    if not GPIO.input(27):
        code_running = False
left_servo.stop()
right_servo.stop()
GPIO.cleanup()