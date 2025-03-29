# udppingserver_no_loss.py (MODIFIED FROM HANDOUT)
from socket import *
import random
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)            # Create a UDP socket
serverSocket.bind(('', 12000))                        # Assign IP address and port number to socket
while True:                                           # Receive the client packet along with the address it is coming from
    try:
        message, address = serverSocket.recvfrom(1024)    # The server responds
        time.sleep(random.uniform(0.010, 0.020)) #simulate a random delay from 0-20 ms
        serverSocket.sendto(message, address)   
    except:
        print(f"Server was closed by Client.") 