import sys
from homepage import Homepage
from upload import Uploadpage
from editprofile import Editprofilepage
import pandas as pd
from helperclass import PandasModel
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableView, QFileDialog, QHeaderView
from PyQt5.QtCore import QObject, pyqtSlot


class HomePage(Homepage):

    switch_upload = QtCore.pyqtSignal(list)
    switch_edit = QtCore.pyqtSignal()

    def __init__(self):
        Homepage.__init__(self)
        self.homepage_gui()
    
    @pyqtSlot()
    def upload_clicked(self):
        # File explorer dialog
        filenames = QFileDialog.getOpenFileNames(self,
                                     "Select all student records (excel file)",
                                     "./",
                                     "excel (*.xlsx *.xls)")
        filenames = list(filenames)[0]
        print(filenames) #logging filenames
        self.switch_upload.emit(filenames)
    
    @pyqtSlot()
    def edit_clicked(self):
        self.switch_edit.emit()
        

class UploadPage(Uploadpage):

    switch_home = QtCore.pyqtSignal()
    def __init__(self, filenames):
        self.create_table(filenames)
        Uploadpage.__init__(self)
        self.upload_gui()
        
    def create_table(self,filenames):
        self.tableWidget = list()
        for fname in filenames:
            tWidget = QTableView()
            df = pd.read_excel(fname)
            model = PandasModel(df)
            tWidget.setModel(model)
            tWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
            self.tableWidget.append([fname.split('/')[-1],tWidget])
    
    @pyqtSlot()
    def back_clicked(self):
        self.switch_home.emit()


class EditProfilePage(Editprofilepage):

    switch_home = QtCore.pyqtSignal()

    def __init__(self):
        Editprofilepage.__init__(self)
        self.editprofilepage_gui()

    def login(self):
        self.switch_window.emit()
    
    @pyqtSlot()
    def save_roomprofile(self):
        df = self.model.get_roomprofile()
        df.to_excel('room_profile.xlsx')

    @pyqtSlot()
    def back_clicked(self):
        self.switch_home.emit()

    @pyqtSlot()
    def add_row(self):
        self.model.add_row()

    @pyqtSlot()
    def remove_row(self):
        self.model.remove_row()


class Controller:

    def __init__(self):
        pass

    def show_homepage(self):
        self.homepage = HomePage()
        self.homepage.switch_upload.connect(self.show_uploadpage)
        self.homepage.switch_edit.connect(self.show_editprofilepage)
        try:
            self.uploadpage.close()
        except:
            pass
        
        try:
            self.editprofilepage.close()
        except:
            pass

        self.homepage.show()

    def show_uploadpage(self,filenames):
        self.uploadpage = UploadPage(filenames)
        self.uploadpage.switch_home.connect(self.show_homepage)
        self.homepage.close()
        self.uploadpage.show()

    def show_editprofilepage(self):
        self.editprofilepage = EditProfilePage()
        self.editprofilepage.switch_home.connect(self.show_homepage)
        self.homepage.close()
        self.editprofilepage.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_homepage()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
