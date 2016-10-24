# UDPClient.py

import socket

import sys

ipNum = sys.argv[1]

portNum = int(sys.argv[2])

#recieveSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#recieveSocket.bind(("127.0.0.2", portNum))
while True:

	message = raw_input("Message to send to server: ")

	sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	sendSocket.sendto(message, (ipNum, portNum))
	#
	print sendSocket.getsockname()[0] #Prints zeros?
	#
	data,addr = sendSocket.recvfrom(1024)
	
	print "response from server with IP: ",addr[0]
	
	print data
	