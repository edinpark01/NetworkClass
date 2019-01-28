#   Client/Server Socket Interaction in UDP
#   Author: Braulio Tonaco
#   Date:   01/27/19
#
# STEP 1 - Create a Socket
#   s = socket(AF_INET, SOCK_DGRAM)
#
# STEP 2 - Bind a socket
#   s.bind((addressIP, addressPort))
#
# STEP 3 - Exchange Data
#   s.sendto(message.encode(), address)
#   receivedMessage, address = s.recvfrom(2048)
#
# STEP 4 - Close socket
#   close(s)

import sys, time

# Include Python's socket library
from socket import *

# Get the server hostname, port and data length as command line arguments
argv = sys.argv

print("[ INFO ]\t\targv -> ", argv)

# Command line argument is a string, change the port and count into integers
HOST = argv[1]
PORT = int(argv[2])
DATA_LENGTH = int(argv[3])

# Initialize data to be sent
DATA = "X" * DATA_LENGTH

# Create UDP client socket for SERVER, note the use of SOCK_DGRAM
# Family:
#   *   AF_INET     -
#   *   AF_INET6    -
# Transmission Protocol Type:
#   *   SOCK_DGRAM  -   UDP
#   *   SOCK_STREAM -   TCP
#   *   SOCK_RAW    -   IP
clientsocket = socket(AF_INET, SOCK_DGRAM)

# Attach SERVER IP and PORT to message
# Send into socket, sending data to server
clientsocket.sendto(DATA.encode(), (HOST, PORT))

print("[ INFO ]\t\tSending Data... HOST: {}\tPORT: {}\tDATA: ".format(HOST, PORT, DATA))

# Read reply characters from socket into string
# Receive the server response
dataEcho, address = clientsocket.recvfrom(DATA_LENGTH)

# Print out received string
print("[ INFO ]\t\tReceived data from "
      "Address 01: {}\t"
      "Address 02: {}\t"
      "Server Response: {}"
      "".format(address[0], address[1], dataEcho.decode()))

# Close the client socket
clientsocket.close()
