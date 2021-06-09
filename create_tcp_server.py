import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname() 
port = 444
ip = socket.gethostbyname(host)
serversocket.bind((str(ip),port))
serversocket.listen(3)

while True:
    clientsocket,address = serversocket.accept()
    print("received connection from %s "% str(address))
    massege = "Thanks for connecting" + "\r\n"
    clientsocket.send(massege.encode('ascii'))
    clientsocket.close()