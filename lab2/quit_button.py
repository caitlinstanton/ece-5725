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

# Display on TFT
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb1')
os.putenv('SDL_MOUSEDRV','TSLIB')
os.putenv('SDL_MOUSEDEV','/dev/input/touchscreen')

# Initialize display constants
pygame.init()
pygame.mouse.set_visible(False)
WHITE = 255,255,255
BLACK = 0,0,0
size = width, height = 320,240
screen = pygame.display.set_mode((320,240))
my_font = pygame.font.Font(None,30)
my_buttons = {'quit':(80,180)}
screen.fill(BLACK)

# Run until timeout, physical quit button, or touchscreen button pressed
while code_running:
    screen.fill(BLACK)
    for my_text, text_pos in my_buttons.items():
        text_surface = my_font.render(my_text,True,WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface,rect)
    pygame.display.flip()
    # Check touchscreen button
    for event in pygame.event.get():
        if (event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif (event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if y > 120:
                if x < 160:
                    print 'button1 pressed'
                    code_running = False
    # Check physical button and timeout
    if not GPIO.input(27):
        code_running = False
    now = time.time()
    elapsed = now - starttime
    if elapsed >= 10:
        code_running = False

