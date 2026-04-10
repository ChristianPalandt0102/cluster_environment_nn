const term = new Terminal({
    cursorBlink: true,
    theme: {
        background: "#000000",
        foreground: "#00ffcc"
    }
});

term.open(document.getElementById("terminal"));

const socket = new WebSocket("ws://localhost:8765");

term.write("TSN Terminal Ready\r\n> ");

socket.onmessage = (event) => {
    term.write("\r\n" + event.data + "\r\n> ");
};

let command = "";

term.onData(data => {

    if (data === "\r") {
        socket.send(command);
        command = "";
    } else if (data === "\u007F") {
        command = command.slice(0, -1);
    } else {
        command += data;
        term.write(data);
    }
});