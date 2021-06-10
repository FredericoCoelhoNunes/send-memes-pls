import socketio
import os

from PIL import Image
from PIL import ImageDraw
import time
from rgbmatrix import RGBMatrix, RGBMatrixOptions

import io

# export HOST=https://send-art-pls.herokuapp.com/
# export PORT=443
HOST = os.environ.get('HOST', 'http://localhost')
PORT = os.environ.get('PORT', 5000)


# Configuration for the matrix
options = RGBMatrixOptions()
options.rows = 64
options.cols = 64
options.chain_length = 1
options.parallel = 1
options.hardware_mapping = 'adafruit-hat'
options.multiplexing = 0
options.gpio_slowdown = 5 #try higher values
options.show_refresh_rate = True
options.pixel_mapper_config = "Rotate:90"

matrix = RGBMatrix(options = options)


def set_image(image_bytes):
    try:
        i = io.BytesIO(image_bytes)
        image = Image.open(i)
        image = image.convert('RGB')
        image = image.resize((options.rows, options.cols))
        matrix.Clear()
        matrix.SetImage(image, 0, 0, unsafe=False)
        
        
    except Exception as e:
        print(e)
    


sio = socketio.Client()
sio.connect(f'{HOST}:{PORT}')
sio.on('new_image', set_image)

