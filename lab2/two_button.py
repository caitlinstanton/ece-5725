# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 2, Due 3/7

import os
import pygame
from pygame.locals import *
import time
import RPi.GPIO as GPIO

# Initialize variables for quit conditions
starttime = time.time()
code_running = True
game_running = False
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_UP)
clock = pygame.time.Clock()

# Display to TFT and use touchscreen
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
speed = [5,5]
speed2 = [7,7]
screen = pygame.display.set_mode((320,240))
ball = pygame.image.load('magic_ball.png')
ball2 = pygame.image.load('ledlightblue.png')
ball_rect = ball.get_rect(center=(50,50))
ball2_rect = ball2.get_rect(center=(100,100))


my_font = pygame.font.Font(None,30)
my_buttons = {'start':(80,180),'quit':(240,180)}
screen.fill(BLACK)

# Continue running until quit button or timeout
while code_running:
    # Use this to slow down the balls
    clock.tick(40)
    screen.fill(BLACK)
    # Update balls
    if (game_running):
        ball_rect = ball_rect.move(speed)
        ball2_rect = ball2_rect.move(speed2)
        if ball_rect.left < 0 or ball_rect.right > width:
            speed[0] = -speed[0]
        if ball_rect.top < 0 or ball_rect.bottom > height:
            speed[1] = -speed[1]
        if ball2_rect.left < 0 or ball2_rect.right > width:
            speed2[0] = -speed2[0]
        if ball2_rect.top < 0 or ball2_rect.bottom > height:
            speed2[1] = -speed2[1]
        if ball_rect.colliderect(ball2_rect):
            speed[0] = -speed[0]
            speed[1] = -speed[1]
            speed2[0] = -speed2[0]
            speed2[1] = -speed[1]
        screen.blit(ball,ball_rect)
        screen.blit(ball2,ball2_rect)
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
                    print 'button1 pressed'
                    game_running = True
                elif x > 220:
                    print 'quit button pressed'
                    code_running = False
            else:
                my_text="Hit at " + str(pos[0]) + "," + str(pos[1])
                print my_text
                text_surface = my_font.render(my_text,True,WHITE)
                rect = text_surface.get_rect(center=(100,100))
                screen.blit(text_surface,rect)
    pygame.display.flip()
    # Check quit conditions
    if not GPIO.input(27):
        code_running = False
    now = time.time()
    elapsed = now - starttime
    if elapsed >= 30:
        code_running = False

