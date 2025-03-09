from socket import *

serverName = 'localhost'
serverPort = 51
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

command = "Random"
clientSocket.send((command + "\n").encode())

response = clientSocket.recv(1024).decode()
print('From Server: ' + response)

numbers = "1 100"  
clientSocket.send((numbers + "\n").encode())
response = clientSocket.recv(1024).decode()
print('From Server: ' + response)

command = "Add"
clientSocket.send((command + "\n").encode())

response = clientSocket.recv(1024).decode()
print('From Server: ' + response)

numbers = "7 5"  
clientSocket.send((numbers + "\n").encode())
response = clientSocket.recv(1024).decode()
print('From Server: ' + response)

command = "Subtract"
clientSocket.send((command + "\n").encode())    

response = clientSocket.recv(1024).decode()
print('From Server: ' + response)

numbers = "9 5" 
clientSocket.send((numbers + "\n").encode())
response = clientSocket.recv(1024).decode()
print('From Server: ' + response)

#clientSocket.close()