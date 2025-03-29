from datetime import datetime
from socket import *
import time

def udp_ping_client(server_address, port, num_pings):

    client_socket = socket(AF_INET, SOCK_DGRAM)

    try:
        client_socket.settimeout(1.0)

        rtt_list = []
        packets_sent = 0
        packets_received = 0
        
        for i in range(num_pings):
            current_time = datetime.now().strftime('%a %b %d %H:%M:%S %Y')      #ping message sent here
            message = f"Kris {i+1}: {current_time}"                 
            start_time = time.time()#used for RTT calculation later 
            
            try:
                client_socket.sendto(message.encode(), (server_address, port)) #this sends our message from above to server
                packets_sent += 1
                response, server = client_socket.recvfrom(1024)                #message received
                end_time = time.time()
                
                rtt = (end_time - start_time) * 1000  #RTT Calculation (*1000 to convert to MS)
                rtt_list.append(rtt)
                packets_received += 1
                
                print(f"Received from server: {response.decode()}")            #server response message
                print(f"RTT: {rtt:.2f} ms")
            
            except timeout:
                print("Request timed out") 
        
        if rtt_list:                         #summary report here 
            min_rtt = min(rtt_list)
            max_rtt = max(rtt_list)
            avg_rtt = sum(rtt_list) / len(rtt_list)
            packet_loss_rate = ((packets_sent - packets_received) / packets_sent) * 100
        else:
            min_rtt = max_rtt = avg_rtt = 0 #this means RTT list is empty, we default to full packet failure 
            packet_loss_rate = 100
        
        print("\nKris' Summary Report:")
        print(f"Minimum RTT: {min_rtt:.2f} ms")
        print(f"Maximum RTT: {max_rtt:.2f} ms")
        print(f"Average RTT: {avg_rtt:.2f} ms")
        print(f"Packet Loss: {packet_loss_rate:.2f}%")
    
    finally:
        client_socket.close()

udp_ping_client('localhost', 12000, 10)