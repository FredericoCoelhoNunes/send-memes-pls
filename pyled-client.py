import socketio

# export HOST=https://send-art-pls.herokuapp.com/
# export PORT=443
HOST = os.environ.get('HOST', 'http://localhost')
PORT = os.environ.get('PORT', 5000)


sio = socketio.Client()
sio.connect(f'{HOST}:{PORT}')
sio.on('new_image', set_image)

def set_image(image_bytes):
    # DO SOMETHING WITH IMAGE BYTES
    return