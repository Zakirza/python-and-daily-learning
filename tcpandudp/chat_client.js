const net = require("net");
const readline = require("readline");

const HOST = "127.0.0.1";
const PORT = 6000;

const rl = readline.createInterface({ input: process.stdin, output: process.stdout });
const socket = net.createConnection({ host: HOST, port: PORT });

let askedUsername = false;

socket.on("data", (data) => {
  const text = data.toString();

  if (!askedUsername) {
    askedUsername = true;
    rl.question(text, (username) => {
      socket.write(username);
      console.log("Connected. Type messages below ('quit' to exit).");
      promptUser();
    });
    return;
  }

  // Clear the current prompt line, print the message, redraw the prompt
  console.log(`\n${text.trim()}`);
});

function promptUser() {
  rl.question("> ", (msg) => {
    if (msg.toLowerCase() === "quit") {
      socket.end();
      rl.close();
      return;
    }
    socket.write(msg);
    promptUser();
  });
}

socket.on("end", () => {
  console.log("[CHAT] Disconnected from server");
  process.exit(0);
});
