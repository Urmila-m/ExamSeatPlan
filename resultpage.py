import sys
from config import *
from helperclass import PandasModel
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget,QVBoxLayout, QHBoxLayout,\
                            QTableView, QPushButton, QHeaderView, QTabWidget
from PyQt5.QtCore import pyqtSlot



class Resultpage(QWidget):
    def __init__(self, df_result):
        super().__init__()
        self.title = window_title
        self.left = window_left
        self.top = window_top
        self.width = window_width
        self.height = window_height
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.result_df = df_result
    
    def resultpage_gui(self):
        vertical_layout = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        
        tab = QTabWidget()
        #result table
        for fname, planed_hall in self.result_df:
            result_table = QTableView()
            self.model = PandasModel(planed_hall)
            result_table.setModel(self.model)
            result_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            tab.addTab(result_table, fname)

        #Buttons
        self.button_back = QPushButton('Back')
        self.button_savelocal = QPushButton('Save Local')
        #self.button_savedb = QPushButton('Save Database')

        #Gui
        horizontal_layout.addWidget(self.button_back)
        horizontal_layout.addWidget(self.button_savelocal)
        #horizontal_layout.addWidget(self.button_savedb)

        vertical_layout.addWidget(tab)
        vertical_layout.addLayout(horizontal_layout)
        self.layout = vertical_layout
        self.setLayout(self.layout)

        #listner for buttons
        self.button_savelocal.clicked.connect(self.save_local)
        #self.button_savedb.clicked.connect(self.save_db)
        self.button_back.clicked.connect(self.back_clicked)

    @pyqtSlot()
    def save_local(self):
        print('you pressed Saved local')

    # @pyqtSlot()
    # def save_db(self):
    #     print('you pressed Saved database')

    @pyqtSlot()
    def back_clicked(self):
        print('back button pressed')

# Standalone 
if __name__ == '__main__':
    df = pd.read_excel('testdata.xlsx')
    app = QApplication(sys.argv)
    App = Resultpage(df)
    App.resultpage_gui()
    App.show()
    sys.exit(app.exec_())




        
