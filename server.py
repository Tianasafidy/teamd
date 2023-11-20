import asyncio
import websockets

connected = set()

async def server(websocket, path):
    # Register.
    connected.add(websocket)
    try:
        async for message in websocket:
            for conn in connected:
                await conn.send(f'Got a new MSG FOR YOU: {message}')
                print(message)                    
    except Exception as e:
        print(f"An execpiezjzked{type(e).__name__} occured: {e}")

    finally:
        # Unregister.
        connected.remove(websocket)
    

start_server = websockets.serve(server, "localhost", 80)


asyncio.get_event_loop().run_until_complete(start_server)
print("running")
asyncio.get_event_loop().run_forever()