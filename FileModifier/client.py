import socket
import os
import sys

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))
filename=input("Enter file's name: ")
client.send(filename.encode())

data = client.recv(1024)
data_transferred = 0
if not data:
    print(f"file '{filename}' does not existing")
    sys.exit()

nowdir=os.getcwd()
with open(nowdir+"\\"+filename, "wb") as f:
    try:
        while data:
            f.write(data)
            data_transferred+=len(data)
            data = client.recv(1024)
    except Exception as ex:
        print(ex)
print(f"Receving Completed: {filename}\n Data capacity: {data_transferred}")

client.close()
