#   Programming Assignment 2: UDP Ping Client and Server
#
#   Author: Braulio Tonaco
#
#       Using UDP sockets, you will write a client and server program that enables the client to determine the
#   round-trip time (RTT) to the server.
#       To determine the RTT delay, the client records the time on sending a ping request to the server, and then
#   records the time on receiving a ping response from the server.  The difference in the two times is the RTT.
#
#   The ping message contains 2 4-byte integers and must be encoded in network-byte order as follows:
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

import sys, time, struct
from socket import *


def get_arguments():
    """ Retrieves command line arguments """

    arguments = {
        "HOST": sys.argv[1],
        "PORT": int(sys.argv[2]),
        "MSG_TYPE": 1
    }

    return arguments

# STEP 1: The client program will read in the above input parameters
args = get_arguments()

# STEP 2: Setup UDP protocol
client_socket = socket(AF_INET, SOCK_DGRAM)

# STEP 3: Sets timeout time (1 for one second)
client_socket.settimeout(1)

format_string = "!ii"

print("Pinging {}, {}".format(args['HOST'], args['PORT']))

# STEP 4: Send 10 ping requests consecutively to the server running at the specified IP address and port
for msg_num in range(1, 11):
    # STEP 4.0: Pack and Encode data
    PACKED = struct.pack(format_string, args['MSG_TYPE'], int(msg_num))
    DATA_LEN = sys.getsizeof(PACKED)

    # STEP 4.1: Start timer
    start = time.time()

    # STEP 4.1: Sends request to server
    client_socket.sendto(PACKED, (args['HOST'], args['PORT']))

    # STEP 4.2: Wait for a response each time.
    try:
        data_echoed, address = client_socket.recvfrom(DATA_LEN)
    except OSError:
        print("Ping message number {} timed out".format(msg_num))
        continue

    # STEP 4.4: Record End + calculate RTT
    end = time.time()
    RTT = end - start

    # STEP 4.5: Trace Output
    print("Ping message number {} RTT: {} secs".format(msg_num, RTT))

    # unpacked = struct.unpack(format_string, data_echoed)


