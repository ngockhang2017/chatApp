import socket

#creat a socket object
s = socket.socket()
print('socket successfully created')

#reserve a port on your computer in our
#case it is 12345 but it can be anything

port = 60000

#next bind to the port
#we have not typed any ip in the field
#instead we have inputted an empty string this makes the server listen to requests coming from other computers on the network

s.bind(('', port))
print("socket binded to %s" %(port))

#put the socket into listening mode
s.listen(5)
print("socket is listening")

# a forever connection until we interrupt it or an error occurs
while True:
    clientConnected, addr = s.accept()
    print('got connection from', addr)

    # #send a thank you message to the client. endcoding to send byte type.
    # clientConnected.send('Thank you for connecting'.encode())

    dataFromClient = clientConnected.recv(1024)
    print('receive from client: ', dataFromClient.decode())

    # Send some data back to the client
    sendback = "server receive: " + dataFromClient.decode()
    clientConnected.send(sendback.encode())

    if dataFromClient.decode() == 'exit':
        print('closed server!')
        #breaking once connection closed
        break
