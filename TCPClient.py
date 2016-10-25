#TCPClient.py
#Of note: The Client program MUST specify 127.0.0.1 in its CLI instantiation
#otherwise the traffic seems to get lost.
import socket

import sys

ipNum = sys.argv[1]

portNum = int(sys.argv[2])

message = raw_input("Message to send to server: ")

sendingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sendingSocket.connect((ipNum,portNum))

while 1:	
	sendingSocket.send(message)
	data = sendingSocket.recv(1024)
	print data
	message = raw_input("Message to send to server: ")
	
s.close()