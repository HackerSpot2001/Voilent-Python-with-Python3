import socket

clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# host = 
ip = socket.gethostbyname(socket.gethostname())
port = 3434
clientSocket.connect((str(ip),port))
msg = clientSocket.recv(1024)
clientSocket.close()
print(msg.decode('ascii'))