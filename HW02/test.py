#   Programming Assignment 2: UDP Ping Client and Server
#
#   Author: Braulio Tonaco
#
#       Using UDP sockets, you will write a client and server program that enables the client to determine the
#   round-trip time (RTT) to the server.
#       To determine the RTT delay, the client records the time on sending a ping request to the server, and then
#   records the time on receiving a ping response from the server.  The difference in the two times is the RTT.
#
#   The ping message contains 2 4-byte integers and must be encoded in network-byte order as follows :
#       •	4-byte message type with an integer value of 1 or 2
#               o	Message type = 1 for a ping request (message from client to server)
#               o	Message type = 2 for a ping response (message from server to client)
#
#       •	4-byte sequence number with a unique integer value starting from 1 .
#           In the ping response, the server should echo back the client’s sequence number.
#
#   Both the client and server program should take the following input parameters:
#       •	IP address of server
#       •	IP port of server
#
#
#       1.  The client program will read in the above input parameters,
#       2.  Send 10 ping requests consecutively to the server running at the specified IP address and port,
#       3.  Wait for a response each time.
#       4.  After each response is received,
#               a.  The client calculates and prints the RTT for the message.
#       5.  If no response is received within a certain amount of time (one second)
#               b.  The client notes that the request timed out and then sends the next request up to the maximum.
#
#       The program output should print out trace information when data is sent and received, and account for error
#   conditions. Trace output must include:
#       •	At start of output, print a message indicating the IP address and port of the server being pinged
#       •	For each ping response received, print RTT along with sequence number of ping message
#       •	For no ping response, print “Message timed out” along with sequence number of the ping message
#       •	After completion, print the following statistics (similar to output of UNIX ping utility);
#               o	Number of packets sent, received, lost (% loss rate)
#               o	Min, Max, Average RTT for all acknowledged ping packets

import struct

format_string = "!i"

for num in range(0, 25):
    packed = struct.pack(format_string, num)
    print("Value {}\t\tPacket: {}".format(num, packed))

    unpacked = struct.unpack(format_string, packed)
    print("Value {}\t\tPacket: {}".format(num, unpacked[0]))
    print("\n")

