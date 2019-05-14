import socket

s = socket.socket()
s.bind(('',2019))
servo = False

GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.OUT)
freq=1000.0/21.5
p=GPIO.PWM(2,freq)
dc=100.0*(1.5/21.5)
p.start(dc)

def waiting():
    s.listen(5)
    c,addr = s.accept()
    print "got connection %s %s" %(c,addr)
    global servo
    servo = True

def playFetch():
    print "yeet"
    p.ChangeFrequency(1000.0/21.0)
    p.ChangeDutyCycle(100.0*(1.0/21.0))

if __name__=="__main__":
    while True:
        if servo:
            playFetch()
            servo = False
        else:
            waiting()
