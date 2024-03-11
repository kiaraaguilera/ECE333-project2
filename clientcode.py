# UDPPingerClient.py
import socket
import time

# Server address and port (change 'localhost' to '127.0.0.1' if needed)
server_address = ('127.0.0.1', 12000)

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Set timeout value for the socket (1 second in this case)
client_socket.settimeout(1.0)

# Number of pings to send
num_pings = 10

# Iterate over the number of pings
for sequence_number in range(1, num_pings + 1):
    # Generate the ping message
    message = f'Ping {sequence_number} {time.time()}'

    try:
        # Send the message to the server
        client_socket.sendto(message.encode(), server_address)

        # Record the time before waiting for a response
        start_time = time.time()

        # Receive the response from the server
        response, server_address = client_socket.recvfrom(1024)

        # Calculate and print the round trip time (RTT)
        rtt = time.time() - start_time
        print(f'Response from {server_address}: {response.decode()} - RTT: {rtt:.6f} seconds')

    except socket.timeout:
        # Print "Request timed out" if no response is received within the timeout period
        print(f'Request timed out for sequence number {sequence_number}')

# Close the socket
client_socket.close()

