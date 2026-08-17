/**
 * Multi-client TCP chat server (Node.js)
 *
 * Node's event loop makes this simpler than the threaded Python version -
 * no locks needed, since JS is single-threaded and callbacks run one
 * at a time. We just keep a Map of connected sockets -> usernames.
 */

const net = require("net");

const HOST = "127.0.0.1";
const PORT = 6000;

const clients = new Map(); // socket -> username

function broadcast(message, excludeSocket = null) {
  for (const [sock] of clients) {
    if (sock === excludeSocket) continue;
    sock.write(message);
  }
}

const server = net.createServer((socket) => {
  socket.write("Enter your username: ");

  let username = null;

  socket.on("data", (data) => {
    const text = data.toString().trim();
    if (!text) return;

    if (username === null) {
      username = text || `user_${socket.remotePort}`;
      clients.set(socket, username);
      console.log(`[CHAT] ${username} joined from ${socket.remoteAddress}:${socket.remotePort}`);
      broadcast(`* ${username} joined the chat *\n`, socket);
      return;
    }

    console.log(`[CHAT] ${username}: ${text}`);
    broadcast(`${username}: ${text}\n`, socket);
  });

  socket.on("end", () => {
    if (username) {
      clients.delete(socket);
      console.log(`[CHAT] ${username} left`);
      broadcast(`* ${username} left the chat *\n`);
    }
  });

  socket.on("error", (err) => {
    console.error("[CHAT] Socket error:", err.message);
  });
});

server.listen(PORT, HOST, () => {
  console.log(`[CHAT] Server listening on ${HOST}:${PORT}`);
});
