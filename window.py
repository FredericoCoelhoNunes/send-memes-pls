import sys
import os
from PySide2 import QtCore, QtWidgets, QtGui
import socketio

HOST = os.environ.get('HOST', 'http://localhost')
PORT = os.environ.get('PORT', 5000)


class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.sio = socketio.Client()
        self.sio.connect(f'{HOST}:{PORT}')
        self.sio.on('new_image', self.set_image)


        self.layout = QtWidgets.QVBoxLayout()

        self.image = QtWidgets.QLabel()
        self.image.setFixedSize(750, 750)
        self.image.setScaledContents(True)

        self.image.setText('No image yet...')
        self.font = QtGui.QFont()
        self.font.setBold(True)
        self.font.setPointSize(60)
        self.image.setFont(self.font)
        self.image.setAlignment(QtCore.Qt.AlignCenter)

        self.layout.addWidget(self.image)    
        self.setLayout(self.layout)


    def set_image(self, image_bytes):
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image_bytes)

        self.image.setPixmap(pixmap)    


if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
    window.sio.disconnect()
