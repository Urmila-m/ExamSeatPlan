import sys
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtWidgets import (QApplication, QHBoxLayout, QLabel, QPushButton,
                             QVBoxLayout, QWidget)

from config import *
Qt = QtCore.Qt


# Homepage design class
class Homepage(QWidget):
    def __init__(self):
        super().__init__()
        self.title = window_title
        self.left = window_left
        self.top = window_top
        self.width = window_width
        self.height = window_height
    
    def homepage_gui(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        vertical_layout = QVBoxLayout()
        vertical_layout1 = QVBoxLayout()
        vertical_layout2 = QVBoxLayout()
        vertical_layout3 = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        horizontal_layout1= QHBoxLayout()
        horizontal_layout2= QHBoxLayout()

        title = QLabel("Choose an action:")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Helvetica", 20, QFont.Bold))
        
        #show edit image
        edit_img = QPixmap('Res/edit.png').scaled(200, 200, transformMode=Qt.SmoothTransformation)
        label_edit = QLabel(self)
        label_edit.setPixmap(edit_img)
        self.button_edit = QPushButton('Edit Room Profile')
        #show upload image
        upload_img = QPixmap('Res/upload.png').scaled(200, 200, transformMode=Qt.SmoothTransformation)
        label_upload = QLabel(self)
        label_upload.setPixmap(upload_img)
        self.button_upload = QPushButton('Upload')
        #show search image
        search_img = QPixmap('Res/search.png').scaled(200, 200, transformMode=Qt.SmoothTransformation)
        label_search = QLabel(self)
        label_search.setPixmap(search_img)
        self.button_search = QPushButton('Search')

        vertical_layout1.addWidget(label_edit)
        vertical_layout1.addWidget(self.button_edit)
        vertical_layout2.addWidget(label_upload)
        vertical_layout2.addWidget(self.button_upload)
        vertical_layout3.addWidget(label_search)
        vertical_layout3.addWidget(self.button_search)

        horizontal_layout.addStretch(2)
        horizontal_layout.addLayout(vertical_layout1)
        horizontal_layout.addStretch(1)
        horizontal_layout.addLayout(vertical_layout2)
        horizontal_layout.addStretch(1)
        horizontal_layout.addLayout(vertical_layout3)
        horizontal_layout.addStretch(2)

        vertical_layout.addStretch(1)
        vertical_layout.addWidget(title)
        vertical_layout.addStretch(1)
        vertical_layout.addLayout(horizontal_layout)
        vertical_layout.addStretch(2)

        #set layout
        self.layout = vertical_layout
        self.setLayout(self.layout)
        
        self.button_upload.clicked.connect(self.upload_clicked)
        self.button_edit.clicked.connect(self.edit_clicked)
    
    @pyqtSlot()
    def upload_clicked(self):
        print('upload button pressed')
    
    @pyqtSlot()
    def edit_clicked(self):
        print('edit button pressed')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    homepage = Homepage()
    homepage.homepage_gui()
    homepage.show()
    sys.exit(app.exec_())
