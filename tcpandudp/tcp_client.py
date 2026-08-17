"""TCP Client (Python) - basics"""

import socket

HOST = "127.0.0.1"
PORT = 5000


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((HOST, PORT))  # performs the TCP 3-way handshake
        print(f"[TCP] Connected to {HOST}:{PORT}")

        while True:
            msg = input("Type a message (or 'quit'): ")
            if msg.lower() == "quit":
                break
            sock.sendall(msg.encode())
            data = sock.recv(1024)
            print(f"[TCP] Server replied: {data.decode()}")


if __name__ == "__main__":
    main()
