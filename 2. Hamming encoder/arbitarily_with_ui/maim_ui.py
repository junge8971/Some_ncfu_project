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
        MainWindow.resize(1127, 822)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 10, 331, 291))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)

        self.verticalLayout.addWidget(self.label)

        self.message_len = QLineEdit(self.verticalLayoutWidget)
        self.message_len.setObjectName(u"message_len")

        self.verticalLayout.addWidget(self.message_len)

        self.message_len_button = QPushButton(self.verticalLayoutWidget)
        self.message_len_button.setObjectName(u"message_len_button")

        self.verticalLayout.addWidget(self.message_len_button)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(350, 10, 426, 287))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_2)

        self.input_message = QTextEdit(self.verticalLayoutWidget_2)
        self.input_message.setObjectName(u"input_message")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.input_message.sizePolicy().hasHeightForWidth())
        self.input_message.setSizePolicy(sizePolicy)
        self.input_message.setLineWrapMode(QTextEdit.NoWrap)

        self.verticalLayout_2.addWidget(self.input_message)

        self.generate_message = QPushButton(self.verticalLayoutWidget_2)
        self.generate_message.setObjectName(u"generate_message")

        self.verticalLayout_2.addWidget(self.generate_message)

        self.encode_message = QPushButton(self.verticalLayoutWidget_2)
        self.encode_message.setObjectName(u"encode_message")

        self.verticalLayout_2.addWidget(self.encode_message)

        self.verticalLayoutWidget_4 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_4.setObjectName(u"verticalLayoutWidget_4")
        self.verticalLayoutWidget_4.setGeometry(QRect(10, 310, 331, 251))
        self.verticalLayout_4 = QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.verticalLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.label_7)

        self.modify_and_decod_input = QLineEdit(self.verticalLayoutWidget_4)
        self.modify_and_decod_input.setObjectName(u"modify_and_decod_input")

        self.verticalLayout_4.addWidget(self.modify_and_decod_input)

        self.modify_and_decod_button = QPushButton(self.verticalLayoutWidget_4)
        self.modify_and_decod_button.setObjectName(u"modify_and_decod_button")

        self.verticalLayout_4.addWidget(self.modify_and_decod_button)

        self.verticalLayoutWidget_5 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_5.setObjectName(u"verticalLayoutWidget_5")
        self.verticalLayoutWidget_5.setGeometry(QRect(780, 300, 341, 341))
        self.verticalLayout_5 = QVBoxLayout(self.verticalLayoutWidget_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_input_data = QLabel(self.verticalLayoutWidget_5)
        self.label_input_data.setObjectName(u"label_input_data")
        self.label_input_data.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_input_data)

        self.label_encoded = QLabel(self.verticalLayoutWidget_5)
        self.label_encoded.setObjectName(u"label_encoded")
        self.label_encoded.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_encoded)

        self.label_modifaed = QLabel(self.verticalLayoutWidget_5)
        self.label_modifaed.setObjectName(u"label_modifaed")
        self.label_modifaed.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_modifaed)

        self.label_binary_syndrome_and_error_pos = QLabel(self.verticalLayoutWidget_5)
        self.label_binary_syndrome_and_error_pos.setObjectName(u"label_binary_syndrome_and_error_pos")
        self.label_binary_syndrome_and_error_pos.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_binary_syndrome_and_error_pos)

        self.label_decode = QLabel(self.verticalLayoutWidget_5)
        self.label_decode.setObjectName(u"label_decode")
        self.label_decode.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.label_decode)

        self.verticalLayoutWidget_6 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_6.setObjectName(u"verticalLayoutWidget_6")
        self.verticalLayoutWidget_6.setGeometry(QRect(780, 10, 341, 291))
        self.verticalLayout_6 = QVBoxLayout(self.verticalLayoutWidget_6)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_message_len = QLabel(self.verticalLayoutWidget_6)
        self.label_message_len.setObjectName(u"label_message_len")
        self.label_message_len.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_message_len)

        self.label_number_of_check_bit = QLabel(self.verticalLayoutWidget_6)
        self.label_number_of_check_bit.setObjectName(u"label_number_of_check_bit")
        self.label_number_of_check_bit.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_number_of_check_bit)

        self.label_coder_type = QLabel(self.verticalLayoutWidget_6)
        self.label_coder_type.setObjectName(u"label_coder_type")
        self.label_coder_type.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_coder_type)

        self.label_check_indices = QLabel(self.verticalLayoutWidget_6)
        self.label_check_indices.setObjectName(u"label_check_indices")
        self.label_check_indices.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_check_indices)

        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(349, 309, 421, 331))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_matrix_info = QLabel(self.verticalLayoutWidget_3)
        self.label_matrix_info.setObjectName(u"label_matrix_info")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_matrix_info.sizePolicy().hasHeightForWidth())
        self.label_matrix_info.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.label_matrix_info)

        self.label_matrix = QLabel(self.verticalLayoutWidget_3)
        self.label_matrix.setObjectName(u"label_matrix")

        self.verticalLayout_3.addWidget(self.label_matrix)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1127, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0441\u0438\u043c\u0432\u043e\u043b \u0434\u043b\u044f \u0438\u0441\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u043d\u0438\u0435 \u0431\u043b\u043e\u0447\u043d\u043e\u0433\u043e \u043a\u043e\u0434\u0430", None))
        self.message_len_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0441\u0442\u0438", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0432\u0435\u0434\u0438\u0442\u0435 \u0438\u043b\u0438 \u0441\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u0439\u0442\u0435 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u0441 \u0437\u0430\u0434\u0430\u043d\u043d\u043e\u0439 \u043f\u043e \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u0443 \u0434\u043b\u0438\u043d\u043d\u043e\u0439", None))
        self.generate_message.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0433\u0435\u043d\u0435\u0440\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.encode_message.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0441\u0438\u0442\u0435 \u0430\u0434\u0440\u0435\u0441 \u0438\u043b\u0438 \u0430\u0434\u0440\u0435\u0441\u0430 \u0440\u0430\u0437\u0440\u0430\u0434\u043e\u0432 \u0434\u043b\u044f \u0432\u043d\u0435\u0441\u0435\u043d\u0438\u044f \u043e\u0448\u0438\u0431\u043a\u0438", None))
        self.modify_and_decod_button.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043d\u0435\u0441\u0442\u0438 \u043e\u0448\u0438\u0431\u043a\u0443 \u0438 \u0434\u0435\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u0442\u044c", None))
        self.label_input_data.setText(QCoreApplication.translate("MainWindow", u"\u0418\u0441\u0445\u043e\u0434\u043d\u044b\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0431\u043b\u043e\u043a: ", None))
        self.label_encoded.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0431\u043b\u043e\u043a: ", None))
        self.label_modifaed.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0434\u0438\u0444\u0438\u0446\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0431\u043b\u043e\u043a: ", None))
        self.label_binary_syndrome_and_error_pos.setText(QCoreApplication.translate("MainWindow", u"\u0421\u0438\u043d\u0434\u043e\u043c \u0438 \u043f\u043e\u0437\u0438\u0446\u0438\u044e \u043e\u0448\u0438\u0431\u043a\u0438: ", None))
        self.label_decode.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0435\u043a\u043e\u0434\u0438\u0440\u043e\u0432\u0430\u043d\u043d\u044b\u0439 \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0439 \u0431\u043b\u043e\u043a: ", None))
        self.label_message_len.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u043d\u0430 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f:", None))
        self.label_number_of_check_bit.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u0440\u043e\u0432\u0435\u0440\u043e\u0447\u043d\u044b\u0445 \u0431\u0438\u0442: ", None))
        self.label_coder_type.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0438\u043f  \u0431\u043b\u043e\u0447\u043d\u043e\u0433\u043e \u043a\u043e\u0434\u0430 \u0425\u044d\u043c\u043c\u0438\u043d\u0433\u0430: ", None))
        self.label_check_indices.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043e\u0440\u0434\u0438\u043d\u0430\u0442\u044b \u043f\u0440\u043e\u0432\u0435\u0440\u043e\u0447\u043d\u044b\u0445 \u0431\u0438\u0442: ", None))
        self.label_matrix_info.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0435\u043d\u0435\u0440\u0438\u0440\u0443\u044e\u0449\u0430\u044f \u043c\u0430\u0442\u0440\u0438\u0446\u0430:", None))
        self.label_matrix.setText("")
    # retranslateUi

