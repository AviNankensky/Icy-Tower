import socket
import threading
import time
import json
import random

from main import updatePlayer2

client_socket = None

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
                x = message["x"]
                y = message["y"]
                updatePlayer2(x,y)
        except:
            print("An error occurred!")
            client_socket.close()
            break

def send_messages(client_socket, data):
    message = json.dumps(data)
    try:
        client_socket.send(message.encode('utf-8'))
    except:
            print("An error occurred!")
            client_socket.close()
            break

def updatePlayer2ToServer(x,y):
    send_messages(client_socket, {"x": x, "y": y})

def main():
    global client_socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.1.240', 9999))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    # send_thread = threading.Thread(target=send_messages, args=(client,))
    # send_thread.start()

if __name__ == "__main__":
    main()
