
from PyQt5 import QtCore, QtGui, QtWidgets
import EditTable
import sys
import globals



class Ui_profile(object):
    def inputRoom(self):
        userInput=QtWidgets.QInputDialog()
        i, okPressed = userInput.getInt(userInput, "Input lab", "Enter number of rooms/labs", 0, 1, 100, 1)
        if okPressed:
            globals.room=i
            self.editProfile = QtWidgets.QDialog()
            self.ui = EditTable.Ui_editProfile()
            self.ui.setupUi(self.editProfile)
            self.editProfile.setModal(True)
            self.editProfile.exec_()

    def setupUi(self, profile):
        profile.setObjectName("profile")
        profile.resize(700, 450)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        profile.setWindowIcon(icon)
        profile.setStyleSheet("QLabel#room,#xlsx{\n"
"font-family:\"Comic Sans MS\",cursive,sans-serif;\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color:black;\n"
"}\n"
"QLabel#xlsx:hover, #room:hover{\n"
"background-color:grey;\n"
"}\n"
"\n"
"QPushButton{\n"
"font-family:\"Comic Sans MS\",cursive,sans-serif;\n"
"border:solid;\n"
"border-width:1px;\n"
"border-color:black;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:grey;\n"
"}\n"
"")
        self.centralwidget = QtWidgets.QWidget(profile)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 380, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS,cursive,sans-serif")
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.imgRoom = QtWidgets.QLabel(self.centralwidget)
        self.imgRoom.setGeometry(QtCore.QRect(160, 150, 91, 81))
        self.imgRoom.setToolTip("")
        self.imgRoom.setToolTipDuration(5)
        self.imgRoom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imgRoom.setText("")
        self.imgRoom.setPixmap(QtGui.QPixmap(":/edit.png"))
        self.imgRoom.setScaledContents(True)
        self.imgRoom.setObjectName("imgRoom")
        self.imgUpload = QtWidgets.QLabel(self.centralwidget)
        self.imgUpload.setGeometry(QtCore.QRect(330, 150, 101, 81))
        self.imgUpload.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.imgUpload.setText("")
        self.imgUpload.setPixmap(QtGui.QPixmap(":/upload.png"))
        self.imgUpload.setScaledContents(True)
        self.imgUpload.setObjectName("imgUpload")
        self.profileSeat = QtWidgets.QLabel(self.centralwidget)
        self.profileSeat.setGeometry(QtCore.QRect(260, 30, 211, 61))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.profileSeat.setFont(font)
        self.profileSeat.setAlignment(QtCore.Qt.AlignCenter)
        self.profileSeat.setObjectName("profileSeat")
        self.btnRoom = QtWidgets.QPushButton(self.centralwidget)
        self.btnRoom.setGeometry(QtCore.QRect(130, 250, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS,cursive,sans-serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnRoom.setFont(font)
        self.btnRoom.setObjectName("btnRoom")
        self.btnXLSX = QtWidgets.QPushButton(self.centralwidget)
        self.btnXLSX.setGeometry(QtCore.QRect(320, 250, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS,cursive,sans-serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btnXLSX.setFont(font)
        self.btnXLSX.setObjectName("btnXLSX")

        self.btn_search = QtWidgets.QPushButton(self.centralwidget)
        self.btn_search.setGeometry(QtCore.QRect(490, 250, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS,cursive,sans-serif")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_search.setFont(font)
        self.btn_search.setObjectName("btn_search")
        self.search_label = QtWidgets.QLabel(self.centralwidget)
        self.search_label.setGeometry(QtCore.QRect(500, 150, 101, 81))
        self.search_label.setFrameShape(QtWidgets.QFrame.Box)
        self.search_label.setText("")
        self.search_label.setPixmap(QtGui.QPixmap(":/search.png"))
        self.search_label.setScaledContents(True)
        self.search_label.setObjectName("search_label")

        profile.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(profile)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 734, 21))
        self.menubar.setObjectName("menubar")
        profile.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(profile)
        self.statusbar.setObjectName("statusbar")
        profile.setStatusBar(self.statusbar)

        self.btnRoom.clicked.connect(self.inputRoom)

        self.retranslateUi(profile)
        QtCore.QMetaObject.connectSlotsByName(profile)

    def retranslateUi(self, profile):
        _translate = QtCore.QCoreApplication.translate
        profile.setWindowTitle(_translate("profile", "Exam Seat Planner"))
        self.pushButton.setText(_translate("profile", "Past seat plans"))
        self.profileSeat.setText(_translate("profile", "Exam Seat Planner"))
        self.btnRoom.setText(_translate("profile", "Edit Room Profile"))
        self.btnXLSX.setText(_translate("profile", "Upload XLSX"))
        self.btn_search.setText(_translate("profile", "Search seat"))


import images.resources

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    profile = QtWidgets.QMainWindow()
    ui = Ui_profile()
    ui.setupUi(profile)
    profile.show()
    sys.exit(app.exec_())

