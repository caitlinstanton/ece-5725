import socket

def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 6166
	s.connect(('10.148.2.162',port))
	print s.recv(1024)
	s.close()

if __name__=="__main__":
   connect()
