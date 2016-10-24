#UDPServer.py

import socket

import sys

portNum = int(sys.argv[1])
ipNum = "127.0.0.1"

mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mySocket.bind((ipNum, portNum))

while(True):
	data,addr = mySocket.recvfrom(1024) #sets buffer to 1024 bytes?
	print "Recieved a datagram from IP:", addr[0]
	#print "address sent from: ",addr[0],"Port number: ",addr[1], "Data recieved: ",data
	responseSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	messageResponse = data.upper()
	#port num is addr[1] ip is addr[0]
	responseSocket.sendto(messageResponse,(addr[0],addr[1]))