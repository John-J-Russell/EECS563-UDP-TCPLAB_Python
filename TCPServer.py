#TCPServer.py

import socket

import sys

ipNum = "127.0.0.1"
portNum = int(sys.argv[1])

bufferSize = 1024 #caps buffer at 1024 bytes?

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mySocket.bind((ipNum,portNum))

mySocket.listen(1)

conn, addr = mySocket.accept()


while 1:
	data = conn.recv(bufferSize)
	if not data: break
	print "recieved data:", data
	conn.send(data.upper()) #echos data back to sender? Or an ACK?
conn.close() #will close connection if while loop breaks
