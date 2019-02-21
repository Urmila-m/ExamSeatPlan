from PyQt5.QtWidgets import QWidget, QApplication, QDateTimeEdit, QHBoxLayout
from PyQt5 import QtGui, QtCore

class MyWindow(QWidget):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)

        self.dateEdit = QDateTimeEdit(self)
        self.dateEdit.setDateTime(QtCore.QDateTime.currentDateTime())
        self.dateEdit.setMaximumDate(QtCore.QDate(7999, 12, 28))
        self.dateEdit.setMaximumTime(QtCore.QTime(23, 59, 59))
        self.dateEdit.setCalendarPopup(True)

        self.layoutHorizontal = QHBoxLayout(self)
        self.layoutHorizontal.addWidget(self.dateEdit)

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    app.setApplicationName('MyWindow')

    main = MyWindow()
    main.show()

    sys.exit(app.exec_())