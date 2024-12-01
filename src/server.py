"""
server.py: A basic TCP server that listens for client connections and sends a welcome message.

Author: _ox.ar3c1B0
Date: 2024
"""

import socket

def start_server(host: str, port: int):
    """
    Starts a basic TCP server that accepts a single client connection.

    :param host: IP address the server will bind to.
    :param port: Port number the server will listen on.
    """
    try:
        # Create a TCP/IP socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(1)  # Listen for one connection
        print(f"Server is running on {host}:{port}")

        # Wait for a connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Send a welcome message to the client
        client_socket.sendall(b"Welcome to the TCP Server!")
        client_socket.close()

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Ensure the socket is closed
        server_socket.close()
        print("Server shut down.")

if __name__ == "__main__":
    HOST = "127.0.0.1"
    PORT = 12345
    start_server(HOST, PORT)
