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

    ascii_values = [ord(character) for character in msg]
    ascii_str = [str(n) for n in ascii_values]

    print("Send the result to client")
    for c in ascii_str:
        clientConnection.send(c.encode())

clientConnection.close()
