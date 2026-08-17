"""
Multi-client TCP chat server (Python)

Why TCP for chat? Messages must arrive in order and without loss -
you don't want "hello" and "how are you" to swap order, or vanish.
TCP handles that for us; UDP does not.

Design: one thread per connected client. A lock protects the shared
list of client sockets since multiple threads write to it.
"""

import socket
import threading

HOST = "127.0.0.1"
PORT = 6000

clients = {}  # socket -> username
clients_lock = threading.Lock()


def broadcast(message: str, exclude_sock=None):
    with clients_lock:
        for sock in list(clients):
            if sock is exclude_sock:
                continue
            try:
                sock.sendall(message.encode())
            except OSError:
                pass  # will be cleaned up by that client's handler thread


def handle_client(conn: socket.socket, addr):
    try:
        conn.sendall(b"Enter your username: ")
        username = conn.recv(1024).decode().strip()
        if not username:
            username = f"user_{addr[1]}"

        with clients_lock:
            clients[conn] = username
        print(f"[CHAT] {username} joined from {addr}")
        broadcast(f"* {username} joined the chat *\n", exclude_sock=conn)

        while True:
            data = conn.recv(1024)
            if not data:
                break  # client disconnected
            text = data.decode().strip()
            if not text:
                continue
            print(f"[CHAT] {username}: {text}")
            broadcast(f"{username}: {text}\n", exclude_sock=conn)

    except ConnectionResetError:
        pass
    finally:
        with clients_lock:
            username = clients.pop(conn, "unknown")
        conn.close()
        print(f"[CHAT] {username} left")
        broadcast(f"* {username} left the chat *\n")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((HOST, PORT))
        server_sock.listen()
        print(f"[CHAT] Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_sock.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()


if __name__ == "__main__":
    main()
