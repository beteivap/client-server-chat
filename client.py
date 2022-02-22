from socket import *


# Create client TCP socket and connect to server
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(('127.0.0.1', 8001))
print('Connected to: localhost on port: 8001')
print('Type /q to quit')
print('Enter message to send...')

# Send messages and receive replies on connection
# socket until either client or server inputs '/q'
# or if 0 bytes sent over TCP connection
while True:
    msg = input('>')
    client_socket.send(msg.encode())
    if not msg or msg == '/q':
        break
    reply = client_socket.recv(2048).decode()
    if not reply or reply == '/q':
        break
    print(reply)

client_socket.close()
