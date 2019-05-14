import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
freq=1000.0/21.5
p=GPIO.PWM(2,freq)
dc=100.0*(1.5/21.5)
p.start(dc)
time.sleep(3)
p.ChangeFrequency(1000.0/22.0)
p.ChangeDutyCycle(100.0*(2.0/22.0))
print("2")
time.sleep(3)
p.ChangeFrequency(1000.0/21.0)
p.ChangeDutyCycle(100.0*(1.0/21.0))
print("3")
