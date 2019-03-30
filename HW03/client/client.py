import sys, time
from socket import *

# Get the server hostname, port and data length as command line arguments
host = sys.argv[1] if len(sys.argv) != 1 else "127.0.0.1"
port = int(sys.argv[2]) if len(sys.argv) != 1 else 12000
count = int(sys.argv[3]) if len(sys.argv) != 1 else 10

# Initialize and print data to be sent
data = 'X' * count

# Create TCP client socket. Note the use of SOCK_STREAM for TCP packet
clientSocket = socket(AF_INET, SOCK_STREAM)

# Create TCP connection to server
print("Connecting to " + host + ", " + str(port))
clientSocket.connect((host, port))

# Send data through TCP connection
print("Sending data to server: " + data)
clientSocket.send(data.encode())

# Receive the server response
dataEcho = clientSocket.recv(count)

# Display the server response as an output
print("Receive data from server: " + dataEcho.decode())

# Close the client socket
clientSocket.close()
