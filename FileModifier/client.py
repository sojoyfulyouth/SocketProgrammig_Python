import socket
import os
import sys

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))
fullname = input(
    "Enter file's name (R+filename: read file, W+filename+\"content\": append \"content\" to file): ")
contentIdx = fullname.find('"')
rORw = fullname[0]
filename = fullname[1:contentIdx]


data = client.recv(1024)
data_transferred = 0

if not data:
    print(f"file '{filename}' does not existing")
    sys.exit()

nowdir = os.getcwd()
if rORw == "R":
    with open(filename, "r") as f:
        try:
            while data:
                data_transferred += len(data)
                print(data.decode())
                data = client.recv(1024)
                # f.write(data.decode())
        except Exception as ex:
            print(ex)
elif rORw == "W":
    with open(filename, "wb") as f:
        try:
            while data:
                f.write(data)
                data_transferred += len(data)
                print(data.decode())
                data = client.recv(1024)
        except Exception as ex:
            print(ex)

print(f"Receving Completed: {filename}\n Data capacity: {data_transferred}")

client.close()
