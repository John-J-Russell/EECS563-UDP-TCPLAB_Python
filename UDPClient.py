# UDPClient.py
#Of note: The Client program MUST specify 127.0.0.1 in its CLI instantiation
#otherwise the traffic seems to get lost.

import socket

import sys

ipNum = sys.argv[1]

portNum = int(sys.argv[2])

while True:

	message = raw_input("Message to send to server: ")

	sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	sendSocket.sendto(message, (ipNum, portNum))
	
	data,addr = sendSocket.recvfrom(1024)
	
	print "response from server with IP: ",addr[0]
	
	print data
	