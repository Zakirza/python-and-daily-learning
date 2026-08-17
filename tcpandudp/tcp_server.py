"""
TCP Server (Python) - basics

TCP is connection-oriented: the server listens, accepts a connection,
and then both sides can read/write over that connection until it's closed.
Delivery is reliable and ordered (the OS handles retransmission, ordering).
"""

import socket

HOST = "127.0.0.1"
PORT = 5000


def main():
    # AF_INET = IPv4, SOCK_STREAM = TCP
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_sock:
        # Lets you restart the server quickly without "Address already in use"
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((HOST, PORT))
        server_sock.listen(1)  # backlog of 1 pending connection
        print(f"[TCP] Listening on {HOST}:{PORT}")

        while True:
            conn, addr = server_sock.accept()  # blocks until a client connects
            with conn:
                print(f"[TCP] Connected by {addr}")
                while True:
                    data = conn.recv(1024)  # blocks until data arrives (or conn closes)
                    if not data:
                        # empty bytes means the client closed the connection
                        print(f"[TCP] {addr} disconnected")
                        break
                    print(f"[TCP] Received: {data.decode()}")
                    conn.sendall(b"ACK: " + data)  # echo back with an ack prefix


if __name__ == "__main__":
    main()
