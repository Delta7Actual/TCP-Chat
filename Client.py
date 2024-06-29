import threading
import socket

nickname = input("Enter nickname: ").strip()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))

def Receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')

            if message == "NICK":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("Failed to connect")
            client.close()
            break

def Send():
    while True:
        message = f'{nickname}: {input()}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=Receive)
receive_thread.start()

send_thread = threading.Thread(target=Send)
send_thread.start()
