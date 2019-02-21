import sys
from homepage import Homepage
from upload import Uploadpage
from editprofile import Editprofilepage
from examdetails import Examdetails
from resultpage import Resultpage
import pandas as pd
from helperclass import PandasModel
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QTableView, QFileDialog, QHeaderView
from PyQt5.QtCore import QObject, pyqtSlot
from helperfunction import equalise, arrange_seat, plan_examhall


class HomePage(Homepage):

    switch_upload = QtCore.pyqtSignal()
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
        self.filenames = list(filenames)[0]
        #print(filenames) #logging filenames
        self.switch_upload.emit()
    
    @pyqtSlot()
    def edit_clicked(self):
        self.switch_edit.emit()
        

class UploadPage(Uploadpage):

    switch_home = QtCore.pyqtSignal()
    switch_examdetail = QtCore.pyqtSignal()
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

    @pyqtSlot()
    def ok_clicked(self):
        self.keyeddataframes = self.generate_dataframe()
        self.switch_examdetail.emit()
    
    def generate_dataframe(self):
        keyed_dataframe = list()
        key = str()
        for dataframe, radio_buttons in zip(self.dataframes, self.radio_keys):
            for radio_button in radio_buttons:
                if radio_button.isChecked():
                    key = radio_button.text().replace('&','')
            
            keyed = pd.DataFrame(dataframe[key].values, columns = ['Key'])
            keyed_dataframe.append(keyed)
        return keyed_dataframe


class EditProfilePage(Editprofilepage):

    switch_home = QtCore.pyqtSignal()

    def __init__(self):
        Editprofilepage.__init__(self)
        self.editprofilepage_gui()

    
    @pyqtSlot()
    def save_roomprofile(self):
        df = self.model.get_roomprofile()
        df.to_excel('Res/room_profile.xlsx')

    @pyqtSlot()
    def back_clicked(self):
        self.switch_home.emit()

    @pyqtSlot()
    def add_row(self):
        self.model.add_row()

    @pyqtSlot()
    def remove_row(self):
        self.model.remove_row()

class ExamDetail(Examdetails):
    switch_upload = QtCore.pyqtSignal()
    switch_result = QtCore.pyqtSignal()

    def __init__(self, filenames):
        Examdetails.__init__(self, filenames)
        self.examdetails_gui()
    
    @pyqtSlot()
    def back_clicked(self):
        self.switch_upload.emit()

    @pyqtSlot()
    def generate_clicked(self):
        # print(self.dataframes)
        # print(self.num_seat)
        equalised = equalise(self.dataframes, self.num_seat)
        
        arranged = arrange_seat(equalised)
        self.planned = list()
        a = 0
        for hall in self.halls_info:
            b = a + hall[1] * hall[2]
            self.planned.append([hall[0],plan_examhall(arranged[a:b], hall[1], hall[2]).reset_index()])
            a = b

        #radio style
        if self.radio_linear.isChecked():
            self.style = self.radio_linear.text().replace('&','')
        else:
            self.style = self.radio_fill.text().replace('&','')
        print(self.style)

        #Emit switch
        self.switch_result.emit()
        
class ResultPage(Resultpage):

    switch_examdetail = QtCore.pyqtSignal()

    def __init__(self, df_result):
        Resultpage.__init__(self, df_result)
        self.resultpage_gui()

    @pyqtSlot()
    def back_clicked(self):
        self.switch_examdetail.emit()


class Controller:

    def __init__(self):
        self.homepage = HomePage()
        self.editprofilepage = EditProfilePage()
        pass

    def show_homepage(self):
        self.homepage.switch_upload.connect(self.show_uploadpage)
        self.homepage.switch_edit.connect(self.show_editprofilepage)
        self.close_uploadpage()
        self.close_editprofilepage()
        self.homepage.show()

    def show_uploadpage(self):
        self.filenames = self.homepage.filenames
        self.uploadpage = UploadPage(self.filenames)
        self.uploadpage.switch_home.connect(self.show_homepage)
        self.uploadpage.switch_examdetail.connect(self.show_examdetail)
        self.close_examdetail()
        self.close_homepage()
        self.uploadpage.show()

    def show_editprofilepage(self):
        self.editprofilepage.switch_home.connect(self.show_homepage)
        self.homepage.close()
        self.editprofilepage.show()

    def show_examdetail(self):
        self.close_resultpage()
        self.examdetail = ExamDetail(self.uploadpage.keyeddataframes)
        self.examdetail.switch_upload.connect(self.show_uploadpage)
        self.examdetail.switch_result.connect(self.show_resultpage)
        self.uploadpage.close()
        self.examdetail.show()

    def show_resultpage(self):
        self.resultpage = ResultPage(self.examdetail.planned)
        self.resultpage.switch_examdetail.connect(self.show_examdetail)
        self.examdetail.close()
        self.resultpage.show()

    def close_examdetail(self):
        try:
            self.examdetail.close()
        except:
            pass
    
    def close_resultpage(self):
        try:
            self.resultpage.close()
        except:
            pass
    
    def close_homepage(self):
        try:
            self.homepage.close()
        except:
            pass
    
    def close_uploadpage(self):
        try:
            self.uploadpage.close()
        except:
            pass
    
    def close_editprofilepage(self):
        try:
            self.editprofilepage.close()
        except:
            pass
    

    

        

def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_homepage()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
