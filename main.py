#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2.QtWidgets import QWidget,\
    QHBoxLayout,\
    QVBoxLayout,\
    QLineEdit,\
    QPushButton,\
    QApplication


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Контрольная работа")

        # Входные параметры для вычисления
        self.input_Ube0 = QLineEdit()  # UБЭ0, мВ
        self.input_Ib0 = QLineEdit()  # IБ0, мкА
        self.input_Uke0 = QLineEdit()  # UКЭ0, В
        self.input_Ik0 = QLineEdit()  # IК0, мА
        self.input_Ek = QLineEdit()  # Источник питания (EK), В
        self.button_calculate = QPushButton('Расчитать')

        self.init_UI()

    def init_UI(self):
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        v_layout.addLayout(h_layout)
        h_layout.addWidget(self.input_Ube0)
        h_layout.addWidget(self.input_Ib0)
        h_layout.addWidget(self.input_Uke0)
        h_layout.addWidget(self.input_Ik0)
        h_layout.addWidget(self.input_Ek)
        h_layout.addWidget(self.button_calculate)
        self.setLayout(v_layout)

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
