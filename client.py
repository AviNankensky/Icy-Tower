import socket
import threading
import time
import json
import random

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"Received: {message}")
        except:
            print("An error occurred!")
            client_socket.close()
            break

def send_messages(client_socket):
    while True:
        x = random.randint(0, 100)
        y = random.randint(0, 100)
        message = json.dumps({"x": x, "y": y})
        try:
            client_socket.send(message.encode('utf-8'))
        except:
             print("An error occurred!")
             client_socket.close()
             break
        time.sleep(5)

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('192.168.1.240', 9999))

    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client,))
    send_thread.start()

if __name__ == "__main__":
    main()
