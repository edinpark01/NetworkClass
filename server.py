#   Client/Server Socket Interaction in UDP
#   Author: Braulio Tonaco
#   Date:   01/27/19


import sys
from socket import *

# Get the server hostname, and port and as command line arguments
argv = sys.argv
HOST = argv[1]
PORT = int(argv[2])

serverIP = HOST
serverPORT = PORT
dataLEN = 1000000

# Create a UDP socket.
# Notice the use of SOCK_DGRAM for UDP packets
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Assign IP address and port number to socket
serverSocket.bind((serverIP, serverPORT))

print('The server is ready to receive on port: {}'.format(serverPORT))

# loop forever listening for incoming datagram messages
while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(dataLEN)

    print("Receive data from client " + address[0] + ", " + str(address[1]) + ": " + data.decode())
    print("Sending data to client " + address[0] + ", " + str(address[1]) + ": " + data.decode())

    # Echo back to client
    serverSocket.sendto(data, address)
