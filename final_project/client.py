import socket

s = socket.socket()
s.bind(('',5725))
s.listen(5)
c,addr = s.accept()
print "got connection %s %s" %(c,addr)
c.send(c)

while True:
    action = s.recv(1024)
    print action

'''
def client_connect():
    
    s = socket.socket()
    print "b"
    port = 5725
    print "C"
    s.connect(('128.253.17.53',port))
    print "connected"
    print s.recv(1024)
    s.close()

if __name__=="__main__":
   client_connect()'''
