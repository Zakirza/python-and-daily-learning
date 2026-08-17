/**
 * UDP Server (Node.js) - basics
 *
 * Node's `dgram` module. There's no "connection" - just a socket that
 * receives 'message' events, each carrying the data AND the sender's
 * address/port (rinfo), since one socket serves many senders.
 */

const dgram = require("dgram");

const HOST = "127.0.0.1";
const PORT = 5001;

const server = dgram.createSocket("udp4");

server.on("message", (msg, rinfo) => {
  console.log(`[UDP] Received from ${rinfo.address}:${rinfo.port}: ${msg.toString()}`);
  server.send("ACK: " + msg, rinfo.port, rinfo.address);
});

server.on("error", (err) => {
  console.error("[UDP] Server error:", err.message);
});

server.bind(PORT, HOST, () => {
  console.log(`[UDP] Listening on ${HOST}:${PORT}`);
});
