import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Socket successfully created')
except socket.error as err:
    print("Socket creation failed with error %s" %(err))

#defaul port for socket
port = 80

try:
    host_ip = socket.gethostbyname(str('www.google.com'))
except socket.gaierror:
    #this means could not resolve the host
    print("there was an error resolving the host")
    sys.exit()

#connecting to the server
s.connect((host_ip, port))

print("the socket has successfully connected to google")
print(host_ip)