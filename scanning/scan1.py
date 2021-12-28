import socket
from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.settimeout(2)

print("Wellcome to the Port Scanner")
host = input("[*] Enter Host Ip Address: ")
port = int(input("[*] Enter Host Port Scan: "))

def scanner(port):
    if s.connect_ex((host,port)):
        print("Port %d is close" % (port))
    else:
         print("Port %d is open" % (port))

scanner(port)
