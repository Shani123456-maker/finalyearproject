import socket
from socket import *
from termcolor import colored

s = socket(AF_INET,SOCK_STREAM)
s.settimeout(2)

print("Wellcome to the Port Scanner")
host = input("[*] Enter Host Ip Address: ") #Gets the host port from user

def scanner(port):
    if s.connect_ex((host,port)):
         print(colored("[!!] Port %d is close" % (port), 'red')) # shows the closed port
    else:
         print(colored("[*] Port %d is open" % (port),'green')) # shows the open port

for port in range(1000):
    scanner(port)
