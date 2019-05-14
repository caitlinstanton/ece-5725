import socket

s = socket.socket()
s.bind(('',2019))
servo = False

def waiting():
    s.listen(5)
    c,addr = s.accept()
    print "got connection %s %s" %(c,addr)
    global servo
    servo = True

def playFetch():
    print "yeet"

if __name__=="__main__":
    while True:
        if servo:
            playFetch()
            servo = False
        else:
            waiting()
