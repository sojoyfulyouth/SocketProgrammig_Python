import socket
import os
import sys

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))
fullname = input(
    "Enter file's name (R+filename: read file, W+filename+\"content\": append \"content\" to file): ")

client.send(fullname.encode())

rORw = fullname[0]
if rORw=="R":
    filename = fullname[1:]
elif rORw == "W":
    contentIdx1 = fullname.find('"')
    contentIdx2=fullname.find('"', contentIdx1+1)
    filename = fullname[1:contentIdx1]
    content=fullname[contentIdx1+1:contentIdx2]
else:
    errormsg="Write a character before the file's name"
    print(errormsg)
    sys.exit()


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
        except Exception as ex:
                print(ex)
elif rORw == "W":
    with open(filename, "r") as f:
        try:
            while data:
                data_transferred += len(data)
                print(data.decode())
                data = client.recv(1024)
        except Exception as ex:
            print(ex)

print(f"Receving Completed: {filename}\n Data capacity: {data_transferred}")

client.close()
