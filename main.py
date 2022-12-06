#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget,\
    QHBoxLayout,\
    QVBoxLayout,\
    QLineEdit,\
    QPushButton,\
    QApplication, \
    QLabel
from PySide2.QtGui import QPixmap


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Контрольная работа")

        # Входные параметры для вычисления
        self.label_input_Ube0 = QLabel('UБЭ0, мВ')
        self.input_Ube0 = QLineEdit()  # UБЭ0, мВ
        self.label_input_Ib0 = QLabel('IБ0, мкА')
        self.input_Ib0 = QLineEdit()  # IБ0, мкА
        self.label_input_Uke0 = QLabel('UКЭ0, В')
        self.input_Uke0 = QLineEdit()  # UКЭ0, В
        self.label_input_Ik0 = QLabel('IК0, мА')
        self.input_Ik0 = QLineEdit()  # IК0, мА
        self.label_input_Ek = QLabel('(EK), В')
        self.input_Ek = QLineEdit()  # Источник питания (EK), В
        self.button_calculate = QPushButton('Расчитать')
        self.button_calculate.clicked.connect(self.culc)

        # Схема
        self.img = QPixmap('img/scheme.jpg')
        self.img_of_scheme = QLabel(self)
        self.img_of_scheme.setPixmap(self.img)

        self.init_UI()

    def init_UI(self):
        h0_layout = QHBoxLayout()
        h1_layout = QHBoxLayout()
        h2_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        v_layout.addLayout(h0_layout)
        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)

        h0_layout.addWidget(self.label_input_Ube0)
        h0_layout.addWidget(self.label_input_Ib0)
        h0_layout.addWidget(self.label_input_Uke0)
        h0_layout.addWidget(self.label_input_Ik0)
        h0_layout.addWidget(self.label_input_Ek)

        h1_layout.addWidget(self.input_Ube0)
        h1_layout.addWidget(self.input_Ib0)
        h1_layout.addWidget(self.input_Uke0)
        h1_layout.addWidget(self.input_Ik0)
        h1_layout.addWidget(self.input_Ek)
        h1_layout.addWidget(self.button_calculate)

        h2_layout.addWidget(self.img_of_scheme)
        self.setLayout(v_layout)

    def culc(self):
        Ube0 = self.input_Ube0.text()
        Ib0 = self.input_Ib0.text()
        Uke0 = self.input_Uke0.text()
        Ik0 = self.input_Ik0.text()
        Ek = self.input_Ek.text()
        if Ube0 and Ib0 and Uke0 and Ik0 and Ek:
            print(1)


class HorizontalResistor:
    def __init__(self, x, y, r_value):
        self.button_x = int(x)
        self.button_y = int(y)
        self.resistance_value = float(r_value)

        self.label_x = self.button_x
        self.label_y = self.button_y + 3


def main():
    if __name__ == "__main__":
        application = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(application.exec_())


if __name__ == '__main__':
    main()
