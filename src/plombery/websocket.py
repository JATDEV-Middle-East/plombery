import socketio


sio = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*")

@sio.event
async def connect(sid, environ):
    print(f"Client {sid} connected")

@sio.event
async def disconnect(sid):
    print(f"Client {sid} disconnected")

@sio.event
async def message(sid, data):
    print(f"Received message from {sid}: {data}")
    await sio.emit('response', {'data': data}, room=sid)

# The key fix: specify the socketio_path to match your mount point
asgi = socketio.ASGIApp(socketio_server=sio, socketio_path="/ws/socket.io")