const net = require("net");
const readline = require("readline");

const HOST = "127.0.0.1";
const PORT = 5000;

const socket = net.createConnection({ host: HOST, port: PORT }, () => {
  console.log(`[TCP] Connected to ${HOST}:${PORT}`);
  promptUser();
});

socket.on("data", (data) => {
  console.log(`[TCP] Server replied: ${data.toString()}`);
  promptUser();
});

socket.on("end", () => {
  console.log("[TCP] Connection closed by server");
  process.exit(0);
});

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

function promptUser() {
  rl.question("Type a message (or 'quit'): ", (msg) => {
    if (msg.toLowerCase() === "quit") {
      socket.end();
      rl.close();
      return;
    }
    socket.write(msg);
  });
}
