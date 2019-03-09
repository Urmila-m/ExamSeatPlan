from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableView
import sys
import pandas as pd
Qt = QtCore.Qt

class PandasModel(QtCore.QAbstractTableModel):
    '''
    Subclassing QAbstractTableModel to use pandas dataframe.
    '''
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def headerData(self, col, orientation, role):
        if orientation == QtCore.Qt.Horizontal and role == QtCore.Qt.DisplayRole:
            return self._data.columns[col]
        return None

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]))
        return QtCore.QVariant()

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable | Qt.ItemIsEditable

    def get_roomprofile(self):
        return self._data

    def remove_row(self):
        self._data = self._data[:-1]
        self.beginResetModel()
        self.endResetModel()

    def add_row(self):
        index = len(self._data.values)
        default = ['New room', 5, 5, 25]
        self._data.loc[index] = default
        #Reseting model(bad implementation better use datachanged.emit later)
        self.beginResetModel()
        self.endResetModel()
        

    def setData(self, index, value, role):
        if not index.isValid():
            return False
        if role != QtCore.Qt.EditRole:
            return False
        row = index.row()
        if row < 0 or row >= len(self._data.values):
            return False
        column = index.column()
        if column < 0 or column >= self._data.columns.size:
            return False
        self._data.iloc[row, column] = value
        self.dataChanged.emit(index, index)
        return True

if __name__ == '__main__':
    application = QtWidgets.QApplication(sys.argv)
    view = QTableView()

    df = pd.read_excel('testdata')
    model = PandasModel(df)
    view.setModel(model)

    view.show()
    sys.exit(application.exec_())