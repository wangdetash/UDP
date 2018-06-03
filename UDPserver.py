
from socket import * 

serverSocket = socket(AF_INET, SOCK_DGRAM) 
serverSocket.bind(('', 12000))

while 1:
	data, address = serverSocket.recvfrom(1024)
	print data
