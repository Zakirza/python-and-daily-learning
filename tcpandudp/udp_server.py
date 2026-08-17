"""
UDP Server (Python) - basics

UDP is connectionless: there's no handshake, no persistent connection object.
Each recvfrom() call gives you a datagram AND the address it came from,
since a single UDP socket can receive from many different senders.
No delivery/order guarantees - packets can be lost, duplicated, or reordered.
"""

import socket

HOST = "127.0.0.1"
PORT = 5001


def main():
    # SOCK_DGRAM = UDP
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.bind((HOST, PORT))
        print(f"[UDP] Listening on {HOST}:{PORT}")

        while True:
            data, addr = sock.recvfrom(1024)  # blocks until a datagram arrives
            print(f"[UDP] Received from {addr}: {data.decode()}")
            sock.sendto(b"ACK: " + data, addr)  # must send back to a specific address


if __name__ == "__main__":
    main()
