#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from main_ui import Ui_MainWindow
import si_prefix
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import numpy as np


class Main_Window(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.c0_generator = Generator()
        self.c1_Rg = Resistor()
        self.c2_R1 = Resistor()
        self.c3_R2 = Resistor()
        self.c4_Rk = Resistor()
        self.c5_Re = Resistor()
        self.c6_R5 = Resistor()
        self.c7_Ce = Capacitor()
        self.c8_Cr = Capacitor()
        self.c9_Cb = Capacitor()
        self.c10_VEk = Battery()

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
        self.pushButton_Cr1.clicked.connect(self.open_dialog)
        self.pushButton_Cr2.clicked.connect(self.open_dialog)
        self.pushButton_Ce.clicked.connect(self.open_dialog)
        self.pushButton_Cb.clicked.connect(self.open_dialog)
        self.pushButton_VEk.clicked.connect(self.open_dialog)
        self.pushButton_oscilloscope.clicked.connect(self.open_dialog)

        self.update_labels()

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
        elif sender == 'pushButton_Ce':
            self.c7_Ce.exec_()
        elif sender == 'pushButton_Cr1' or sender == 'pushButton_Cr2':
            self.c8_Cr.exec_()
        elif sender == 'pushButton_Cb':
            self.c9_Cb.exec_()
        elif sender == 'pushButton_VEk':
            self.c10_VEk.exec_()
        elif sender == 'pushButton_oscilloscope':
            osci = Oscilloscope()
            osci.set_params(self.culc())
            osci.exec_()

        self.update_labels()
        self.culc()

    def culc(self):
        Ube0 = self.input_Ube0.text().replace(',', '.')
        Ib0 = self.input_Ib0.text().replace(',', '.')
        Uke0 = self.input_Uke0.text().replace(',', '.')
        Ik0 = self.input_Ik0.text().replace(',', '.')
        Ek = self.c10_VEk.voltage.replace(',', '.')
        H11 = self.input_H11.text().replace(',', '.')
        B = self.input_B.text().replace(',', '.')
        if Ube0 and Ib0 and Uke0 and Ik0 and Ek and H11 and B:
            Ube0 = convert_si_to_num(Ube0)
            Ib0 = convert_si_to_num(Ib0)
            Uke0 = convert_si_to_num(Uke0)
            Ik0 = convert_si_to_num(Ik0)
            Ek = convert_si_to_num(Ek)
            H11 = convert_si_to_num(H11)
            B = convert_si_to_num(B)

            Rke: float = (Ek - Uke0) / Ik0  # сопротивление цепи эмиттер-коллектор
            Ikn: float = Ek / Rke  # постоянный коллекторный ток насыщения транзистора
            Ie0: float = Ik0 + Ib0  # постоянный эмиттерный ток в режиме покоя транзистора
            URe: float = 0.01 * Ek  # падение напряжения на сопротивлении эмиттера
            Re: float = URe / Ie0  # сопротивление в цепи эмиттера, обеспечивающее отрицательную обратную связь по току
            self.c5_Re.update_resistor_values(Re)
            Rk: float = Rke - Re  # сопротивление в коллекторной цепи
            self.c4_Rk.update_resistor_values(Rk)
            UR2: float = Ube0 + URe  # фиксированное падение напряжение на базе транзистора
            I1: float = 10 * Ib0  # ток в ветви делителя напряжений, протекающий через сопротивление R1
            I2: float = I1-Ib0  # ток в ветви делителя напряжений, протекающий через сопротивление R2
            R2: float = UR2 / I2  # сопротивление резистора R2 делителя напряжения
            self.c3_R2.update_resistor_values(R2)
            R1: float = (Ek - UR2) / I1  # сопротивление резистора R1 делителя напряжения
            self.c2_R1.update_resistor_values(R1)
            h11: float = Ube0 / Ib0  # собственное входное сопротивление транзистора по постоянному току
            h22: float = Uke0 / Ik0  # собственное выходное сопротивление транзистора по постоянному току
            # емкость разделительных конденсаторов и конденсатора в цепи эмиттера
            f: float = convert_si_to_num(self.c0_generator.frequency)
            Cr: float = 1 / (2 * 3.14 * f)
            self.c8_Cr.update_capacitance_values(Cr)
            Ce: float = 3 / (2 * 3.14 * f)
            self.c7_Ce.update_capacitance_values(Ce)
            Rb: float = (R1 * R2) / (R1 + R2)
            Rvx: float = (Rb * H11) / (Rb + H11)
            E: float = convert_si_to_num(self.c10_VEk.voltage)
            Rg: float = convert_si_to_num(self.c1_Rg.resistive_value)
            Ivx: float = E / (Rg + Rvx)
            Uvx: float = Ivx * Rvx
            Ib: float = Uvx / H11
            Ik: float = Ib * B
            Rn: float = convert_si_to_num(self.c5_Re.resistive_value)
            Rvux: float = (Rk * Rn) / (Rk + Rn)
            Uke: float = Ik * Rvux
            Ivux: float = Uke / Rk
            In: float = Uke / Rn

            Un: float = Ik * Rvux # Выходное напрядение после усиления
            Ku: float = Un / Uvx  #
            Ke: float = Un / E  # Eg - в генераторе напряжение
            Ki: float = In / Ivx
            Kp: float = Ki * Ku

            self.update_labels()

            return {'Un': Un,
                    'Ku': Ku,
                    'Ke': Ke,
                    'Ki': Ki,
                    'Kp': Kp,
                    'generator_a': convert_si_to_num(self.c0_generator.amplitude),
                    'generator_f': convert_si_to_num(self.c0_generator.frequency),
                    }

    def update_labels(self):
        self.label_Rg.setText(self.c1_Rg.get_resistor_label())
        self.label_R1.setText(self.c2_R1.get_resistor_label())
        self.label_R2.setText(self.c3_R2.get_resistor_label())
        self.label_Rk.setText(self.c4_Rk.get_resistor_label())
        self.label_Re.setText(self.c5_Re.get_resistor_label())
        self.label_R5.setText(self.c6_R5.get_resistor_label())
        self.label_Ce.setText(self.c7_Ce.get_capacitance_label())
        self.label_Cr1.setText(self.c8_Cr.get_capacitance_label())
        self.label_Cr2.setText(self.c8_Cr.get_capacitance_label())
        self.label_Cb.setText(self.c9_Cb.get_capacitance_label())
        self.label_VEk.setText(self.c10_VEk.get_battery_label())


class Resistor(QDialog):
    def __init__(self, parent=None):
        super(Resistor, self).__init__(parent)
        self.resistive_value = '1 k'

        self.setWindowTitle('Резистор')
        self.resistor_v_layout = QVBoxLayout()
        self.resistor_dialog_label = QLabel('Сопротивление')
        self.resistor_dialog_input = QLineEdit(self.resistive_value)
        self.resistor_dialog_pushbutton = QPushButton(text='Внести')
        self.resistor_v_layout.addWidget(self.resistor_dialog_label)
        self.resistor_v_layout.addWidget(self.resistor_dialog_input)
        self.resistor_v_layout.addWidget(self.resistor_dialog_pushbutton)
        self.setLayout(self.resistor_v_layout)

        self.resistor_dialog_pushbutton.clicked.connect(self.update_resistor_values)

    def update_resistor_values(self, raw_value: float):
        if raw_value is not False:
            self.resistive_value = set_proper_value(raw_value)
        else:
            self.resistive_value = self.resistor_dialog_input.text()
            self.close()

    def get_resistor_label(self) -> str:
        return f'{self.resistive_value}Ом'


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


class Capacitor(QDialog):
    def __init__(self, parent=None):
        super(Capacitor, self).__init__(parent)
        self.capacitance = '1'
        self.label_name = "Конденсатор"

        self.setWindowTitle(f'{self.label_name}')
        self.capacitor_v_layout = QVBoxLayout()
        self.capacitor_label_capacity = QLabel('Емкость')
        self.capacitor_input_capacity = QLineEdit(self.capacitance)
        self.capacitor_push_button = QPushButton('Внести')
        self.capacitor_v_layout.addWidget(self.capacitor_label_capacity)
        self.capacitor_v_layout.addWidget(self.capacitor_input_capacity)
        self.capacitor_v_layout.addWidget(self.capacitor_push_button)
        self.setLayout(self.capacitor_v_layout)

        self.capacitor_push_button.clicked.connect(self.update_capacitance_values)

    def update_capacitance_values(self, raw_value: float):
        if raw_value is not False:
            self.capacitance = set_proper_value(raw_value)
        else:
            self.capacitance = self.capacitor_input_capacity.text()
            self.close()

    def get_capacitance_label(self):
        return f'{self.capacitance}Ф'


class Battery(QDialog):
    def __init__(self, parent=None):
        super(Battery, self).__init__(parent)
        self.voltage = '12'
        self.label_name = 'Батарейка'

        self.setWindowTitle(f'{self.label_name}')
        self.battery_v_layout = QVBoxLayout()
        self.battery_label_voltage = QLabel('Напряжение')
        self.battery_input_voltage = QLineEdit(self.voltage)
        self.battery_push_button = QPushButton('Внести')
        self.battery_v_layout.addWidget(self.battery_label_voltage)
        self.battery_v_layout.addWidget(self.battery_input_voltage)
        self.battery_v_layout.addWidget(self.battery_push_button)
        self.setLayout(self.battery_v_layout)

        self.battery_push_button.clicked.connect(self.update_voltage_values)

    def update_voltage_values(self):
        self.voltage = self.battery_input_voltage.text()
        self.close()

    def get_battery_label(self):
        return f'{self.voltage}В'


class Oscilloscope(QDialog):
    def __init__(self, parent=None):
        super(Oscilloscope, self).__init__(parent)
        self.setWindowTitle('Осцилограф')
        self.setMinimumSize(300, 300)

        self.params = None

        self.label_time_base = QLabel('Time base')
        self.combo_time_base = QComboBox()
        self.spin_time_base = QDoubleSpinBox()

        self.label_channel_a = QLabel('Channel A')
        self.combo_channel_a = QComboBox()
        self.spin_channel_a = QDoubleSpinBox()

        self.label_channel_b = QLabel('Channel B')
        self.combo_channel_b = QComboBox()
        self.spin_channel_b = QDoubleSpinBox()

        self.button = QPushButton("Построить")
        self.button.clicked.connect(self.plot)

        self.layout_osci = QVBoxLayout()

        self.init_DUI()

    def init_DUI(self):
        self.layout_osci.addWidget(self.label_time_base)
        self.layout_osci.addWidget(self.combo_time_base)
        self.layout_osci.addWidget(self.spin_time_base)
        self.layout_osci.addWidget(self.label_channel_a)
        self.layout_osci.addWidget(self.combo_channel_a)
        self.layout_osci.addWidget(self.spin_channel_a)
        self.layout_osci.addWidget(self.label_channel_b)
        self.layout_osci.addWidget(self.combo_channel_b)
        self.layout_osci.addWidget(self.spin_channel_b)
        self.layout_osci.addWidget(self.button)
        self.setLayout(self.layout_osci)

        self.spin_time_base.setRange(-5, 5)
        self.spin_time_base.setSingleStep(0.1)
        self.spin_time_base.setSuffix(' - y position')
        self.spin_time_base.valueChanged.connect(self.plot)

        self.spin_channel_a.setRange(-5, 5)
        self.spin_channel_a.setSingleStep(0.2)
        self.spin_channel_a.setSuffix(' - y position')
        self.spin_channel_a.valueChanged.connect(self.plot)

        self.spin_channel_b.setRange(-5, 5)
        self.spin_channel_b.setSingleStep(0.2)
        self.spin_channel_b.setSuffix(' - y position')
        self.spin_channel_b.valueChanged.connect(self.plot)

        self.combo_time_base.addItems(list_for_combobox('time_base'))
        self.combo_time_base.currentTextChanged.connect(self.plot)

        self.combo_channel_a.addItems(list_for_combobox('chanal'))
        self.combo_channel_a.currentTextChanged.connect(self.plot)
        self.combo_channel_a.setCurrentText('1 V/div')

        self.combo_channel_b.addItems(list_for_combobox('chanal'))
        self.combo_channel_b.currentTextChanged.connect(self.plot)
        self.combo_channel_b.setCurrentText('1 V/div')

    def set_params(self, params):
        self.params = params

    def plot(self):
        plt.close()
        osci_multiplaer_a = convert_si_to_num(self.combo_channel_a.currentText())
        osci_multiplaer_b = convert_si_to_num(self.combo_channel_b.currentText())
        offset_by_y_in_osci = self.spin_channel_a.value()
        offset_by_y2_in_osci = self.spin_channel_b.value()
        x = np.linspace(0, 1000, 100)
        y = (self.params.get('generator_a') * np.sin(2 * np.pi * self.params.get('generator_f') * x)) \
            * osci_multiplaer_a + offset_by_y_in_osci
        y2 = (self.params.get('Un') * np.sin(2 * np.pi * self.params.get('generator_f') * x)) \
            * osci_multiplaer_b + offset_by_y2_in_osci
        fig, ax = plt.subplots()
        ax.plot(x, y, label='Генератор')
        ax.plot(x, y2, label='Услининый сигнал')
        ax.legend()
        plt.xlabel('Время, t')
        plt.ylabel('Напряжение, U')
        plt.title('Осцилограф')
        plt.grid(True)
        plt.show()


def list_for_combobox(type_of_list: str) -> list:
    if type_of_list == 'chanal':
        type_of_number = ('500', '200', '100', '50', '20', '10', '5', '2', '1')
        type_of_suffix = (' kV/div', ' V/div', ' mV/div', ' uV/div')
        result = []
        for item in type_of_suffix:
            for number in type_of_number:
                result.append(number + item)
        return result
    elif type_of_list == 'time_base':
        type_of_number = ('5.00', '2.00', '1.00', '0.5', '0.2', '0.1', '0.05', '0.02', '0.01')
        type_of_suffix = (' s/div', ' ms/div', ' us/div', ' ns/div',)
        result = []
        for item in type_of_suffix:
            for number in type_of_number:
                result.append(number + item)
        return result


def convert_si_to_num(input_string: str) -> float:
    params_dict_ru = {'p': -12,
                      'n': -9,
                      'u': -6,
                      'm': -3,
                      's': -2,
                      'd': -1,
                      'da': 1,
                      'h': 2,
                      'k': 3,
                      'M': 6,
                      'G': 9,
                      'T': 12,
                      '': 0
                      }
    try:
        num, postfix = input_string.split(' ')
        if postfix in params_dict_ru:
            params_postfix = params_dict_ru.get(postfix)
            result = float(num) * pow(10, params_postfix)
            return result
        elif 's/div' in postfix or 'V/div' in postfix:
            postfix = postfix[:-5]
            if postfix in params_dict_ru:
                params_postfix = params_dict_ru.get(postfix)
                result = float(num) * pow(10, params_postfix)
                return result
            else:
                return float(num)
        else:
            return float(num)
    except ValueError:
        return float(input_string)


def convert_num_to_si(input_num: float) -> str:
    params_dict_ru = {'p': -12,
                      'n': -9,
                      'u': -6,
                      'm': -3,
                      's': -2,
                      'd': -1,
                      'da': 1,
                      'h': 2,
                      'k': 3,
                      'M': 6,
                      'G': 9,
                      'T': 12,
                      '': 0
                      }
    num_and_extent = si_prefix.split(input_num)
    for key, value in params_dict_ru.items():
        if value == num_and_extent[1]:
            result = f'{round(num_and_extent[0], 1)} {key}'
            return result


def convert_si_to_proper_from(string_to_convert: str) -> str:
    try:
        num, postfix = string_to_convert.split(' ')
        num = round(float(num), 1)
        return _check(num, postfix)

    except AttributeError:
        num = string_to_convert
        num = round(float(num), 1)
        postfix = ''
        return _check(num, postfix)


def _check(num, postfix):
    e24 = (1.0, 1.1, 1.2,
           1.3, 1.5, 1.6,
           1.8, 2.0, 2.2,
           2.4, 2.7, 3.0,
           3.3, 3.6, 3.9,
           4.3, 4.7, 5.1,
           5.6, 6.2, 6.8,
           7.5, 8.1, 9.1)
    if num < 10:
        if num not in e24:
            for item in e24:
                if item > num:
                    num = item
                    return f'{num} {postfix}'
        else:
            return f'{round(num, 1)} {postfix}'
    elif 10 <= num < 100:
        num_for_check = round(num / 10, 1)
        if num_for_check not in e24:
            for item in e24:
                if item > num_for_check:
                    num = item
                    return f'{round(num * 10, 1)} {postfix}'
        else:
            return f'{round(num_for_check * 10)} {postfix}'
    elif num >= 100:
        num_for_check = round(num / 100, 1)
        if num_for_check not in e24:
            for item in e24:
                if item > num_for_check:
                    num = item
                    return f'{round(num * 100, 1)} {postfix}'
        else:
            return f'{round(num_for_check * 100, 1)} {postfix}'


def set_proper_value(value_to_correct: float) -> str:
    value_in_si_form = convert_num_to_si(value_to_correct)
    result = convert_si_to_proper_from(value_in_si_form)
    return result


def main():
    application = QApplication(sys.argv)
    window = Main_Window()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
