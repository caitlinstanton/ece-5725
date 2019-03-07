# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 2, Due 3/7

import os
import pygame
from pygame.locals import *
import time
import RPi.GPIO as GPIO

# used for physical quit button and timeout
starttime = time.time()
code_running = True
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_UP)

# For displaying to TFT
os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb1')

# Initialize and set constants for display
pygame.init()
WHITE = 255,255,255
BLACK = 0,0,0
size = width, height = 320,240
speed = [1,1]
screen = pygame.display.set_mode((320,240))
ball = pygame.image.load('magic_ball.png')
ball_rect = ball.get_rect()
ball_rect.move(50,50)

my_font = pygame.font.Font(None,50)
my_buttons = {'button1':(80,180),'button2':(240,180)}
screen.fill(BLACK)

# Keep looping until quit button or timeout
while code_running:
    screen.fill(BLACK)
    ball_rect = ball_rect.move(speed)
    if ball_rect.left < 0 or ball_rect.right > width:
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > height:
        speed[1] = -speed[1]  
    for my_text, text_pos in my_buttons.items():
        text_surface = my_font.render(my_text,True,WHITE)
        rect = text_surface.get_rect(center=text_pos)
        screen.blit(text_surface,rect)
    screen.blit(ball,ball_rect)
    pygame.display.flip()
    if not GPIO.input(27):
        code_running = False
    now = time.time()
    elapsed = now - starttime
    # timeout of 5 seconds
    if elapsed >= 5:
        code_running = False

