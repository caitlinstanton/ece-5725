import socket

s = socket.socket()
print "socket successfully created"

port = 6166
s.bind(('0.0.0.0',port))
print "socket binded to port %s" %(port)

s.listen(5)
print "socket is listening"

while True:
    c,addr = s.accept()
    print "got connection %s %s" %(c,addr)
    c.send("Thank you for connecting")
    c.close()
