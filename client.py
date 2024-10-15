import socket


def send_message():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect(("192.168.1.67", 65432))

    # Send the message
    message = str(['hello' , 'world'])
    client_socket.sendall(message.encode())

    # Close the socket
    client_socket.close()


if __name__ == "__main__":
    send_message()