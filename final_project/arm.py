import RPi.GPIO as GPIO
import time

def change_PWM(on_time, p):
    freq = 1000.0/(20.0+on_time)
    dc = 100.0*(on_time/(20.0+on_time))
    p.ChangeFrequency(freq)
    p.ChangeDutyCycle(dc)

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(13, GPIO.OUT)

# Define constants (for stopping)
GPIO_pin = 13

on_time = 1.5
freq = 1000.0/(20.0+on_time)
dc = 100.0*(on_time/(20.0+on_time))

# Start PWM
p = GPIO.PWM(GPIO_pin, freq)
p.start(dc)
direction = False
start_time = time.time()
while time.time() < start_time+10:
    change_PWM(direction + 1, p)
    time.sleep(0.3)
    direction = not direction
p.stop()
GPIO.cleanup()
