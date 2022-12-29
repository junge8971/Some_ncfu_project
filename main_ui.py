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
            MainWindow.setObjectName(u"Main_Window")
        MainWindow.resize(1129, 764)
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

        self.label_input_B = QLabel(self.verticalLayoutWidget)
        self.label_input_B.setObjectName(u"label_input_B")
        self.label_input_B.setFont(font)
        self.label_input_B.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_input_B)

        self.input_B = QLineEdit(self.verticalLayoutWidget)
        self.input_B.setObjectName(u"input_B")

        self.verticalLayout.addWidget(self.input_B)

        self.label_input_H11 = QLabel(self.verticalLayoutWidget)
        self.label_input_H11.setObjectName(u"label_input_H11")
        self.label_input_H11.setFont(font)
        self.label_input_H11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_input_H11)

        self.input_H11 = QLineEdit(self.verticalLayoutWidget)
        self.input_H11.setObjectName(u"input_H11")

        self.verticalLayout.addWidget(self.input_H11)

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
        self.label_Rg.setGeometry(QRect(250, 400, 91, 16))
        self.label_Rg.setAlignment(Qt.AlignCenter)
        self.label_Cr1 = QLabel(self.centralwidget)
        self.label_Cr1.setObjectName(u"label_Cr1")
        self.label_Cr1.setGeometry(QRect(330, 390, 91, 16))
        self.label_Cr1.setAlignment(Qt.AlignCenter)
        self.label_R2 = QLabel(self.centralwidget)
        self.label_R2.setObjectName(u"label_R2")
        self.label_R2.setGeometry(QRect(520, 520, 111, 16))
        self.label_Ce = QLabel(self.centralwidget)
        self.label_Ce.setObjectName(u"label_Ce")
        self.label_Ce.setGeometry(QRect(710, 590, 101, 16))
        self.label_Re = QLabel(self.centralwidget)
        self.label_Re.setObjectName(u"label_Re")
        self.label_Re.setGeometry(QRect(830, 600, 101, 16))
        self.label_R5 = QLabel(self.centralwidget)
        self.label_R5.setObjectName(u"label_R5")
        self.label_R5.setGeometry(QRect(1070, 480, 81, 16))
        self.label_Cr2 = QLabel(self.centralwidget)
        self.label_Cr2.setObjectName(u"label_Cr2")
        self.label_Cr2.setGeometry(QRect(940, 340, 101, 16))
        self.label_Cr2.setAlignment(Qt.AlignCenter)
        self.label_Rk = QLabel(self.centralwidget)
        self.label_Rk.setObjectName(u"label_Rk")
        self.label_Rk.setGeometry(QRect(830, 300, 71, 16))
        self.label_Cb = QLabel(self.centralwidget)
        self.label_Cb.setObjectName(u"label_Cb")
        self.label_Cb.setGeometry(QRect(930, 210, 111, 20))
        self.label_Cb.setAlignment(Qt.AlignCenter)
        self.label_VEk = QLabel(self.centralwidget)
        self.label_VEk.setObjectName(u"label_VEk")
        self.label_VEk.setGeometry(QRect(900, 110, 131, 20))
        self.label_VEk.setAlignment(Qt.AlignCenter)
        self.label_R1 = QLabel(self.centralwidget)
        self.label_R1.setObjectName(u"label_R1")
        self.label_R1.setGeometry(QRect(520, 290, 101, 20))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1129, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("Main_Window", u"Main_Window", None))
        self.label_input_Ube0.setText(QCoreApplication.translate("Main_Window", u"U\u0411\u042d0, \u0412", None))
        self.label_input_Ib0.setText(QCoreApplication.translate("Main_Window", u"I\u04110, \u0410", None))
        self.label_input_Uke0.setText(QCoreApplication.translate("Main_Window", u"U\u041a\u042d0, \u0412", None))
        self.label_input_Ik0.setText(QCoreApplication.translate("Main_Window", u"I\u041a0, \u0410", None))
        self.label_input_B.setText(QCoreApplication.translate("Main_Window", u"\u03b2", None))
        self.label_input_H11.setText(QCoreApplication.translate("Main_Window", u"h11, \u043f\u0435\u0440\u0435\u043c", None))
        self.button_calculate.setText(QCoreApplication.translate("Main_Window", u"\u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0442\u044c", None))
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
        self.label_R1.setText("")
    # retranslateUi

