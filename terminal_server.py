# terminal_server.py

import asyncio
import websockets
import subprocess


async def handle(ws):

    await ws.send("Connected to TSN backend")

    async for msg in ws:

        try:
            # ⚠️ SAFE MODE: restrict commands
            if msg.strip() == "status":
                response = "System running"

            elif msg.strip() == "cycle":
                response = "Cycle triggered"

            elif msg.startswith("exec "):
                cmd = msg.replace("exec ", "")

                # VERY IMPORTANT: limit execution
                if cmd in ["ls", "pwd"]:
                    result = subprocess.getoutput(cmd)
                    response = result
                else:
                    response = "Command blocked"

            else:
                response = f"Unknown command: {msg}"

        except Exception as e:
            response = str(e)

        await ws.send(response)


async def main():
    async with websockets.serve(handle, "0.0.0.0", 8765):
        print("Terminal server running on ws://localhost:8765")
        await asyncio.Future()

asyncio.run(main())