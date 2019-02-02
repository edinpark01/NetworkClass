#   Client/Server Socket Interaction in UDP
#
#   Author: Braulio Tonaco
#   UCID:   bt74
#   Date:   01/27/19
#   Class:  CS356 - Wednesday 6pm to 9pm
#
#   Using UDP sockets, you will write a client and server program that enables the client to send a string of some
#   specified length to the server over the network, and the server simply echoes back that string back to the client.
#
#   The client program should take the following command-line parameters:
#       •	IP address of server            127.0.0.1
#       •	UDP port of server              12000
#       •	Length of string to be sent     10
#
#   STEP 01: The client program will read in the above input parameters
#   STEP 02: Initialize a string of the specified length
#   STEP 03: Send the message using the UDP socket API to the server running at the specified IP address and port
#   STEP 04: If the client does not receive a message back from the server within a certain amount of time
#            (one second), the client should retry up to a maximum number of tries (3) before terminating
#   STEP 05: The program output should print out trace information when data is sent and received, and account for
#            error conditions
#   STEP 06: Client trace output must include:
#               •	A message when data is sent to the server indicating destination IP address and port and length
#                   plus content of the data sent
#               •	A message when data is received from the server indicating source IP address and port and
#                   contents of the data received
#               •	An error message when any error occurs such as when a time-out occurs because the server is
#                   not running

import sys, time

from socket import *

argv = sys.argv

HOST = argv[1]
PORT = int(argv[2])
DATA_LENGTH = int(argv[3])

DATA = "X" * DATA_LENGTH

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)

dataEcho = None
attempts = 0

while attempts < 3:
    print("Sending Data To\t\t{}, {}: {} ( {} character(s) )".format(HOST, PORT, DATA, DATA_LENGTH))
    clientSocket.sendto(DATA.encode(), (HOST, PORT))

    try:
        dataEcho, address = clientSocket.recvfrom(DATA_LENGTH)
    except OSError:
        attempts += 1
        print("Message Timed Out")
        continue

    print("Received Data From\t{}, {}: {}".format(HOST, PORT, dataEcho.decode()))
    break


clientSocket.close()
