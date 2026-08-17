"""UDP Client (Python) - basics"""

import socket

HOST = "127.0.0.1"
PORT = 5001


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.settimeout(3)  # UDP has no "disconnect" signal, so use a timeout
        print(f"[UDP] Sending datagrams to {HOST}:{PORT} (no connection is made)")

        while True:
            msg = input("Type a message (or 'quit'): ")
            if msg.lower() == "quit":
                break
            sock.sendto(msg.encode(), (HOST, PORT))
            try:
                data, _ = sock.recvfrom(1024)
                print(f"[UDP] Server replied: {data.decode()}")
            except socket.timeout:
                print("[UDP] No reply - packet may have been lost (this is normal for UDP)")


if __name__ == "__main__":
    main()
