
from PyQt5 import QtCore, QtGui, QtWidgets
import login
import signup
import sys
import globals
from globals import Dialog
# app = QtWidgets.QApplication(sys.argv)
# MainWindow = QtWidgets.QMainWindow()
class Ui_MainWindow(object):
    def on_pushButton_clicked(self):
        # self.loginDialog = QtWidgets.QDialog()
        self.ui = login.Ui_Dialog()
        self.ui.setupUi(Dialog)
        Dialog.setModal(True)
        Dialog.exec_()

    def on_signUp_clicked(self):
        self.signUpDialog=QtWidgets.QDialog()
        self.ui=signup.Ui_Dialog()
        self.ui.setupUi(self.signUpDialog)
        self.signUpDialog.setModal(True)
        self.signUpDialog.exec_()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 550)
        MainWindow.setStyleSheet("background-color:rgb(192, 192, 192);")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(200, 90, 421, 281))
        self.groupBox.setStyleSheet("QGroupBox{\n"
"background-color:rgba(143,188,143, 0.7);\n"
"}\n"
"\n"
"QPushButton{\n"
"color:#228B22;\n"
"background-color:rgba(192,192,192, 0.7);\n"
"font-family:\"Comic Sans MS\", cursive, sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"border:solid;\n"
"border-width:2px;\n"
"border-color:rgba(0, 0, 0, 0.7);\n"
"color:black;\n"
"}\n"
"")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.seatPlanner = QtWidgets.QLabel(self.groupBox)
        self.seatPlanner.setGeometry(QtCore.QRect(90, 10, 231, 71))
        self.seatPlanner.setStyleSheet("border: solid;\n"
"border-width:3px;\n"
"border-color:rgba(0, 0, 0, 0.7);\n"
"font-family:\"Comic Sans MS\", cursive, sans-serif;\n"
"background-color:rgba(192,192,192, 0.7);\n"
"")
        self.seatPlanner.setScaledContents(True)
        self.seatPlanner.setAlignment(QtCore.Qt.AlignCenter)
        self.seatPlanner.setObjectName("seatPlanner")
        self.mainImage = QtWidgets.QLabel(self.groupBox)
        self.mainImage.setGeometry(QtCore.QRect(20, 110, 231, 141))
        self.mainImage.setText("")
        self.mainImage.setPixmap(QtGui.QPixmap(":/main.jpg"))
        self.mainImage.setScaledContents(True)
        self.mainImage.setObjectName("mainImage")
        self.btnLogin = QtWidgets.QPushButton(self.groupBox)
        self.btnLogin.setGeometry(QtCore.QRect(274, 130, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS,cursive,sans-serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.btnLogin.setFont(font)
        self.btnLogin.setStyleSheet("")
        self.btnLogin.setObjectName("btnLogin")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(274, 190, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS,cursive,sans-serif")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        font.setKerning(False)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.btnLogin.clicked.connect(self.on_pushButton_clicked)
        self.pushButton_2.clicked.connect(self.on_signUp_clicked)


        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.seatPlanner.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt; color:#228B22;\">Exam Seat Planner</span></p></body></html>"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.pushButton_2.setText(_translate("MainWindow", "SignUp"))

import images.resources

if __name__ == "__main__":
    #import sys
    #app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(globals.MainWindow)
    globals.MainWindow.show()
    sys.exit(globals.app.exec_())


