import socket

def connect():
	s = socket.socket()
	port = 6166
	s.connect(('10.148.2.162',port))
	print s.recv(1024)
	s.close()

if __name__=="__main__":
   connect()
