import websockets
import asyncio
import os
print()

async def main():
    uri = f"ws://127.0.0.1:8080/v1/receive/{os.environ['PHONE_NUMBER']}"
    print(uri)
    # same happens when I use the default value for ping_interval
    async with websockets.connect(uri, ping_interval=None) as websocket:
        async for raw_message in websocket:
            print(raw_message)

asyncio.run(main())
