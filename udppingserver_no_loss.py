# udppingserver_no_loss.py (UNMODIFIED FROM HANDOUT)
from socket import *
serverSocket = socket(AF_INET, SOCK_DGRAM)            # Create a UDP socket
serverSocket.bind(('', 12000))                        # Assign IP address and port number to socket
while True:                                           # Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(1024)    # The server responds
    serverSocket.sendto(message, address)           