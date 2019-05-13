import socket

s = socket.socket()

port = 6166

s.connect(('10.148.2.162',port))

print s.recv(1024)

s.close()
