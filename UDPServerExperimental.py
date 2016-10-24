#UDPServerExperimental
#REQUIREMENT: Both server and client must! be instantiated with the same port number
#Launch format: must be put in CLI as "python UDPServerExperimental.py [PORT#]"
#Note: method of obtaining local IP is considered "unreliable", and as such
#this is not a perfect solution to the problem at hand.

#Credit: method for getting local IP address taken from Stack Overflow users "alexandreferris"
# and "Vinko Vrsalovic" in thread http://stackoverflow.com/a/166520
import socket

import sys

portNum = int(sys.argv[1])
ipNum = socket.gethostbyname(socket.gethostname())
print "Local IP: ", ipNum
mySocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

mySocket.bind((ipNum, portNum))

while(True):
	print "Awaiting connections..."
	data,addr = mySocket.recvfrom(1024) #sets buffer to 1024 bytes?
	print "Recieved a datagram from IP:", addr[0]
	responseSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	messageResponse = data.upper()
	#port num is addr[1] ip is addr[0]
	responseSocket.sendto(messageResponse,(addr[0],portNum))
	#print addr[0], addr[1]
	#print messageResponse