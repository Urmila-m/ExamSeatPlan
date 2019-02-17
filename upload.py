import sys
from config import *
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTableWidget,QTableWidgetItem, QTabWidget, \
                            QPushButton, QHBoxLayout

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
    
    def upload_gui(self):
        self.layout = QVBoxLayout()
        horizontal_layout1 = QHBoxLayout()

        #Create tab of files
        self.tab = QTabWidget()
        for fname, table_widget in self.tableWidget:
            self.tab.addTab(table_widget,fname)

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
        #button_OK.clicked.connect(self.ok_clicked)
    
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
 