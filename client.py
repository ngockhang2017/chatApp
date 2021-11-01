import socket

while True:
    clientSocket = socket.socket()  # creat a socket object

    # define the port on which you want to connect
    port = 60000

    # connect to the server on local computer
    clientSocket.connect(('127.0.0.1', port))

    # Send data to server
    data = input('input data to send: ')

    clientSocket.send(data.encode())

    #receive data from the server and decode to get the string
    print(clientSocket.recv(1024).decode())
    if data == 'exit':
        break
    clientSocket.close() #close the connection