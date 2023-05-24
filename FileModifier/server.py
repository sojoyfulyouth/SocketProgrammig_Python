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

fullname = clientConnection.recv(1024)
fullname = fullname.decode()
rORw = fullname[0]
filename = fullname[1:]
print(f"filename: {filename}; Equation is received")
data_transferred = 0

if not exists(filename):
    print("no file")
    sys.exit()

print(f"sending file content: {filename}")
if rORw == "R":
    with open(filename, 'rb') as f:
        try:
            data = f.read(1024)
            while data:
                data_transferred += clientConnection.send(str(data).encode())
                data = f.read(1024)
        except Exception as ex:
            print(ex)
elif rORw == "W":
    with open(filename, 'a') as f:
        try:
            data = f.read(1024)
            while data:
                data_transferred += clientConnection.send(str(data).encode())
                data = f.read(1024)
        except Exception as ex:
            print(ex)
print(f"Sending Completed: {filename}\n Data capacity: {data_transferred}")


clientConnection.close()
