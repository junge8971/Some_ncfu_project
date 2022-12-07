#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtGui import QPixmap
from main_ui import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Контрольная работа")
        self.setupUi(self)
        self.show()


    def culc(self):
        Ube0 = self.input_Ube0.text()
        Ib0 = self.input_Ib0.text()
        Uke0 = self.input_Uke0.text()
        Ik0 = self.input_Ik0.text()
        Ek = self.input_Ek.text()
        if Ube0 and Ib0 and Uke0 and Ik0 and Ek:
            Ube0 = self.convert_input_to_num(Ube0)
            Ib0 = self.convert_input_to_num(Ib0)
            Uke0 = self.convert_input_to_num(Uke0)
            Ik0 = self.convert_input_to_num(Ik0)
            Ek = self.convert_input_to_num(Ek)

            Rke = (Ek - Uke0) / Ik0  # сопротивление цепи эмиттер-коллектор
            Ikn = Ek / Rke  # постоянный коллекторный ток насыщения транзистора
            Ie0 = Ik0 + Ib0  # постоянный эмиттерный ток в режиме покоя транзистора
            URe = 0.01 * Ek  # падение напряжения на сопротивлении эмиттера
            Re = URe / Ie0  # сопротивление в цепи эмиттера, обеспечивающее отрицательную обратную связь по току
            Rk = Rke - Re  # сопротивление в коллекторной цепи
            UR2 = Ube0 + URe  # фиксированное падение напряжение на базе транзистора
            I1 = 10 * Ib0  # ток в ветви делителя напряжений, протекающий через сопротивление R1
            I2 = I1-Ib0  # ток в ветви делителя напряжений, протекающий через сопротивление R2
            R2 = UR2 / I2  # сопротивление резистора R2 делителя напряжения
            R1 = (Ek - UR2) / I1  # сопротивление резистора R1 делителя напряжения
            h11 = Ube0 / Ib0  # собственное входное сопротивление транзистора по постоянному току
            h22 = Uke0 / Ik0  # собственное выходное сопротивление транзистора по постоянному току
            # емкость разделительных конденсаторов и конденсатора в цепи эмиттера
            Cr = 1 / (2 * 3.14 * f)
            Ce = 3 / (2 * 3.14 * f)

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
    def __init__(self, r_value: float, label_name: str):
        self.resistance_value = r_value
        self.label_name = label_name



def main():
    if __name__ == "__main__":
        application = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(application.exec_())


if __name__ == '__main__':
    main()
