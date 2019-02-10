#   Client/Server Socket Interaction in UDP
#   Author: Braulio Tonaco
#   Date:   01/27/19
#
#   The server program should take the following command-line parameters:
#       •	IP address that server listens on (127.0.0.1 will be used to test the program)
#       •	UDP port that server listens on (e.g. 12000)
#   STEP 01: The server will listen on the loopback address and the given port number
#   STEP 02: The server should be prepared to receive data from the client up to a fixed maximum length (100 bytes).
#   STEP 03: The server will wait in an infinite loop to receive data from a client
#   STEP 04: The server will send the received data back to the client without modification.
#   STEP 05: Server trace output must include:
#               •	A message when data is received from the client indicating source IP address and port and
#                   contents of the data received
#               •	A message when data is sent back to the client indicating destination IP address and port

import sys
from socket import *

argv = sys.argv
HOST = argv[1]
PORT = int(argv[2])

serverIP = HOST
serverPORT = PORT
dataLEN = 1000000

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind((serverIP, serverPORT))

print('The server is ready to receive on port: {}'.format(serverPORT))

# loop forever listening for incoming datagram messages
while True:
    # Receive and print the client data from "data" socket
    data, address = serverSocket.recvfrom(dataLEN)

    print("Receive data from client\t" + address[0] + ", " + str(address[1]) + ": " + data.decode())
    print("Sending data to client\t\t" + address[0] + ", " + str(address[1]) + ": " + data.decode())

    # Echo back to client
    serverSocket.sendto(data, address)
