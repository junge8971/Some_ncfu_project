#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide2 import QtWidgets
from PySide2.QtWidgets import *
from main_ui import Ui_MainWindow
import si_prefix
import matplotlib.pyplot as plt
import numpy as np




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
            self.label_k_output.setText(f'Ku = {convert_num_to_si(Ku)}\nKe = {convert_num_to_si(Ke)}\n'
                                        f'Ki = {convert_num_to_si(Ki)}\nKp = {convert_num_to_si(Kp)}')

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
        if self.resistive_value.isdigit():
            return f'{self.resistive_value} Ом'
        else:
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
        if self.capacitance.isdigit():
            return f'{self.capacitance} Ф'
        else:
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
        if self.voltage.isdigit():
            return f'{self.voltage} В'
        else:
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
        # self.layout_osci.addWidget(self.label_time_base)
        # self.layout_osci.addWidget(self.combo_time_base)
        # self.layout_osci.addWidget(self.spin_time_base)
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
        ax.plot(x, y, label='Channel A')
        ax.plot(x, y2, label='Channel B')
        ax.legend(loc='lower right')
        plt.xlabel('Время, t')
        plt.ylabel('Напряжение, U')
        plt.title('Осцилограф')
        plt.grid(True)
        plt.yticks(range(-10, 11, 1))
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
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
        font1 = QFont()
        font1.setPointSize(10)
        self.label_Rg.setFont(font1)
        self.label_Rg.setAlignment(Qt.AlignCenter)
        self.label_Cr1 = QLabel(self.centralwidget)
        self.label_Cr1.setObjectName(u"label_Cr1")
        self.label_Cr1.setGeometry(QRect(330, 390, 91, 16))
        self.label_Cr1.setFont(font1)
        self.label_Cr1.setAlignment(Qt.AlignCenter)
        self.label_R2 = QLabel(self.centralwidget)
        self.label_R2.setObjectName(u"label_R2")
        self.label_R2.setGeometry(QRect(520, 520, 111, 16))
        self.label_R2.setFont(font1)
        self.label_Ce = QLabel(self.centralwidget)
        self.label_Ce.setObjectName(u"label_Ce")
        self.label_Ce.setGeometry(QRect(710, 590, 101, 16))
        self.label_Ce.setFont(font1)
        self.label_Re = QLabel(self.centralwidget)
        self.label_Re.setObjectName(u"label_Re")
        self.label_Re.setGeometry(QRect(830, 600, 101, 16))
        self.label_Re.setFont(font1)
        self.label_R5 = QLabel(self.centralwidget)
        self.label_R5.setObjectName(u"label_R5")
        self.label_R5.setGeometry(QRect(1070, 480, 81, 16))
        self.label_R5.setFont(font1)
        self.label_Cr2 = QLabel(self.centralwidget)
        self.label_Cr2.setObjectName(u"label_Cr2")
        self.label_Cr2.setGeometry(QRect(940, 340, 101, 16))
        self.label_Cr2.setFont(font1)
        self.label_Cr2.setAlignment(Qt.AlignCenter)
        self.label_Rk = QLabel(self.centralwidget)
        self.label_Rk.setObjectName(u"label_Rk")
        self.label_Rk.setGeometry(QRect(830, 300, 71, 16))
        self.label_Rk.setFont(font1)
        self.label_Cb = QLabel(self.centralwidget)
        self.label_Cb.setObjectName(u"label_Cb")
        self.label_Cb.setGeometry(QRect(930, 210, 111, 20))
        self.label_Cb.setFont(font1)
        self.label_Cb.setAlignment(Qt.AlignCenter)
        self.label_VEk = QLabel(self.centralwidget)
        self.label_VEk.setObjectName(u"label_VEk")
        self.label_VEk.setGeometry(QRect(900, 110, 131, 20))
        self.label_VEk.setFont(font1)
        self.label_VEk.setAlignment(Qt.AlignCenter)
        self.label_R1 = QLabel(self.centralwidget)
        self.label_R1.setObjectName(u"label_R1")
        self.label_R1.setGeometry(QRect(520, 290, 101, 20))
        self.label_R1.setFont(font1)
        self.label_k_output = QLabel(self.centralwidget)
        self.label_k_output.setObjectName(u"label_k_output")
        self.label_k_output.setGeometry(QRect(194, 25, 181, 91))
        self.label_k_output.setFont(font1)
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
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_input_Ube0.setText(QCoreApplication.translate("MainWindow", u"U\u0411\u042d0, \u0412", None))
        self.label_input_Ib0.setText(QCoreApplication.translate("MainWindow", u"I\u04110, \u0410", None))
        self.label_input_Uke0.setText(QCoreApplication.translate("MainWindow", u"U\u041a\u042d0, \u0412", None))
        self.label_input_Ik0.setText(QCoreApplication.translate("MainWindow", u"I\u041a0, \u0410", None))
        self.label_input_B.setText(QCoreApplication.translate("MainWindow", u"\u03b2", None))
        self.label_input_H11.setText(QCoreApplication.translate("MainWindow", u"h11, \u043f\u0435\u0440\u0435\u043c", None))
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
        self.label_R1.setText("")
        self.label_k_output.setText("")
    # retranslateUi


def main():
    application = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
