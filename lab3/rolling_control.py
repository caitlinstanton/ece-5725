# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 3, Due 3/21

import os
import pygame
from pygame.locals import *
import RPi.GPIO as GPIO
from collections import deque
import time

# Display on TFT
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb1')
os.putenv('SDL_MOUSEDRV','TSLIB')
os.putenv('SDL_MOUSEDEV','/dev/input/touchscreen')

# Initialize pygame constants
pygame.init()
pygame.mouse.set_visible(False)
WHITE = 255,255,255
BLACK = 0,0,0
RED = 255,0,0
GREEN = 0,255,0
screen = pygame.display.set_mode((320,240))
button_font = pygame.font.Font(None,30)
data_font = pygame.font.Font(None,20)
game_buttons = {'Left History':(40,20,data_font),'Right History':(260,20,data_font),\
        'STOP':(160,80,button_font),'Quit':(160,180,button_font),'RESUME':(160,80,button_font)}
screen.fill(BLACK)

# Function for setting direction of a servo
# PWM_number is a pointer to a GPIO.PWM object
# Direction is a string equal to one of: - "stop"
#                                        - "clockwise"
#                                        - "counter-clockwise"
def set_direction(PWM_number, direction):
    # Set freq and dc based on desired direction
    if direction == "stop" or direction == "Stop":
        freq = 50
        dc = 0
    if direction == "clockwise" or direction == "Clkwise":
        freq = 46.948
        dc = 6.103
    if direction == "counter-clockwise" or direction == "Counter-Clk":
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
# "panic" button pressed
stopped = False

# Data structures for logs, initalized with "stop"
left_log = deque([])
left_log.append(("Stop", 0))
left_log.append(("Stop", 0))
left_log.append(("Stop", 0))
right_log = deque([])
right_log.append(("Stop", 0))
right_log.append(("Stop", 0))
right_log.append(("Stop", 0))

# Record initial time (for logging direction changes)
initial_time = time.time()
print("----")
print(initial_time)

# Interrupt function calls
# Each one, if the not stopped, updates the log and changes the direction
def stop(channel):
    now = time.time()
    if not stopped:
        if left:
            left_log.append(("Stop", int(now - initial_time)))
            left_log.popleft()
            set_direction(left_servo, "stop")
        else:
            right_log.append(("Stop", int(now - initial_time)))
            right_log.popleft()
            set_direction(right_servo, "stop")
def clockwise(channel):
    now = time.time()
    if not stopped:
        if left:
            left_log.append(("Clkwise", int(now - initial_time)))
            left_log.popleft()
            set_direction(left_servo, "clockwise")
        else:
            right_log.append(("Clkwise", int(now - initial_time)))
            right_log.popleft()
            set_direction(right_servo, "clockwise")
def counter_clockwise(channel):
    now = time.time()
    if not stopped:
        if left:
            left_log.append(("Counter-Clk", int(now - initial_time)))
            left_log.popleft()
            set_direction(left_servo, "counter-clockwise")
        else:
            right_log.append(("Counter-Clk", int(now - initial_time)))
            right_log.popleft()
            set_direction(right_servo, "counter-clockwise")
# Swaps which servo is being controlled
def swap_servo(channel):
    if not stopped:
        global left 
        left = not left
# Quit button callback
def exit_program(channel):
    left_servo.stop()
    right_servo.stop()
    GPIO.cleanup()
    exit()
    
# Attach interrupts to falling edges
GPIO.add_event_detect(17, GPIO.FALLING, callback=counter_clockwise, bouncetime=200)
GPIO.add_event_detect(19, GPIO.FALLING, callback=swap_servo, bouncetime=200)
GPIO.add_event_detect(22, GPIO.FALLING, callback=clockwise, bouncetime=200)
GPIO.add_event_detect(23, GPIO.FALLING, callback=stop, bouncetime=200)
GPIO.add_event_detect(27, GPIO.FALLING, callback=exit_program, bouncetime=200)

# Constants for determine coordinates to write log entries
left_coords = [(40,60), (40,100), (40,140)]
right_coords = [(260,60), (260,100), (260,140)]

# Continually update the screen
while True:   
    screen.fill(BLACK) 
    # Buttons and log headers
    for my_text, text_data in game_buttons.items(): 
        if stopped and my_text != "STOP":
            if my_text == "RESUME":
                pygame.draw.circle(screen,GREEN,(text_data[0],text_data[1]),30)
            text_surface = text_data[2].render(my_text,True,WHITE)
            rect = text_surface.get_rect(center=(text_data[0], text_data[1]))
            screen.blit(text_surface,rect)
        elif not stopped and my_text != "RESUME":
            if my_text == "STOP":
                pygame.draw.circle(screen,RED,(text_data[0],text_data[1]),30)
            text_surface = text_data[2].render(my_text,True,WHITE)
            rect = text_surface.get_rect(center=(text_data[0], text_data[1]))
            screen.blit(text_surface,rect)
    # Display left log
    for n in range(3):
        direction = left_log[n][0]
        log_time = left_log[n][1]
        text_surface = data_font.render(direction + " " + str(log_time),True,WHITE)
        rect = text_surface.get_rect(center=left_coords[n])
        screen.blit(text_surface,rect)
    # Display right log
    for n in range(3):
        direction = right_log[n][0]
        log_time = right_log[n][1]
        text_surface = data_font.render(direction + " " + str(log_time),True,WHITE)
        rect = text_surface.get_rect(center=right_coords[n])
        screen.blit(text_surface,rect)
    pygame.display.flip()
    # Check for button presses
    for event in pygame.event.get():
        if (event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif (event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if x > 140 and x < 200:
                # Stop button - if already stopped, then resume
                if y > 60 and y < 100:
                    print "STOP button pressed"
                    stopped = not stopped
                    if stopped:
                        set_direction(left_servo, "stop")
                        set_direction(right_servo, "stop")
                    else:
                        set_direction(left_servo,left_log[2][0])
                        set_direction(right_servo,right_log[2][0])
                # Cleanup and exit
                elif y > 160 and y < 200:
                    print "QUIT Button pressed"
                    left_servo.stop()
                    right_servo.stop()
                    GPIO.cleanup()
                    exit()
                
GPIO.cleanup()

