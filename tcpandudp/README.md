# TCP & UDP: Basics + Chat App (Python & Node.js)

## Structure

```
python/
  basics/       tcp_server.py, tcp_client.py, udp_server.py, udp_client.py
  chat_app/     chat_server.py, chat_client.py   (multi-client TCP chat)
node/
  basics/       tcp_server.js, tcp_client.js, udp_server.js, udp_client.js
  chat_app/     chat_server.js, chat_client.js   (multi-client TCP chat)
```

## Running the basics

Open two terminals per example (one for server, one for client).

**Python TCP:**
```bash
python3 python/basics/tcp_server.py
python3 python/basics/tcp_client.py
```

**Python UDP:**
```bash
python3 python/basics/udp_server.py
python3 python/basics/udp_client.py
```

**Node TCP:**
```bash
node node/basics/tcp_server.js
node node/basics/tcp_client.js
```

**Node UDP:**
```bash
node node/basics/udp_server.js
node node/basics/udp_client.js
```

## Running the chat app

Start one server, then open as many client terminals as you like.

**Python:**
```bash
python3 python/chat_app/chat_server.py
python3 python/chat_app/chat_client.py   # run this in 2+ terminals
```

**Node.js:**
```bash
node node/chat_app/chat_server.js
node node/chat_app/chat_client.js        # run this in 2+ terminals
```

Type a username, then messages. Everyone connected sees everyone else's
messages in real time.

## TCP vs UDP — what actually differs in this code

| | TCP | UDP |
|---|---|---|
| Connection | `connect()`/`accept()` — 3-way handshake first | None — `sendto()` just fires a packet |
| Reliability | Guaranteed delivery + order (OS retransmits) | Best-effort — can be lost, duplicated, reordered |
| API shape | `recv()`/`send()` on an established socket | `recvfrom()`/`sendto()`, address given every time |
| Overhead | Higher (handshake, ACKs, retransmission) | Lower — just packets |
| Good for | Chat, file transfer, HTTP — anything where losing/reordering data breaks correctness | Video/voice streaming, game state updates, DNS — where a late/lost packet is better dropped than retransmitted |

This is exactly why the chat app is built on TCP: if UDP dropped or
reordered a message, the conversation would visibly break. Try killing
the UDP server mid-conversation in the basics example — the client's
`sendto()` won't even error, it'll just time out waiting for a reply,
because UDP has no concept of "connection lost."

## Next steps worth trying
- Add a `/quit` broadcast so others see a clean leave message (already partially done).
- Try `nc -u 127.0.0.1 5001` (netcat) against the UDP server to see raw datagrams.
- Simulate packet loss: add `if random.random() < 0.3: return` before `sendto()` in the UDP server and watch the client's timeouts.
