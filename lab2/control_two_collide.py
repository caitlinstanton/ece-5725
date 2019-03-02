import os
import pygame
from pygame.locals import *
import time
import RPi.GPIO as GPIO

starttime = time.time()
code_running = True #boolean for running program
game_running = False #boolean for running ball collision animation
paused = False #boolean for pausing ball collision animation
speed = 40 #framerate value for fast/slow buttons
GPIO.setmode(GPIO.BCM)
GPIO.setup(27,GPIO.IN,pull_up_down=GPIO.PUD_UP)
clock = pygame.time.Clock()

os.putenv('SDL_VIDEODRIVER','fbcon')
os.putenv('SDL_FBDEV','/dev/fb1')
os.putenv('SDL_MOUSEDRV','TSLIB')
os.putenv('SDL_MOUSEDEV','/dev/input/touchscreen')

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
my_buttons = {'start':(40,180),'quit':(240,180)}
game_buttons = {'pause':(40,180),'fast':(100,180),'slow':(160,180),'back':(220,180)}
screen.fill(BLACK)

while code_running:
    clock.tick(speed)
    screen.fill(BLACK)
    if (game_running and not paused): #ball collision displayed 
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
    if (game_running or paused): #ensures buttons will be displayed/checked whether game is paused/unpaused
        for my_text, text_pos in game_buttons.items(): #pause,fast,slow,and back buttons displayed
            text_surface = my_font.render(my_text,True,WHITE)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface,rect)
        screen.blit(ball,ball_rect) #ball,ball2 are still displayed but shouldn't move
        screen.blit(ball2,ball2_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if (event.type is MOUSEBUTTONDOWN):
                pos = pygame.mouse.get_pos()
            elif (event.type is MOUSEBUTTONUP):
                pos = pygame.mouse.get_pos()
                x,y = pos
                if y > 160:
                    if x < 60:
                        print 'pause pressed'
                        paused = not paused
                        game_running = not paused
                    elif x > 70 and x < 120:
                        print 'fast pressed'
                        speed = 80
                    elif x > 130 and x < 180:
                        print 'slow pressed'
                        speed = 20
                    elif x > 190:
                        print 'back pressed'
                        game_running = False
                        code_running = True
                        paused = False
    else:
        for my_text, text_pos in my_buttons.items(): #start,quit buttons displayed
            text_surface = my_font.render(my_text,True,WHITE)
            rect = text_surface.get_rect(center=text_pos)
            screen.blit(text_surface,rect)
    pygame.display.flip()
    for event in pygame.event.get():
        if (event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif (event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if y > 120:
                if x < 160:
                    print 'start pressed'
                    game_running = True
                    code_running = True
                else:
                    print 'quit pressed'
                    game_running = False
                    code_running = False
            else:
                my_text="Hit at " + str(pos[0]) + "," + str(pos[1])
                print my_text
                text_surface = my_font.render(my_text,True,WHITE)
                rect = text_surface.get_rect(center=(100,100))
                screen.blit(text_surface,rect)
    if not GPIO.input(27):
        code_running = False
    now = time.time()
    elapsed = now - starttime
    if elapsed >= 30:
        code_running = False

