/**
 * TCP Server (Node.js) - basics
 *
 * Node's `net` module gives you an event-driven TCP server.
 * Each connected client gets its own `socket` object with events:
 * 'data', 'end', 'error', etc.
 */

const net = require("net");

const HOST = "127.0.0.1";
const PORT = 5000;

const server = net.createServer((socket) => {
  console.log(`[TCP] Connected: ${socket.remoteAddress}:${socket.remotePort}`);

  socket.on("data", (data) => {
    console.log(`[TCP] Received: ${data.toString()}`);
    socket.write("ACK: " + data);
  });

  socket.on("end", () => {
    console.log("[TCP] Client disconnected");
  });

  socket.on("error", (err) => {
    console.error("[TCP] Socket error:", err.message);
  });
});

server.listen(PORT, HOST, () => {
  console.log(`[TCP] Listening on ${HOST}:${PORT}`);
});
