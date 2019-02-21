import sys
from config import *
import pandas as pd
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget,QTableWidgetItem, QTabWidget, \
                            QPushButton, QHBoxLayout, QRadioButton, QLabel

class Uploadpage(QWidget):
    def __init__(self):
        super().__init__()
        self.title = window_title
        self.left = window_left
        self.top = window_top
        self.width = window_width
        self.height = window_height
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.dataframes = [table.model()._data for _, table in self.tableWidget]
    
    def upload_gui(self):
        self.layout = QVBoxLayout()
        horizontal_layout1 = QHBoxLayout()

        self.radio_keys = list()
        #Create tab of files
        self.tab = QTabWidget()
        for fname, table_widget in self.tableWidget:
            headers = table_widget.model()._data.columns.values
            radio_buttons = list()
            for key in headers:
                radio_buttons.append(QRadioButton(key))
            self.radio_keys.append(radio_buttons)
            horizontal_layoutradio = QHBoxLayout()
            horizontal_layoutradio.addWidget(QLabel('Choose Key'))
            for radio_button in radio_buttons:
                horizontal_layoutradio.addWidget(radio_button)
            else:
                radio_button.setChecked(True)
            
            horizontal_layoutradio.addStretch(1)
            
            vertical_layout = QVBoxLayout()
            vertical_layout.addWidget(table_widget)
            vertical_layout.addLayout(horizontal_layoutradio)
            tab_wid = QWidget()
            tab_wid.setLayout(vertical_layout)
            self.tab.addTab(tab_wid,fname)

        #Create buttons'Back' and 'OK'
        self.button_OK = QPushButton('OK')
        self.button_back = QPushButton('Back')
        horizontal_layout1.addWidget(self.button_back)
        horizontal_layout1.addWidget(self.button_OK)

        #add to main layout
        self.layout.addWidget(self.tab)
        self.layout.addLayout(horizontal_layout1)
        self.setLayout(self.layout)

        #add lister to the buttons
        self.button_back.clicked.connect(self.back_clicked)
        self.button_OK.clicked.connect(self.ok_clicked)
    
    @pyqtSlot()
    def back_clicked(self):
        print('back button pressed')

        
    
    @pyqtSlot()
    def ok_clicked(self):
        print('ok button pressed')
        

    def create_table(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)
        self.tableWidget = [['test', self.tableWidget]]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    uploadpage = Uploadpage()
    uploadpage.create_table()
    uploadpage.upload_gui()
    uploadpage.show()
    sys.exit(app.exec_())
 