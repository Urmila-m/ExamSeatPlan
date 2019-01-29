from PyQt5 import QtCore, QtGui, QtWidgets
from profile import Ui_profile
import globals
from globals import Dialog

name = ""
password = ""

class Ui_Dialog(object):

    def gotoProfile(self):
        name = str(self.loginEditName.text())
        password = str(self.loginEditPass.text())
        if (name == "Me" and password == "123"):
            self.profile = globals.MainWindow
            self.ui = Ui_profile()
            self.ui.setupUi(self.profile)
            self.profile.show()
            Dialog.close()
        else:
            _translate = QtCore.QCoreApplication.translate
            self.loginCheck.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Name/Password incorrect</span></p></body></html>"))


    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(469, 301)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.loginButton = QtWidgets.QDialogButtonBox(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(80, 210, 341, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loginButton.sizePolicy().hasHeightForWidth())
        self.loginButton.setSizePolicy(sizePolicy)
        self.loginButton.setOrientation(QtCore.Qt.Horizontal)
        self.loginButton.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Ok)
        self.loginButton.setObjectName("loginButton")
        self.login = QtWidgets.QLabel(Dialog)
        self.login.setGeometry(QtCore.QRect(110, 20, 261, 61))
        self.login.setAlignment(QtCore.Qt.AlignCenter)
        self.login.setObjectName("login")
        self.loginName = QtWidgets.QLabel(Dialog)
        self.loginName.setGeometry(QtCore.QRect(140, 100, 81, 31))
        self.loginName.setObjectName("loginName")
        self.loginPass = QtWidgets.QLabel(Dialog)
        self.loginPass.setGeometry(QtCore.QRect(140, 140, 81, 31))
        self.loginPass.setObjectName("loginPass")
        self.loginCheck = QtWidgets.QLabel(Dialog)
        self.loginCheck.setGeometry(QtCore.QRect(140, 175, 300, 31))
        self.loginCheck.setObjectName("loginCheck")
        self.loginEditName = QtWidgets.QLineEdit(Dialog)
        self.loginEditName.setGeometry(QtCore.QRect(230, 100, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loginEditName.setFont(font)
        self.loginEditName.setMaxLength(50)
        self.loginEditName.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.loginEditName.setObjectName("loginEditName")
        self.loginEditPass = QtWidgets.QLineEdit(Dialog)
        self.loginEditPass.setGeometry(QtCore.QRect(230, 140, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.loginEditPass.setFont(font)
        self.loginEditPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.loginEditPass.setObjectName("loginEditPass")
        self.loginImg = QtWidgets.QLabel(Dialog)
        self.loginImg.setGeometry(QtCore.QRect(30, 80, 101, 101))
        self.loginImg.setText("")
        self.loginImg.setPixmap(QtGui.QPixmap(":/login.png"))
        self.loginImg.setScaledContents(True)
        self.loginImg.setObjectName("loginImg")
        self.loginName.setBuddy(self.loginEditName)
        self.loginPass.setBuddy(self.loginEditPass)

        self.retranslateUi(Dialog)
        self.loginButton.clicked['QAbstractButton*'].connect(self.gotoProfile)
        self.loginButton.rejected.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Login Form"))
        self.login.setText(_translate("Dialog",
                                      "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Login Form</span></p></body></html>"))
        self.loginName.setText(_translate("Dialog",
                                          "<html><head/><body><p><span style=\" font-size:10pt;\">Name:</span></p></body></html>"))
        self.loginPass.setText(_translate("Dialog",
                                          "<html><head/><body><p><span style=\" font-size:10pt;\">Password:</span></p></body></html>"))

import images.resources

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
