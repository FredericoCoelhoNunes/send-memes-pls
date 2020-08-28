import sys
import threading
from PySide2 import QtCore, QtWidgets, QtGui
from flask import Flask, request, render_template, redirect, url_for
from PIL import Image
import io
from flask_socketio import SocketIO, emit

import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
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
    response = requests.get(request.args['url'])
    
    socketio.emit('new_image', response.content)

    return redirect('/')



if __name__ == '__main__':
    socketio.run(app, port=5000) 