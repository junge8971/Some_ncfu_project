#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
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
        self.label_error = QLabel()

        # Схема
        self.img = QPixmap('img/scheme.jpg')
        self.img_of_scheme = QLabel(self)
        self.img_of_scheme.setPixmap(self.img)

        self.init_UI()

    def init_UI(self):
        h0_labels_for_input_layout = QHBoxLayout()
        h1_inputs_to_start_layout = QHBoxLayout()
        h2_img_and_menu_layout = QHBoxLayout()
        h3_for_error_masages_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        v_layout.addLayout(h0_labels_for_input_layout)
        v_layout.addLayout(h1_inputs_to_start_layout)
        v_layout.addLayout(h2_img_and_menu_layout)
        v_layout.addLayout(h3_for_error_masages_layout)

        h0_labels_for_input_layout.addWidget(self.label_input_Ube0)
        h0_labels_for_input_layout.addWidget(self.label_input_Ib0)
        h0_labels_for_input_layout.addWidget(self.label_input_Uke0)
        h0_labels_for_input_layout.addWidget(self.label_input_Ik0)
        h0_labels_for_input_layout.addWidget(self.label_input_Ek)

        h1_inputs_to_start_layout.addWidget(self.input_Ube0)
        h1_inputs_to_start_layout.addWidget(self.input_Ib0)
        h1_inputs_to_start_layout.addWidget(self.input_Uke0)
        h1_inputs_to_start_layout.addWidget(self.input_Ik0)
        h1_inputs_to_start_layout.addWidget(self.input_Ek)
        h1_inputs_to_start_layout.addWidget(self.button_calculate)

        h2_img_and_menu_layout.addWidget(self.img_of_scheme)

        h3_for_error_masages_layout.addWidget(self.label_error)
        self.setLayout(v_layout)

    def culc(self):
        Ube0 = self.input_Ube0.text()
        Ib0 = self.input_Ib0.text()
        Uke0 = self.input_Uke0.text()
        Ik0 = self.input_Ik0.text()
        Ek = self.input_Ek.text()
        if Ube0 and Ib0 and Uke0 and Ik0 and Ek:
            Ube0 = self.convert_input_to_num(Ube0)

    def convert_input_to_num(self, input_string: str) -> float:
        params_dict_ru = {'П': [10, -12],
                          'Н': [10, -9],
                          'мк': [10, -6],
                          'м': [10, -3],
                          'C': [10, -2],
                          'Д': [10, -1],
                          'да': [10, 1],
                          'г': [10, 2],
                          'К': [10, 3],
                          'М': [10, 6],
                          'Г': [10, 9],
                          'Т': [10, 12]
                          }
        num, postfix = input_string.split(' ')
        if postfix in params_dict_ru:
            params_postfix = params_dict_ru.get(postfix)
            result = float(num) * pow(params_postfix[0], params_postfix[1])
            return result
        else:
            self.label_error.setText(f'Неправильно введено значение: {input_string}')


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
