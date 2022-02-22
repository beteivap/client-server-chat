from socket import *


# Create server TCP listening socket on localhost port 8001
server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(('127.0.0.1', 8001))
server_socket.listen(1)
print('Server listening on: localhost on port: 8001')

# Create connection socket for requests on listening socket
connection_socket, addr = server_socket.accept()
print(f'Connected by {addr}')
print('Waiting for message...')

# Receive messages and send replies on connection
# socket until either client or server inputs '/q'
# or if 0 bytes sent over TCP connection
msg = connection_socket.recv(2048).decode()
if msg and msg != '/q':
       print(msg)
       print('Type /q to quit')
       print('Enter message to send...')
       while True:
              reply = input('>')
              connection_socket.send(reply.encode())
              if not reply or reply == '/q':
                     break
              msg = connection_socket.recv(2048).decode()
              if not msg or msg == '/q':
                     break
              print(msg)

connection_socket.close()
server_socket.close()
