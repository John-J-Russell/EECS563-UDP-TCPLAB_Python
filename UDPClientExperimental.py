#UDPClientExperimental

import socket

import sys

ipNum = sys.argv[1]

portNum = int(sys.argv[2])

recieveSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
recieveSocket.bind((socket.gethostbyname(socket.gethostname()), portNum))
while True:

	message = raw_input("Message to send to server: ")

	sendSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	
	sendSocket.sendto(message, (ipNum, portNum))
	#
	#print sendSocket.getsockname()[0] #Prints zeros?
	#
	data,addr = recieveSocket.recvfrom(1024)
	
	print "response from server with IP: ",addr[0]
	
	print data
	