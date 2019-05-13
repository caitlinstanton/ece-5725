import socket

'''s = socket.socket()
print "socket successfully created"

port = 5725
s.bind(('',port))
print "socket binded to port %s" %(port)

s.listen(5)
print "socket is listening"
'''
def pi_zero_message(text):
    s = socket.socket()
    s.bind(('',5725))
    s.listen(5)
    c,addr = s.accept()
    print "got connection %s %s" %(c,addr)
    c.send(text)
    c.close()
