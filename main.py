#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from PySide2.QtGui import QPixmap
from main_ui import Ui_MainWindow
import si_prefix


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.c0_generator = Generator()
        self.c1_Rg = Resistor()
        self.c2_R1 = Resistor()
        self.c3_R2 = Resistor()
        self.c4_Rk = Resistor()
        self.c5_Re = Resistor()
        self.c6_R5 = Resistor()

        self.setWindowTitle("Контрольная работа")
        self.setupUi(self)
        self.show()
        self.button_calculate.clicked.connect(self.open_dialog)
        self.pushButton_Rg.clicked.connect(self.open_dialog)
        self.pushButton_R1.clicked.connect(self.open_dialog)
        self.pushButton_R2.clicked.connect(self.open_dialog)
        self.pushButton_Rk.clicked.connect(self.open_dialog)
        self.pushButton_Re.clicked.connect(self.open_dialog)
        self.pushButton_R5.clicked.connect(self.open_dialog)
        self.pushButton_generator.clicked.connect(self.open_dialog)


    def open_dialog(self):
        sender = self.sender().objectName()
        if sender == 'pushButton_generator':
            self.c0_generator.exec_()
        elif sender == 'pushButton_Rg':
            self.c1_Rg.exec_()
        elif sender == 'pushButton_R1':
            self.c2_R1.exec_()
        elif sender == 'pushButton_R2':
            self.c3_R2.exec_()
        elif sender == 'pushButton_Rk':
            self.c4_Rk.exec_()
        elif sender == 'pushButton_Re':
            self.c5_Re.exec_()
        elif sender == 'pushButton_R5':
            self.c6_R5.exec_()
        elif sender == 'button_calculate':
            self.culc()

    def culc(self):
        Ube0 = self.input_Ube0.text()
        Ib0 = self.input_Ib0.text()
        Uke0 = self.input_Uke0.text()
        Ik0 = self.input_Ik0.text()
        Ek = self.input_Ek.text()
        if Ube0 and Ib0 and Uke0 and Ik0 and Ek:
            Ube0 = convert_si_to_num(Ube0)
            Ib0 = convert_si_to_num(Ib0)
            Uke0 = convert_si_to_num(Uke0)
            Ik0 = convert_si_to_num(Ik0)
            Ek = convert_si_to_num(Ek)

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
            f = convert_si_to_num(self.c0_generator.frequency)
            Cr = 1 / (2 * 3.14 * f)
            print(Cr)
            Ce = 3 / (2 * 3.14 * f)


class Resistor(QDialog):
    def __init__(self, parent=None):
        super(Resistor, self).__init__(parent)
        self.resistive_value = '1 K'
        self.label_name = None

        self.setWindowTitle(f'{self.label_name}')
        self.resistor_v_layout = QVBoxLayout()
        self.resistor_dialog_label = QLabel('Сопротивление')
        self.resistor_dialog_input = QLineEdit(self.resistive_value)
        self.resistor_dialog_pushbutton = QPushButton(text='Внести')
        self.resistor_v_layout.addWidget(self.resistor_dialog_label)
        self.resistor_v_layout.addWidget(self.resistor_dialog_input)
        self.resistor_v_layout.addWidget(self.resistor_dialog_pushbutton)
        self.setLayout(self.resistor_v_layout)

        self.resistor_dialog_pushbutton.clicked.connect(self.update_resistor_values)

    def update_resistor_values(self):
        self.resistive_value = self.resistor_dialog_input.text()
        self.close()


class Generator(QDialog):
    def __init__(self, parent=None):
        super(Generator, self).__init__(parent)
        self.frequency = '1'
        self.duty_cycle = '50'
        self.amplitude = '10'
        self.offset = '0'
        self.label_name = "Генератор"

        self.setWindowTitle(f'{self.label_name}')
        self.generator_v_layout = QVBoxLayout()
        self.generator_label_frequency = QLabel('Частота')
        self.generator_input_frequency = QLineEdit(self.frequency)
        self.generator_label_duty_cycle = QLabel('Скважность %')
        self.generator_input_duty_cycle = QLineEdit(self.duty_cycle)
        self.generator_label_amplitude = QLabel('Амплитуда')
        self.generator_input_amplitude = QLineEdit(self.amplitude)
        self.generator_label_offset = QLabel('Постоянная составляющая')
        self.generator_input_offset = QLineEdit(self.offset)
        self.generator_push_button = QPushButton('Внести')
        self.generator_v_layout.addWidget(self.generator_label_frequency)
        self.generator_v_layout.addWidget(self.generator_input_frequency)
        self.generator_v_layout.addWidget(self.generator_label_duty_cycle)
        self.generator_v_layout.addWidget(self.generator_input_duty_cycle)
        self.generator_v_layout.addWidget(self.generator_label_amplitude)
        self.generator_v_layout.addWidget(self.generator_input_amplitude)
        self.generator_v_layout.addWidget(self.generator_label_offset)
        self.generator_v_layout.addWidget(self.generator_input_offset)
        self.generator_v_layout.addWidget(self.generator_push_button)
        self.setLayout(self.generator_v_layout)

        self.generator_push_button.clicked.connect(self.update_generator_values)

    def update_generator_values(self):
        self.frequency = self.generator_input_frequency.text()
        self.duty_cycle = self.generator_input_duty_cycle.text()
        self.amplitude = self.generator_input_amplitude.text()
        self.offset = self.generator_input_offset.text()
        self.close()


def convert_si_to_num(input_string: str) -> float:
    params_dict_ru = {'П': -12,
                      'Н': -9,
                      'мк': -6,
                      'м': -3,
                      'C': -2,
                      'Д': -1,
                      'да': 1,
                      'г': 2,
                      'К': 3,
                      'М': 6,
                      'Г': 9,
                      'Т': 12
                      }
    try:
        num, postfix = input_string.split(' ')
        if postfix in params_dict_ru:
            params_postfix = params_dict_ru.get(postfix)
            result = float(num) * pow(10, params_postfix)
            return result
    except ValueError:
        return float(input_string)


def convert_num_to_si(input_num: float) -> str:
    params_dict_ru = {'П': -12,
                      'Н': -9,
                      'мк': -6,
                      'м': -3,
                      'C': -2,
                      'Д': -1,
                      'да': 1,
                      'г': 2,
                      'К': 3,
                      'М': 6,
                      'Г': 9,
                      'Т': 12
                      }
    num_and_extent = si_prefix.split(input_num)
    for key, value in params_dict_ru.items():
        if value == num_and_extent[1]:
            return f'{num_and_extent[0]} {key}'


def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(application.exec_())


if __name__ == '__main__':


    main()
