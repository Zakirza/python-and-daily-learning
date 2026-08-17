const dgram = require("dgram");
const readline = require("readline");

const HOST = "127.0.0.1";
const PORT = 5001;

const client = dgram.createSocket("udp4");
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

console.log(`[UDP] Sending datagrams to ${HOST}:${PORT} (no connection is made)`);

client.on("message", (msg) => {
  console.log(`[UDP] Server replied: ${msg.toString()}`);
  promptUser();
});

function promptUser() {
  rl.question("Type a message (or 'quit'): ", (msg) => {
    if (msg.toLowerCase() === "quit") {
      client.close();
      rl.close();
      return;
    }
    client.send(msg, PORT, HOST);
    // Simple timeout to show that UDP replies aren't guaranteed
    setTimeout(() => {}, 0);
  });
}

promptUser();
