# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Lab 3, Due 3/21

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO_pin = 13
on_time = 1.5
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))

p = GPIO.PWM(GPIO_pin, freq)
p.start(dc)
print("Stopped")
time.sleep(3.0)

print("Clockwise")
for i in range(10):
    on_time = on_time - 0.01 
    freq = 1000.0/(20.0+on_time)
    dc = 100.0*(on_time/(20.0+on_time))
    print("\nPulse width: " + str(on_time))
    print("Duty cycle: " + str(dc))
    print("Frequency: " + str(freq))
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(dc)
    time.sleep(3.0)
     
on_time = 1.5

print ("Counter-clockwise")
for i in range(10):
    on_time = on_time + 0.01 
    freq = 1000.0/(20.0+on_time)
    dc = 100.0*(on_time/(20.0+on_time))
    print("\nPulse width: " + str(on_time))
    print("Duty cycle: " + str(dc))
    print("Frequency: " + str(freq))
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(dc)
    time.sleep(3.0)

on_time = 1.5
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))
p.ChangeFrequency(freq)
p.ChangeDutyCycle(dc)
time.sleep(3.0)

p.stop()
GPIO.cleanup()
