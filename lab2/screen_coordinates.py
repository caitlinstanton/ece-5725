# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 2, Due 3/7

import os
import pygame
from pygame.locals import *
import time
import RPi.GPIO as GPIO

# Initialize variables for quit button and timeout
starttime = time.time()
code_running = True
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_UP)
clock = pygame.time.Clock()

# Display on TFT
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb1')
os.putenv('SDL_MOUSEDRV','TSLIB')
os.putenv('SDL_MOUSEDEV','/dev/input/touchscreen')

# Initialze display constants
pygame.init()
pygame.mouse.set_visible(False)
WHITE = 255,255,255
BLACK = 0,0,0
size = width, height = 320,240
speed = [5,5]
speed2 = [7,7]
screen = pygame.display.set_mode((320,240))
hit_text = ""

my_font = pygame.font.Font(None,30)
my_buttons = {'start':(80,180),'quit':(240,180)}
screen.fill(BLACK)

# Run until timeout, or either quit button is pressed
while code_running:
    clock.tick(40)
    screen.fill(BLACK)
    # Display buttons
    for my_text, text_pos in my_buttons.items():
        text_surface = my_font.render(my_text,True,WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface,rect)
    # Check buttons
    for event in pygame.event.get():
        if (event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif (event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if y > 160:
                if x < 120:
                    print 'start pressed'
                elif x > 220:
                    print 'quit button pressed'
                    code_running = False
            else:
                # Display "hit"
                if (hit_text != ""):
                    text_surface = my_font.render(hit_text,True,WHITE)
                    rect = text_surface.get_rect(center=(100,100))
                    screen.blit(text_surface,rect)
    pygame.display.flip()
    # Check physical button and timeout
    if not GPIO.input(27):
        code_running = False
    now = time.time()
    elapsed = now - starttime
    if elapsed >= 30:
        code_running = False

