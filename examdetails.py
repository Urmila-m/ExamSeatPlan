import sys
import pandas as pd
import math
from config import *
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QCheckBox\
                            , QApplication, QRadioButton, QLabel, QLineEdit, QCalendarWidget,\
                                QTimeEdit
from PyQt5.QtCore import Qt, pyqtSlot, QDate, QTime
from PyQt5.QtGui import QPixmap, QFont

class Examdetails(QWidget):
    def __init__(self, dataframes):
        super().__init__()
        self.title = window_title
        self.left = window_left
        self.top = window_top
        self.width = window_width
        self.height = window_height
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.exam_halldf = pd.read_excel('Res/room_profile.xlsx') 
        self.exam_hall = self.exam_halldf['Exam Hall'].values
        self.dataframes = dataframes
        self.num_student = sum(map(len, self.dataframes))
    
    def examdetails_gui(self):
        vertical_layout = QVBoxLayout()

        # check box according to room profile
        horizontal_layoutcheckbox = QHBoxLayout()
        text_choose = QLabel('Choose Exam Hall')
        text_choose.setFont(QFont("Arial", 15, QFont.Bold))
        horizontal_layoutcheckbox.addWidget(text_choose)

        self.check_boxes = list()
        for hall in self.exam_hall:
            check_box = QCheckBox(hall)
            self.check_boxes.append(check_box)
        
        check_box_groups = list()
        check_box_rows = math.ceil(len(self.check_boxes)/8)
        for row in range(check_box_rows): #  no of checkbox in one line = 8
            check_box_groupR = list()
            for check_box in self.check_boxes[(row)*8 : (row+1) *8]:
                check_box_groupR.append(check_box)
            check_box_groups.append(check_box_groupR)


        vertical_layoutcheckboxgroup = QVBoxLayout()
        vertical_layoutcheckboxgroup.addStretch(2)
        for check_box_group in check_box_groups:
            horizontal_layoutcheckboxgroup = QHBoxLayout()
            for check_box in check_box_group:
                check_box.clicked.connect(self.update_seat)
                horizontal_layoutcheckboxgroup.addWidget(check_box)
            vertical_layoutcheckboxgroup.addLayout(horizontal_layoutcheckboxgroup)
        vertical_layoutcheckboxgroup.addStretch(1)
        
        horizontal_layoutcheckbox.addLayout(vertical_layoutcheckboxgroup)

        horizontal_layoutcheckbox.addStretch(1)

        # info text
        self.num_studenttext = QLabel('No of student is '+ str(self.num_student))
        self.num_seattext = QLabel()
        self.num_studenttext.setFont(QFont("Arial", 15))
        self.num_seattext.setFont(QFont("Arial", 15))

        #Create buttons'Back' and 'Generate'
        horizontal_layoutbutton = QHBoxLayout()
        self.button_generate = QPushButton('Generate')
        self.button_back = QPushButton('Back')
        horizontal_layoutbutton.addWidget(self.button_back)
        horizontal_layoutbutton.addWidget(self.button_generate)

        #text box
        horizontal_layouttext = QHBoxLayout()
        exam_namelabel = QLabel('Enter Examination')
        exam_namelabel.setFont(QFont("Arial", 15, QFont.Bold))
        self.exam_name = QLineEdit()
        horizontal_layouttext.addWidget(exam_namelabel)
        horizontal_layouttext.addWidget(self.exam_name)

        # Calender widget
        vertical_layoutcalender = QVBoxLayout()
        self.calender = QCalendarWidget()
        self.calender.setFixedSize(350,250)
        self.label_date = QLabel()
        self.showDate()
        self.calender.setGridVisible(True)
        self.calender.clicked.connect(self.showDate)
        calender_head = QLabel('Examination Date')
        calender_head.setAlignment(Qt.AlignCenter)
        calender_head.setFont(QFont("Arial", 15, QFont.Bold))        
        vertical_layoutcalender.addWidget(calender_head)
        vertical_layoutcalender.addWidget(self.calender)
        vertical_layoutcalender.addWidget(self.label_date)

        # Time widget
        text_from = QLabel('Exam From:')
        text_to = QLabel('Exam To:')
        time_from = QTimeEdit(QTime.currentTime())
        time_to = QTimeEdit(QTime.currentTime())
        horizontal_layouttime = QHBoxLayout()
        horizontal_layouttime.addWidget(text_from)
        horizontal_layouttime.addWidget(time_from)
        horizontal_layouttime.addWidget(text_to)
        horizontal_layouttime.addWidget(time_to)
    
        #Calender and time

        vertical_layoutcalendertime = QVBoxLayout()
        vertical_layoutcalendertime.addLayout(vertical_layoutcalender)
        vertical_layoutcalendertime.addLayout(horizontal_layouttime)

        # radio button for seat plan
        self.radio_linear = QRadioButton('Linear')
        self.radio_fill = QRadioButton('Fill')
        self.radio_fill.setChecked(True)
        horizontal_layoutradio = QHBoxLayout()
        text_choose_style = QLabel('Choose Seat Style')
        text_choose_style.setFont(QFont("Arial", 15, QFont.Bold))
        horizontal_layoutradio.addWidget(text_choose_style)
        horizontal_layoutradio.addWidget(self.radio_linear)
        horizontal_layoutradio.addWidget(self.radio_fill)
        horizontal_layoutradio.addStretch(1)
        
        vertical_layout.addLayout(horizontal_layouttext)
        horizontal_layoutcheckbox.addLayout(vertical_layoutcalendertime)
        vertical_layout.addLayout(horizontal_layoutcheckbox)
        vertical_layout.addLayout(horizontal_layoutradio)
        vertical_layout.addStretch(1)
        vertical_layout.addWidget(self.num_studenttext)
        vertical_layout.addWidget(self.num_seattext)
        vertical_layout.addLayout(horizontal_layoutbutton)
        self.layout = vertical_layout
        self.setLayout(self.layout)
        #add lister to the buttons
        self.button_back.clicked.connect(self.back_clicked)
        self.button_generate.clicked.connect(self.generate_clicked)
        self.update_seat()

    @pyqtSlot()
    def back_clicked(self):
        print('back button pressed')

    @pyqtSlot()
    def generate_clicked(self):
        print('generate button pressed')

    @pyqtSlot()
    def showDate(self):
        date = self.calender.selectedDate()     
        self.label_date.setText('Exam Date :- ' +date.toString())
        self.label_date.setFont(QFont("Arial", 12, QFont.Bold))
    
    @pyqtSlot()
    def update_seat(self):
        self.num_seat = 0
        hall_name = str()
        self.halls_info = list()
        for check_box in self.check_boxes:
            if check_box.isChecked():
                exam_hall = self.exam_halldf.set_index(['Exam Hall'])
                hall_name = str(check_box.text()).replace('&','')
                hall = exam_hall.loc[[hall_name]]
                self.num_seat += int(hall['Rows']) * int(hall['Columns'])
                hall_info = (hall_name,int(hall['Rows']),  int(hall['Columns']))
                self.halls_info.append(hall_info)
        
        color = 'red'
        self.button_generate.setEnabled(False)
        if self.num_seat > self.num_student:
            color = 'green'
            self.button_generate.setEnabled(True)

        
        self.num_seattext.setText('<font color='+ color +'>No. of Seat is '+ str(self.num_seat)+' </font>')
    

if __name__ == '__main__':
    App = QApplication(sys.argv)
    app = Examdetails([pd.read_excel('testdata.xlsx')])
    app.examdetails_gui()
    app.show()
    sys.exit(App.exec_())
