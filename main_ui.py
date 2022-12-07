# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1320, 764)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 156, 701))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_input_Ube0 = QLabel(self.verticalLayoutWidget)
        self.label_input_Ube0.setObjectName(u"label_input_Ube0")
        font = QFont()
        font.setPointSize(12)
        self.label_input_Ube0.setFont(font)
        self.label_input_Ube0.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_input_Ube0)

        self.input_Ube0 = QLineEdit(self.verticalLayoutWidget)
        self.input_Ube0.setObjectName(u"input_Ube0")

        self.verticalLayout.addWidget(self.input_Ube0)

        self.label_input_Ib0 = QLabel(self.verticalLayoutWidget)
        self.label_input_Ib0.setObjectName(u"label_input_Ib0")
        self.label_input_Ib0.setFont(font)
        self.label_input_Ib0.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_input_Ib0)

        self.input_Ib0 = QLineEdit(self.verticalLayoutWidget)
        self.input_Ib0.setObjectName(u"input_Ib0")

        self.verticalLayout.addWidget(self.input_Ib0)

        self.label_input_Uke0 = QLabel(self.verticalLayoutWidget)
        self.label_input_Uke0.setObjectName(u"label_input_Uke0")
        self.label_input_Uke0.setFont(font)
        self.label_input_Uke0.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_input_Uke0)

        self.input_Uke0 = QLineEdit(self.verticalLayoutWidget)
        self.input_Uke0.setObjectName(u"input_Uke0")

        self.verticalLayout.addWidget(self.input_Uke0)

        self.label_input_Ik0 = QLabel(self.verticalLayoutWidget)
        self.label_input_Ik0.setObjectName(u"label_input_Ik0")
        self.label_input_Ik0.setFont(font)
        self.label_input_Ik0.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_input_Ik0)

        self.input_Ik0 = QLineEdit(self.verticalLayoutWidget)
        self.input_Ik0.setObjectName(u"input_Ik0")

        self.verticalLayout.addWidget(self.input_Ik0)

        self.label_input_Ek = QLabel(self.verticalLayoutWidget)
        self.label_input_Ek.setObjectName(u"label_input_Ek")
        self.label_input_Ek.setFont(font)
        self.label_input_Ek.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_input_Ek)

        self.input_Ek = QLineEdit(self.verticalLayoutWidget)
        self.input_Ek.setObjectName(u"input_Ek")

        self.verticalLayout.addWidget(self.input_Ek)

        self.button_calculate = QPushButton(self.verticalLayoutWidget)
        self.button_calculate.setObjectName(u"button_calculate")

        self.verticalLayout.addWidget(self.button_calculate)

        self.label_error = QLabel(self.verticalLayoutWidget)
        self.label_error.setObjectName(u"label_error")

        self.verticalLayout.addWidget(self.label_error)

        self.img_of_scheme = QLabel(self.centralwidget)
        self.img_of_scheme.setObjectName(u"img_of_scheme")
        self.img_of_scheme.setGeometry(QRect(170, 0, 961, 721))
        self.img_of_scheme.setPixmap(QPixmap(u"img/scheme.jpg"))
        self.pushButton_R1 = QPushButton(self.centralwidget)
        self.pushButton_R1.setObjectName(u"pushButton_R1")
        self.pushButton_R1.setEnabled(True)
        self.pushButton_R1.setGeometry(QRect(460, 270, 31, 51))
        self.pushButton_R1.setAutoFillBackground(False)
        self.pushButton_R1.setFlat(True)
        self.pushButton_R2 = QPushButton(self.centralwidget)
        self.pushButton_R2.setObjectName(u"pushButton_R2")
        self.pushButton_R2.setGeometry(QRect(462, 500, 31, 41))
        self.pushButton_R2.setFlat(True)
        self.pushButton_Rg = QPushButton(self.centralwidget)
        self.pushButton_Rg.setObjectName(u"pushButton_Rg")
        self.pushButton_Rg.setGeometry(QRect(280, 440, 41, 20))
        self.pushButton_Rg.setFlat(True)
        self.pushButton_Cr1 = QPushButton(self.centralwidget)
        self.pushButton_Cr1.setObjectName(u"pushButton_Cr1")
        self.pushButton_Cr1.setGeometry(QRect(360, 440, 41, 31))
        self.pushButton_Cr1.setFlat(True)
        self.pushButton_Ce = QPushButton(self.centralwidget)
        self.pushButton_Ce.setObjectName(u"pushButton_Ce")
        self.pushButton_Ce.setGeometry(QRect(642, 580, 31, 28))
        self.pushButton_Ce.setFlat(True)
        self.pushButton_Re = QPushButton(self.centralwidget)
        self.pushButton_Re.setObjectName(u"pushButton_Re")
        self.pushButton_Re.setGeometry(QRect(780, 580, 20, 51))
        self.pushButton_Re.setFlat(True)
        self.pushButton_R5 = QPushButton(self.centralwidget)
        self.pushButton_R5.setObjectName(u"pushButton_R5")
        self.pushButton_R5.setGeometry(QRect(1022, 460, 21, 41))
        self.pushButton_R5.setFlat(True)
        self.pushButton_Cr2 = QPushButton(self.centralwidget)
        self.pushButton_Cr2.setObjectName(u"pushButton_Cr2")
        self.pushButton_Cr2.setGeometry(QRect(970, 390, 41, 28))
        self.pushButton_Cr2.setFlat(True)
        self.pushButton_Rk = QPushButton(self.centralwidget)
        self.pushButton_Rk.setObjectName(u"pushButton_Rk")
        self.pushButton_Rk.setGeometry(QRect(782, 287, 21, 41))
        self.pushButton_Rk.setFlat(True)
        self.pushButton_generator = QPushButton(self.centralwidget)
        self.pushButton_generator.setObjectName(u"pushButton_generator")
        self.pushButton_generator.setGeometry(QRect(170, 397, 61, 41))
        self.pushButton_generator.setFlat(True)
        self.pushButton_blood_ploter = QPushButton(self.centralwidget)
        self.pushButton_blood_ploter.setObjectName(u"pushButton_blood_ploter")
        self.pushButton_blood_ploter.setGeometry(QRect(710, 20, 93, 31))
        self.pushButton_blood_ploter.setFlat(True)
        self.pushButton_oscilloscope = QPushButton(self.centralwidget)
        self.pushButton_oscilloscope.setObjectName(u"pushButton_oscilloscope")
        self.pushButton_oscilloscope.setGeometry(QRect(822, 100, 71, 28))
        self.pushButton_oscilloscope.setFlat(True)
        self.pushButton_VEk = QPushButton(self.centralwidget)
        self.pushButton_VEk.setObjectName(u"pushButton_VEk")
        self.pushButton_VEk.setGeometry(QRect(950, 170, 31, 28))
        self.pushButton_VEk.setFlat(True)
        self.pushButton_Cb = QPushButton(self.centralwidget)
        self.pushButton_Cb.setObjectName(u"pushButton_Cb")
        self.pushButton_Cb.setGeometry(QRect(970, 250, 41, 28))
        self.pushButton_Cb.setFlat(True)
        self.label_Rg = QLabel(self.centralwidget)
        self.label_Rg.setObjectName(u"label_Rg")
        self.label_Rg.setGeometry(QRect(260, 480, 91, 16))
        self.label_Cr1 = QLabel(self.centralwidget)
        self.label_Cr1.setObjectName(u"label_Cr1")
        self.label_Cr1.setGeometry(QRect(360, 400, 91, 16))
        self.label_R2 = QLabel(self.centralwidget)
        self.label_R2.setObjectName(u"label_R2")
        self.label_R2.setGeometry(QRect(490, 550, 111, 16))
        self.label_Ce = QLabel(self.centralwidget)
        self.label_Ce.setObjectName(u"label_Ce")
        self.label_Ce.setGeometry(QRect(670, 610, 101, 16))
        self.label_Re = QLabel(self.centralwidget)
        self.label_Re.setObjectName(u"label_Re")
        self.label_Re.setGeometry(QRect(810, 630, 101, 16))
        self.label_R5 = QLabel(self.centralwidget)
        self.label_R5.setObjectName(u"label_R5")
        self.label_R5.setGeometry(QRect(1040, 510, 81, 16))
        self.label_Cr2 = QLabel(self.centralwidget)
        self.label_Cr2.setObjectName(u"label_Cr2")
        self.label_Cr2.setGeometry(QRect(930, 340, 101, 16))
        self.label_Rk = QLabel(self.centralwidget)
        self.label_Rk.setObjectName(u"label_Rk")
        self.label_Rk.setGeometry(QRect(800, 330, 71, 16))
        self.label_Cb = QLabel(self.centralwidget)
        self.label_Cb.setObjectName(u"label_Cb")
        self.label_Cb.setGeometry(QRect(940, 210, 111, 20))
        self.label_Cb.setAlignment(Qt.AlignCenter)
        self.label_VEk = QLabel(self.centralwidget)
        self.label_VEk.setObjectName(u"label_VEk")
        self.label_VEk.setGeometry(QRect(914, 120, 131, 20))
        self.label_VEk.setAlignment(Qt.AlignCenter)

        # input_values
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1130, 10, 181, 181))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_for_input_value_object = QLabel(self.verticalLayoutWidget_2)
        self.label_for_input_value_object.setObjectName(u"label_for_input_value_object")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_for_input_value_object.setFont(font1)
        self.label_for_input_value_object.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_for_input_value_object)

        self.input_value_object = QLineEdit(self.verticalLayoutWidget_2)
        self.input_value_object.setObjectName(u"input_value_object")

        self.verticalLayout_2.addWidget(self.input_value_object)

        self.pushButton_for_input_value_object = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_for_input_value_object.setObjectName(u"pushButton_for_input_value_object")

        self.verticalLayout_2.addWidget(self.pushButton_for_input_value_object)
        # end_input_values

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(1130, 200, 181, 351))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_generator = QLabel(self.verticalLayoutWidget_3)
        self.label_generator.setObjectName(u"label_generator")
        self.label_generator.setFont(font1)
        self.label_generator.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_generator)

        self.label_generator_frequency = QLabel(self.verticalLayoutWidget_3)
        self.label_generator_frequency.setObjectName(u"label_generator_frequency")
        self.label_generator_frequency.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_generator_frequency)

        self.input_generator_frequency = QLineEdit(self.verticalLayoutWidget_3)
        self.input_generator_frequency.setObjectName(u"input_generator_frequency")

        self.verticalLayout_3.addWidget(self.input_generator_frequency)

        self.label_generator_duty_cycle = QLabel(self.verticalLayoutWidget_3)
        self.label_generator_duty_cycle.setObjectName(u"label_generator_duty_cycle")
        self.label_generator_duty_cycle.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_generator_duty_cycle)

        self.input_generator_duty_cycle = QLineEdit(self.verticalLayoutWidget_3)
        self.input_generator_duty_cycle.setObjectName(u"input_generator_duty_cycle")

        self.verticalLayout_3.addWidget(self.input_generator_duty_cycle)

        self.label_generator_amplitude = QLabel(self.verticalLayoutWidget_3)
        self.label_generator_amplitude.setObjectName(u"label_generator_amplitude")
        self.label_generator_amplitude.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_generator_amplitude)

        self.input_generator_amplitude = QLineEdit(self.verticalLayoutWidget_3)
        self.input_generator_amplitude.setObjectName(u"input_generator_amplitude")

        self.verticalLayout_3.addWidget(self.input_generator_amplitude)

        self.label_generator_offset = QLabel(self.verticalLayoutWidget_3)
        self.label_generator_offset.setObjectName(u"label_generator_offset")
        self.label_generator_offset.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_generator_offset)

        self.input_generator_offset = QLineEdit(self.verticalLayoutWidget_3)
        self.input_generator_offset.setObjectName(u"input_generator_offset")

        self.verticalLayout_3.addWidget(self.input_generator_offset)

        self.pushButton_input_generator = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_input_generator.setObjectName(u"pushButton_input_generator")

        self.verticalLayout_3.addWidget(self.pushButton_input_generator)

        self.label_R1 = QLabel(self.centralwidget)
        self.label_R1.setObjectName(u"label_R1")
        self.label_R1.setGeometry(QRect(500, 320, 101, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1320, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi
    '''
    def init_input_for(self):
        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(1130, 10, 181, 181))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_for_input_value_object = QLabel(self.verticalLayoutWidget_2)
        self.label_for_input_value_object.setObjectName(u"label_for_input_value_object")
        font1 = QFont()
        font1.setPointSize(10)
        self.label_for_input_value_object.setFont(font1)
        self.label_for_input_value_object.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_for_input_value_object)

        self.input_value_object = QLineEdit(self.verticalLayoutWidget_2)
        self.input_value_object.setObjectName(u"input_value_object")

        self.verticalLayout_2.addWidget(self.input_value_object)

        self.pushButton_for_input_value_object = QPushButton(self.verticalLayoutWidget_2)
        self.pushButton_for_input_value_object.setObjectName(u"pushButton_for_input_value_object")

        self.verticalLayout_2.addWidget(self.pushButton_for_input_value_object)
    '''

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_input_Ube0.setText(QCoreApplication.translate("MainWindow", u"U\u0411\u042d0, \u043c\u0412", None))
        self.label_input_Ib0.setText(QCoreApplication.translate("MainWindow", u"I\u04110, \u043c\u043a\u0410", None))
        self.label_input_Uke0.setText(QCoreApplication.translate("MainWindow", u"U\u041a\u042d0, \u0412", None))
        self.label_input_Ik0.setText(QCoreApplication.translate("MainWindow", u"I\u041a0, \u043c\u0410", None))
        self.label_input_Ek.setText(QCoreApplication.translate("MainWindow", u"(EK), \u0412", None))
        self.button_calculate.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
        self.label_error.setText("")
        self.img_of_scheme.setText("")
        self.pushButton_R1.setText("")
        self.pushButton_R2.setText("")
        self.pushButton_Rg.setText("")
        self.pushButton_Cr1.setText("")
        self.pushButton_Ce.setText("")
        self.pushButton_Re.setText("")
        self.pushButton_R5.setText("")
        self.pushButton_Cr2.setText("")
        self.pushButton_Rk.setText("")
        self.pushButton_generator.setText("")
        self.pushButton_blood_ploter.setText("")
        self.pushButton_oscilloscope.setText("")
        self.pushButton_VEk.setText("")
        self.pushButton_Cb.setText("")
        self.label_Rg.setText("")
        self.label_Cr1.setText("")
        self.label_R2.setText("")
        self.label_Ce.setText("")
        self.label_Re.setText("")
        self.label_R5.setText("")
        self.label_Cr2.setText("")
        self.label_Rk.setText("")
        self.label_Cb.setText("")
        self.label_VEk.setText("")
        self.label_for_input_value_object.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0438\u0447\u0435\u0433\u043e \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d\u043e", None))
        self.pushButton_for_input_value_object.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0441\u0442\u0438", None))
        self.label_generator.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0430\u0442\u043e\u0440", None))
        self.label_generator_frequency.setText(QCoreApplication.translate("MainWindow", u"\u0427\u0430\u0441\u0442\u043e\u0442\u0430", None))
        self.label_generator_duty_cycle.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0431\u043e\u0447\u0438\u0439 \u0446\u0438\u043a\u043b", None))
        self.label_generator_amplitude.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043c\u043f\u043b\u0438\u0442\u0443\u0434\u0430", None))
        self.label_generator_offset.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043c\u043f\u0435\u043d\u0441\u0430\u0446\u0438\u044f", None))
        self.pushButton_input_generator.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.label_R1.setText("")
    # retranslateUi

