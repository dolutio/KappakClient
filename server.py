import socket
import struct

HOST = socket.gethostbyname_ex(socket.gethostname())[-1][-1];print(HOST)
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen(1)


client, adress = server.accept()

while True:
    data = client.recv(1024).decode('utf-8')
    print(data)