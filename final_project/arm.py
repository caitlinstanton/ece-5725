import RPi.GPIO as GPIO

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

# Continue until quit button pressed
while GPIO.input(27):
    pass

p.stop()
GPIO.cleanup()
