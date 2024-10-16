import socket
import json as j

def send_message(data):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("192.168.1.67", 65432))
    message = j.dumps(data)
    client_socket.sendall(message.encode())
    client_socket.close()


if __name__ == "__main__":
    while True:
        t = input('>>')
        send_message(t)