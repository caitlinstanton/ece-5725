import socket

<<<<<<< HEAD
def connect():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	port = 6166
	s.connect(('10.148.2.162',port))
	print s.recv(1024)
	s.close()
=======
def client_connect():
    print "a"
    s = socket.socket()
    print "b"
    port = 5725
    print "C"
    s.connect(('128.253.17.10',port))
    print "connected"
    print s.recv(1024)
    s.close()
>>>>>>> 5c992a3ef1d2d1295552c77d1395e853b2e1bec1

if __name__=="__main__":
   client_connect()
