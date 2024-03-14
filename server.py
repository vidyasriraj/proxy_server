import socket
import threading

def handle_client(c, addr):
    print("Connection from: ", str(addr))
    c.send(b"Hello, how are you")
    msg = "bye!"
    c.send(msg.encode())
    c.close()

host = 'localhost'
port = 8000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)

while True:
    c, addr = s.accept()
    client_thread = threading.Thread(target=handle_client, args=(c, addr))
    client_thread.start()