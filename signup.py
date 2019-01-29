
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setFixedSize(519, 323)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        Dialog.setWindowIcon(icon)
        self.btnSignUp = QtWidgets.QDialogButtonBox(Dialog)
        self.btnSignUp.setGeometry(QtCore.QRect(110, 240, 341, 32))
        self.btnSignUp.setOrientation(QtCore.Qt.Horizontal)
        self.btnSignUp.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnSignUp.setObjectName("btnSignUp")
        self.signUp = QtWidgets.QLabel(Dialog)
        self.signUp.setGeometry(QtCore.QRect(170, 20, 141, 41))
        self.signUp.setAlignment(QtCore.Qt.AlignCenter)
        self.signUp.setObjectName("signUp")
        self.signName = QtWidgets.QLabel(Dialog)
        self.signName.setGeometry(QtCore.QRect(160, 80, 47, 31))
        self.signName.setObjectName("signName")
        self.signEmail = QtWidgets.QLabel(Dialog)
        self.signEmail.setGeometry(QtCore.QRect(160, 120, 47, 31))
        self.signEmail.setObjectName("signEmail")
        self.signPass = QtWidgets.QLabel(Dialog)
        self.signPass.setGeometry(QtCore.QRect(160, 160, 71, 31))
        self.signPass.setObjectName("signPass")
        self.signNameEdit = QtWidgets.QLineEdit(Dialog)
        self.signNameEdit.setGeometry(QtCore.QRect(260, 80, 181, 20))
        self.signNameEdit.setObjectName("signNameEdit")
        self.signEmailEdit = QtWidgets.QLineEdit(Dialog)
        self.signEmailEdit.setGeometry(QtCore.QRect(260, 120, 181, 20))
        self.signEmailEdit.setObjectName("signEmailEdit")
        self.signEmailPass = QtWidgets.QLineEdit(Dialog)
        self.signEmailPass.setGeometry(QtCore.QRect(260, 160, 181, 20))
        self.signEmailPass.setObjectName("signEmailPass")
        self.signUpImg = QtWidgets.QLabel(Dialog)
        self.signUpImg.setGeometry(QtCore.QRect(30, 90, 111, 111))
        self.signUpImg.setText("")
        self.signUpImg.setPixmap(QtGui.QPixmap(":/signUp.png"))
        self.signUpImg.setScaledContents(True)
        self.signUpImg.setObjectName("signUpImg")
        self.signName.setBuddy(self.signNameEdit)
        self.signEmail.setBuddy(self.signEmailEdit)
        self.signPass.setBuddy(self.signEmailPass)

        self.retranslateUi(Dialog)
        self.btnSignUp.accepted.connect(Dialog.accept)
        self.btnSignUp.clicked['QAbstractButton*'].connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Sign Up Form"))
        self.signUp.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Sign Up Form</span></p></body></html>"))
        self.signName.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Name:</span></p></body></html>"))
        self.signEmail.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Email:</span></p></body></html>"))
        self.signPass.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:10pt;\">Password:</span></p></body></html>"))

import images.resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

