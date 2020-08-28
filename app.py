import sys
import os

from flask import (
    Flask,
    flash,
    request,
    render_template,
    redirect
)
import io
from flask_socketio import SocketIO, emit

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/upload', methods=['POST'])
def upload_image():
    data = request.files['image']

    socketio.emit('new_image', data.read())

    return redirect('/')

@app.route('/link', methods=['GET'])
def image_from_link():
    try:
        response = requests.get(request.args['url'])
        socketio.emit('new_image', response.content)
    except:
        flash("Couldn't get the meme from that URL :(")

    return redirect('/')

def run_server():
    socketio.run(app, port=5000)  


if __name__ == '__main__':
    run_server()