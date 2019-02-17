import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QFileDialog, QTableView
from PyQt5.QtCore import pyqtSlot, QObjectCleanupHandler
from PyQt5.QtGui import QIcon, QPixmap
from homepage import Homepage
from upload import Uploadpage
from helperclass import PandasModel


class App(Homepage, Uploadpage):
    def __init__(self):
        super().__init__()
        self.title = 'Exam Seat Planner'
        self.left = 10
        self.top = 10
        self.width = 600
        self.height = 600
        self.homepage_ui()
    
    @pyqtSlot()
    def upload_clicked(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.ExistingFiles)
        #dlg.setFilter("Text files (*.txt)")
        if dlg.exec_():
            filenames = dlg.selectedFiles()
        QObjectCleanupHandler().add(self.layout)
        self.create_table(filenames)
        self.upload_gui()
    
    def create_table(self,filenames):
        self.tableWidget = list()
        for fname in filenames:
            tWidget = QTableView()
            df = pd.read_excel(fname)
            model = PandasModel(df)
            tWidget.setModel(model)
            self.tableWidget.append([fname.split('/')[-1],tWidget])

    
    @pyqtSlot()
    def back_clicked(self):
        QObjectCleanupHandler().add(self.layout)
        self.homepage_ui()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())