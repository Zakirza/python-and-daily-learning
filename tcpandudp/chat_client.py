"""
TCP chat client (Python)

Uses two threads: one to listen for incoming messages, one for your
typing input - so you can receive messages while composing your own.
"""

import socket
import threading

HOST = "127.0.0.1"
PORT = 6000


def listen_for_messages(sock: socket.socket):
    while True:
        try:
            data = sock.recv(1024)
            if not data:
                print("\n[CHAT] Disconnected from server")
                break
            print(f"\n{data.decode().strip()}\n> ", end="")
        except OSError:
            break


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))

    prompt = sock.recv(1024).decode()
    username = input(prompt)
    sock.sendall(username.encode())

    threading.Thread(target=listen_for_messages, args=(sock,), daemon=True).start()

    print("Connected. Type messages below ('quit' to exit).")
    while True:
        msg = input("> ")
        if msg.lower() == "quit":
            break
        sock.sendall(msg.encode())

    sock.close()


if __name__ == "__main__":
    main()
