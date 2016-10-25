#TCPClientExperimental.py
#REQUIREMENTS: both server and client must have same port number specified at command line launching
#Launch format for this program is "python TCPClientExperimental.py [IP of target server] [PORT#]"

#Note: method of obtaining local IP is considered "unreliable", and as such
#this is not a perfect solution to the problem at hand.

#Credit: method for getting local IP address taken from Stack Overflow users "alexandreferris"
# and "Vinko Vrsalovic" in thread http://stackoverflow.com/a/166520

import socket

import sys

ipNum = sys.argv[1]

portNum = int(sys.argv[2])

message = raw_input("Message to send to server: ")

sendingSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sendingSocket.connect((ipNum,portNum))

while 1:	
	sendingSocket.send(message) #Send message
	data = sendingSocket.recv(1024) #Recieve server echo
	print data #print echoed data (that's been uppercased)
	message = raw_input("Message to send to server: ") #Collect next input
	
s.close()