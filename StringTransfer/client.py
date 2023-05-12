import socket

SERVER = "127.0.0.1"
PORT = 8080

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER, PORT))
while True:
    inp = input("Enter the string : ")
    if inp == "Over":
        break
    client.send(inp.encode())

    answer = client.recv(1024)
    print("Answer is "+answer.decode())
    print("Type 'Over' to terminate")
client.close()
