import sys
from socket import *

server_ip = "127.0.0.1" if len(sys.argv) == 1 else sys.argv[1]
server_port = 12000 if len(sys.argv) == 1 else int(sys.argv[2])
dataLen = 100000

# Create a TCP "welcoming" socket. Notice the use of SOCK_STREAM for TCP packets
serverSocket = socket(AF_INET, SOCK_STREAM)

# Assign IP address and port number to socket
serverSocket.bind((server_ip, server_port))

# Listen for incoming connection requests
serverSocket.listen(1)
print('The server is ready to receive on port: ' + str(server_port))

# loop forever listening for incoming connection requests on "welcoming" soecket
while True:
    # Accept incoming connection requests, and allocate a new socket for data communication
    connectionSocket, address = serverSocket.accept()
    print("Socket created for client " + address[0] + ", " + str(address[1]))

    # Receive and print the client data in bytes from "data" socket
    data = connectionSocket.recv(dataLen).decode()
    print("Data from client: " + data)

    # Echo back to client
    connectionSocket.send(data.encode())
    connectionSocket.close()
