import socket
import time

HOST = "192.168.125.123"
PORT = 65432


def send_coords(c_socket, coords:list):
    c_socket.sendall(coords[0].encode())
    time.sleep(0.1)
    c_socket.sendall(coords[1].encode())
    time.sleep(0.1)
    c_socket.sendall(coords[2].encode())
    time.sleep(0.1)

    c_socket.sendall(coords[3].encode())
    time.sleep(0.1)
    c_socket.sendall(coords[4].encode())
    time.sleep(0.1)
    c_socket.sendall(coords[5].encode())
    time.sleep(0.1)
    c_socket.sendall(coords[6].encode())
    time.sleep(0.1)


def start_server(host=HOST, port=PORT):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    
    server_socket.listen(5)
    print(f'Server listening on {host}:{port}')
    
    while True:
        client_socket, addr = server_socket.accept()
        #// print(f'Connection from {addr}')
        while True:
            try:
                # dobimo podatke od roke
                data = client_socket.recv(1024).decode('utf-8') # 1MB max
                if not data:
                    break

                if data == "move":
                    print(data)
                    time.sleep(0.3)
                    send_coords(client_socket, ["234", "78", "160", "0", "650", "0"])
                    

            except Exception as e:
                print(f"Error: {e}")


if __name__ == "__main__":
    start_server()