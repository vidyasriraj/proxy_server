import socket
host = 'localhost'
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
response = s.recv(1024)
while response:
    print("Received: " + response.decode())
    response = s.recv(1024)
s.close()