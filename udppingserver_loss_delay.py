# udppingserver_no_loss.py (MODIFIED FROM HANDOUT)
from socket import *
import random
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)            # Create a UDP socket
serverSocket.bind(('', 12000))                        # Assign IP address and port number to socket
try:
    while True:                                           # Receive the client packet along with the address it is coming from
        try:
            message, address = serverSocket.recvfrom(1024)    # The server responds

            time.sleep(random.uniform(0.010, 0.020)) #simulate a random delay from 0-20 ms
            loss_chance = random.randint(1, 100)   # simulate random packet loss (10% chance)

            if loss_chance <= 10:
                #time.sleep(3)  #will wait 3 seconds, which means a timeout will occur from the pinger, simulating loss 
                continue

            serverSocket.sendto(message, address)  
            
        except Exception as e:
            print(f"Something from the server side went wrong {e}")

except KeyboardInterrupt:   
    print("Manually killing the server") #manual kill switch for testing
finally:
    serverSocket.close()
    print(f"Server was successfully closed.")





from socket import *
import random
import time

serverSocket = socket(AF_INET, SOCK_DGRAM)  # Create a UDP socket
serverSocket.bind(('', 12000))              # Assign IP address and port number to socket

try:
    while True:  # Receive the client packet along with the address it is coming from
        try:
            message, address = serverSocket.recvfrom(1024)  # The server responds

            time.sleep(random.uniform(0.010, 0.020))  # Simulate a random delay from 0-20 ms
            loss_chance = random.randint(1, 100)  # Simulate random packet loss (10% chance)

            if loss_chance <= 10:
                print("Simulating packet loss.")
                continue  # Skip sending the response to simulate packet loss

            serverSocket.sendto(message, address)
        
        except ConnectionResetError as e:
            print(f"Connection reset error: {e}. Continuing to next message.")
        except Exception as e:
            print(f"An error occurred: {e}")

except KeyboardInterrupt:
    print("Server is shutting down.")

finally:
    serverSocket.close()
    print("Server was successfully closed.")