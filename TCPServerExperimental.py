#TCPServerExperimental
#REQUIREMENT: Both server and client !must! be instantiated with the same port number
#Launch format: must be put in CLI as "python TCPServerExperimental.py [PORT#]"
#Note: method of obtaining local IP is considered "unreliable", and as such
#this is not a perfect solution to the problem at hand.

#Credit: method for getting local IP address taken from Stack Overflow users "alexandreferris"
# and "Vinko Vrsalovic" in thread http://stackoverflow.com/a/166520
import socket

import sys

ipNum = socket.gethostbyname(socket.gethostname())
print "Local IP: ",ipNum
portNum = int(sys.argv[1])

bufferSize = 1024 #caps buffer at 1024 bytes?

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.bind((ipNum,portNum))

mySocket.listen(1)

conn, addr = mySocket.accept()


while 1:
	data = conn.recv(bufferSize)
	if not data: break 
	print "Recieved data from IP:" ,addr[0]
	conn.send(data.upper()) #echos data back to sender
conn.close() #will close connection if while loop breaks
