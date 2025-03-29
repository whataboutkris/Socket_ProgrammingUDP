from datetime import datetime
from socket import *
import time
import random

def udp_client_pinger(server_address, port, num_pings):

    clientSocket = socket(AF_INET, SOCK_DGRAM)

    try:
        clientSocket.settimeout(1.0) #1 second

        RTTList = []
        sentPackets = 0
        receivedPackets = 0                 

        
        for i in range(num_pings):
            timeCurr = datetime.now().strftime('%a %b %d %H:%M:%S %Y')      #ping message sent here
            message = f"Kris {i+1}: {timeCurr}"                 
            timeStart = time.time() #used for RTT calculation later 
            
            try:
                clientSocket.sendto(message.encode(), (server_address, port)) #this sends a message to server
                sentPackets += 1
                response, server = clientSocket.recvfrom(1024)                #message received
                timeEnd = time.time()
                
                rtt = (timeEnd - timeStart) * 1000  #RTT Calculation (*1000 to convert to MS)
                RTTList.append(rtt)
                receivedPackets += 1
                
                print(f"Kris {i+1}: server reply: {response.decode()}")            #server response message
                print(f"RTT: {rtt:.2f} ms")
            except timeout:
                print(f"Kris {i+1}: server request timed out, message was lost")
        
        if RTTList:                        #summary report here 
            min_rtt = min(RTTList)
            max_rtt = max(RTTList)
            avg_rtt = sum(RTTList) / len(RTTList) 
            packetLoss = ((sentPackets - receivedPackets) / sentPackets) * 100
        else:
            min_rtt = max_rtt = avg_rtt = 0
            packetLoss = 100
        
        print("\nKris' Summary Report:")
        print(f"Minimum RTT: {min_rtt:.2f} ms")
        print(f"Maximum RTT: {max_rtt:.2f} ms")
        print(f"Average RTT: {avg_rtt:.2f} ms")
        print(f"Packet Loss: {packetLoss:.2f}%")

    except:
        print("Something went wrong")

    finally:
        clientSocket.close()

udp_client_pinger('localhost', 12000, 10)