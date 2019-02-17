import sys
from config import *
from helperclass import PandasModel
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout, QHBoxLayout, QTableView, QPushButton, QHeaderView
from PyQt5.QtCore import pyqtSlot



class Editprofilepage(QWidget):
    def __init__(self):
        super().__init__()
        self.title = window_title
        self.left = window_left
        self.top = window_top
        self.width = window_width
        self.height = window_height
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
    
    def editprofilepage_gui(self):
        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        
        #Room profile table
        profile_table = QTableView()
        df = pd.read_excel('room_profile.xlsx')
        self.model = PandasModel(df)
        profile_table.setModel(self.model)

        #Buttons
        self.button_back = QPushButton('Back')
        self.button_save = QPushButton('Save')
        self.button_addroom = QPushButton('Add Room')
        self.button_removeroom = QPushButton('Remove Room')

        #Gui
        horizontal_layout.addWidget(self.button_back)
        horizontal_layout.addWidget(self.button_save)

        horizontal_layout2.addStretch(1)
        horizontal_layout2.addWidget(self.button_addroom)
        horizontal_layout2.addWidget(self.button_removeroom)

        profile_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        vertical_layout.addWidget(profile_table)
        vertical_layout.addLayout(horizontal_layout2)
        vertical_layout.addLayout(horizontal_layout)
        self.layout = vertical_layout
        self.setLayout(self.layout)

        #listner for buttons
        self.button_save.clicked.connect(self.save_roomprofile)
        self.button_back.clicked.connect(self.back_clicked)
        self.button_addroom.clicked.connect(self.add_row)
        self.button_removeroom.clicked.connect(self.remove_row)

    @pyqtSlot()
    def save_roomprofile(self):
        print('you pressed Saved')

    @pyqtSlot()
    def back_clicked(self):
        print('back button pressed')

    @pyqtSlot()
    def add_row(self):
        print('add room pressed')

    @pyqtSlot()
    def remove_row(self):
        print('remove room pressed')

    

# Standalone 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    App = Editprofilepage()
    App.editprofilepage_gui()
    App.show()
    sys.exit(app.exec_())

        
