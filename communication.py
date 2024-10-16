import socket
import json
def start_server():
    print("Server is listening for connections...")
    while True:
        print('>>',end='')
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind(("192.168.1.67", 8080))  # Bind to the same IP and port
        server_socket.listen()
        conn, addr = server_socket.accept()
        data = json.loads(conn.recv(1024).decode())
        print(data)
        conn.close()


if __name__ == "__main__":
    start_server()
