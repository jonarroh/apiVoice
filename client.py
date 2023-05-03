
import asyncio
import websockets


async def connect():
    uri = "ws://localhost:3001"  # URL del servidor websocket

    async with websockets.connect(uri) as websocket:
        # Enviar mensajes al servidor
        await websocket.send("5")

        # Esperar la respuesta del servidor
        response = await websocket.recv()
        print(f"Respuesta del servidor: {response}")


asyncio.run(connect())
