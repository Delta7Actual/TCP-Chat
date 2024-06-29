import threading
import socket

host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def Broadcast(message):
    for client in clients:
        client.send(message)

def Handle(client):
    while True:
        try:
            message = client.recv(1024)
            Broadcast(message)
        except:
            clientIndex = clients.index(client)
            clients.remove(clientIndex)
            nickname = nicknames[clientIndex]
            Broadcast(f"{nickname} has blown the fuck up.".encode('utf-8'))
            nicknames.remove(nickname)

            break

def Receive():
    while True:
        client, address = server.accept()
        print(f"{str(address)} has connected")

        client.send("NICK".encode('utf-8'))
        nickname = client.recv(1024).decode("utf-8")

        nicknames.append(nickname)
        clients.append(client)

        print(f"Client nickname is {nickname}")
        Broadcast(f"{nickname} has joined the chat!".encode('utf-8'))
        client.send("You are connected!".encode('utf-8'))

        thread = threading.Thread(target=Handle, args=(client,))
        thread.start()

print("Server is up!")
Receive()