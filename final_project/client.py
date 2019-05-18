# Brandon Quinlan (bmq4) and Caitlin Stanton (cs968)
# ECE5725, Final Project
# Python script to be run on the Pi Zero
import socket
import RPi.GPIO as GPIO

servo = False
s = socket.socket()
# Connect to Pi 3
def connection():
    global s
    s.bind(('',5725))

# Setup GPIO and PWM
GPIO.setmode(GPIO.BCM)
GPIO.setup(3,GPIO.OUT)
freq=1000.0/21.5
p=GPIO.PWM(3,freq)
dc=100.0*(1.5/21.5)
p.start(dc)

# Wait for connection
def waiting():
    s.listen(5)
    c,addr = s.accept()
    print "got connection %s %s" %(c,addr)
    global servo
    servo = True

# Change servo position
def playFetch():
    print "yeet"
    p.ChangeFrequency(1000.0/21.0)
    p.ChangeDutyCycle(100.0*(1.0/21.0))

if __name__=="__main__":
    connection()
    while True:
        if servo:
            playFetch()
            servo = False
        else:
            waiting()
