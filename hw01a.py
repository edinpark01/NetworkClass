#   Client/Server Socket Interaction in UDP
#   Author: Braulio Tonaco
#   Date:   01/27/19

# STEP 1 - Create a Socket
s = socket(AF_INET, SOCK_DGRAM)

# STEP 2 - Bind a socket
s.bind((addressIP, addressPort))

# STEP 3 - Exchange Data
s.sendto(message.encode(), address)
receivedMessage, address = s.recvfrom(2048)

# STEP 4 - Close socket
close(s)