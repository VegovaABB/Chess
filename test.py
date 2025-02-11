import socket
import threading
import time

def start_server(host='192.168.125.123', port=65432):
    """Starts a simple TCP server that listens on the given host and port."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Server listening on {host}:{port}")
        
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                conn.sendall(b"Message received")

def start_client(host='192.168.125.123', port=65432, message='Hello, Server!'):
    """Starts a simple TCP client that connects to the server and sends a message."""
    time.sleep(1)  # Ensure the server starts before the client connects
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        client_socket.sendall(message.encode())
        data = client_socket.recv(1024)
        print(f"Received from server: {data.decode()}")

def main():
    server_thread = threading.Thread(target=start_server, daemon=True)
    server_thread.start()
    
    start_client()

if __name__ == "__main__":
    main()