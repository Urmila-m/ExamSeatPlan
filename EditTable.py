
from PyQt5 import QtCore, QtGui, QtWidgets
import globals

class Ui_editProfile(object):
    def addRow(self):
        row=self.EditRoom.rowCount()
        self.EditRoom.insertRow(row)
        item = QtWidgets.QTableWidgetItem()
        self.EditRoom.setVerticalHeaderItem(row, item)
        item.setText(QtCore.QCoreApplication.translate("editProfile", str(row+1)+"."))
        item = QtWidgets.QTableWidgetItem()
        self.EditRoom.setItem(row, 0, item)
        item.setText(QtCore.QCoreApplication.translate("editProfile", "Lab" + str(row+ 1)))

    def removeRow(self):
         self.EditRoom.removeRow(self.EditRoom.rowCount()-1)

    def setupUi(self, editProfile):
        editProfile.setObjectName("editProfile")
        editProfile.resize(500, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        editProfile.setWindowIcon(icon)
        editProfile.setModal(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(editProfile)
        self.buttonBox.setGeometry(QtCore.QRect(140, 350, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")

        self.EditRoom = QtWidgets.QTableWidget(editProfile)
        self.EditRoom.setGeometry(QtCore.QRect(40, 80, 430, 261))
        self.EditRoom.setEditTriggers(QtWidgets.QAbstractItemView.DoubleClicked)
        self.EditRoom.setWordWrap(True)
        self.EditRoom.setCornerButtonEnabled(False)
        self.EditRoom.setObjectName("EditRoom")
        self.EditRoom.setColumnCount(4)
        self.EditRoom.setRowCount(globals.room)

        # print(self.EditRoom.rowCount())

        for i in range(self.EditRoom.rowCount()):
            item = QtWidgets.QTableWidgetItem()
            self.EditRoom.setVerticalHeaderItem(i, item)

        for i in range(self.EditRoom.columnCount()):
            item = QtWidgets.QTableWidgetItem()
            self.EditRoom.setHorizontalHeaderItem(i, item)

        for i in range(self.EditRoom.rowCount()):
            item = QtWidgets.QTableWidgetItem()
            self.EditRoom.setItem(i, 0, item)

        self.EditProfileLabel = QtWidgets.QLabel(editProfile)
        self.EditProfileLabel.setGeometry(QtCore.QRect(170, 40, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.EditProfileLabel.setFont(font)
        self.EditProfileLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.EditProfileLabel.setWordWrap(False)
        self.EditProfileLabel.setObjectName("EditProfileLabel")

        self.btn_remove = QtWidgets.QPushButton(editProfile)
        self.btn_remove.setGeometry(QtCore.QRect(380, 300, 75, 23))
        self.btn_remove.setObjectName("btn_remove")
        self.btn_add = QtWidgets.QPushButton(editProfile)
        self.btn_add.setGeometry(QtCore.QRect(300, 300, 75, 23))
        self.btn_add.setFlat(False)
        self.btn_add.setObjectName("btn_add")

        self.btn_add.clicked.connect(self.addRow)
        self.btn_remove.clicked.connect(self.removeRow)

        self.retranslateUi(editProfile)
        self.buttonBox.accepted.connect(editProfile.accept)
        self.buttonBox.clicked['QAbstractButton*'].connect(editProfile.close)
        QtCore.QMetaObject.connectSlotsByName(editProfile)

    def retranslateUi(self, editProfile):
        _translate = QtCore.QCoreApplication.translate
        editProfile.setWindowTitle(_translate("editProfile", "Edit Room"))
        self.EditProfileLabel.setText(_translate("editProfile", "Edit Room Profile"))
        self.btn_add.clicked.connect(self.EditRoom.update)
        self.btn_remove.clicked.connect(self.EditRoom.update)
        self.btn_remove.setText(_translate("editProfile", "Remove labs"))
        self.btn_add.setText(_translate("editProfile", "Add labs"))
        
        for i in range(self.EditRoom.rowCount()):
            item = self.EditRoom.verticalHeaderItem(i)
            item.setText(_translate("editProfile", str(i+1)+"."))

        item = self.EditRoom.horizontalHeaderItem(0)
        item.setText(_translate("editProfile", "Room"))
        item = self.EditRoom.horizontalHeaderItem(1)
        item.setText(_translate("editProfile", "No of students"))
        item = self.EditRoom.horizontalHeaderItem(2)
        item.setText(_translate("editProfile", "No of rows"))
        item = self.EditRoom.horizontalHeaderItem(3)
        item.setText(_translate("editProfile", "No of columns"))
        __sortingEnabled = self.EditRoom.isSortingEnabled()
        self.EditRoom.setSortingEnabled(False)

        for i in range(self.EditRoom.rowCount()):
            item = self.EditRoom.item(i, 0)
            item.setText(_translate("editProfile", "Lab"+str(i+1)))

import images.resources

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    editProfile = QtWidgets.QDialog()
    ui = Ui_editProfile()
    ui.setupUi(editProfile)
    editProfile.show()
    sys.exit(app.exec_())

