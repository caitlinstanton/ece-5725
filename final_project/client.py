import socket

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

if __name__=="__main__":
   client_connect()
