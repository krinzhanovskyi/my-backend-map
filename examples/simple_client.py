"""
simple_client.py: A basic TCP client that connects to a server and receives a message.

Author: _ox.ar3c1B0
Date: 2024
"""

import socket

def connect_to_server(host: str, port: int):
    """
    Connects to a TCP server and receives a message.

    :param host: IP address of the server.
    :param port: Port number of the server.
    """
    try:
        # Create a TCP/IP socket
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client_socket.connect((host, port))
        print(f"Connected to server at {host}:{port}")

        # Receive and print the server message
        message = client_socket.recv(1024)  # Buffer size is 1024 bytes
        print(f"Server says: {message.decode()}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the socket is closed
        client_socket.close()
        print("Connection closed.")

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 12345
    connect_to_server(HOST, PORT)
