import socket
import threading

clients = []
lock = threading.Lock()

def handle_client(client_socket):
    global clients
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            print(f"Received: {message.decode('utf-8')}")
            with lock:
                for c in clients:
                    if c != client_socket:
                        try:
                            c.send(message)
                        except:
                            clients.remove(c)
        except:
            break

    with lock:
        clients.remove(client_socket)
    client_socket.close()

def main():
    global clients
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    print("Server listening on port 9999")

    while True:
        client_sock, addr = server.accept()
        print(f"Accepted connection from {addr}")
        with lock:
            clients.append(client_sock)
        client_handler = threading.Thread(target=handle_client, args=(client_sock,))
        client_handler.start()

if __name__ == "__main__":
    main()
