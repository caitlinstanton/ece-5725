import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(13,GPIO.OUT)

p = GPIO.PWM(13,1000.0/21.5)
p.start(0)
