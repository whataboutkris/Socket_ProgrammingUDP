# udppingserver with delay AND loss (MODIFIED FROM HANDOUT)
from socket import *
import random
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)            # Create a UDP socket
serverSocket.bind(('', 12000))                        # Assign IP address and port number to socket
while True:                                           # Receive the client packet along with the address it is coming from
    try:
        message, address = serverSocket.recvfrom(1024)    # The server responds

        time.sleep(random.uniform(0.010, 0.020)) #simulate a random delay from 10-20 ms
        loss_chance = random.randint(1, 100)   # simulate random packet loss (10% chance)

        if loss_chance <= 10:
            time.sleep(3)  #will wait 3 seconds, which means a timeout will occur from the pinger, simulating loss 

        serverSocket.sendto(message, address)  
        
    except Exception as e:
        print(f"Something from the server side went wrong {e}")