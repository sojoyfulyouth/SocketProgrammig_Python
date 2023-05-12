import socket

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

while True:
    data = clientConnection.recv(1024)
    msg = data.decode()
    if msg == 'Over':
        print("Connection is Over")
        break
    print("Equation is received")
    ascii_values = []
    for character in msg:
        ascii_values.append(ord(character))

    print("Send the result to client")
    output = ascii_values
    clientConnection.send(output.encode())
clientConnection.close()
