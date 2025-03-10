import json
from socket import *

serverName = 'localhost'
serverPort = 2000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

def send_json_command(method, tal1=None, tal2=None):
    message = {"method": method}
    if tal1 is not None:
        message["Tal1"] = tal1
    if tal2 is not None:
        message["Tal2"] = tal2
    clientSocket.send((json.dumps(message) + "\n").encode())

def receive_json_response():
    response = clientSocket.recv(1024).decode().strip()
    return json.loads(response)

def print_response(response):
    if "Method" in response and response["Method"] == "close":
        print("Server requested to close connection.")
        return False
    print("From Server:", response)
    return True

# Send flere requests uden at lukke forbindelsen
commands = [("Random", 1, 100), ("Add", 7, 5), ("Subtract", 9, 5), ("Error", 3, 4)]

for cmd in commands:
    send_json_command(*cmd)
    response = receive_json_response()
    if not print_response(response):
        break  

# Send close-kommando
send_json_command("close")
receive_json_response() 

clientSocket.close()
