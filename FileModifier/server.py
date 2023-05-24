import socket
from os.path import exists
import sys

LOCALHOST = "127.0.0.1"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen()
print("Server started")
print("Waiting for client request..")

clientConnection, clientAddress = server.accept()
print("Connected client: ", clientAddress)
msg = ''

filename = clientConnection.recv(1024)
filename = filename.decode()
print("Equation is received")
data_transferred = 0

if not exists(filename):
    print("no file")
    sys.exit()

print(f"sending file: {filename}")
with open(filename, 'rb') as f:
    try:
        data = f.read(1024)
        while data:
            data_transferred += clientConnection.send(data.encode())
            data = f.read(1024)
    except Exception as ex:
        print(ex)
print(f"Sending Completed: {filename}\n Data capacity: {data_transferred}")


clientConnection.close()
