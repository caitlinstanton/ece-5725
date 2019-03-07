# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 3, Due 3/21

import RPi.GPIO as GPIO
#import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)
GPIO_pin = 13
freq = 46.5116279
dc = 6.97674419

p = GPIO.PWM(GPIO_pin, freq)
p.start(dc)

'''time.sleep(5.0)

freq = 1000.0/(20.0+1.3)
dc = 100.0*(1.3/(21.3))
p.ChangeFrequency(freq)
p.ChangeDutyCycle(dc)
time.sleep(5.0)

freq = 1000.0/(21.7)
dc = 100.0*(1.7/(21.7))
p.ChangeFrequency(freq)
p.ChangeDutyCycle(dc)
time.sleep(5.0)
'''

while GPIO.input(27):
    pass

p.stop()
GPIO.cleanup()
