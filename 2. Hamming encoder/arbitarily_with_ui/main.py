#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
from typing import List
from PySide2.QtWidgets import *
from PySide2.QtCore import QObject
from maim_ui import Ui_MainWindow


class Hemming:
    def __init__(self):
        self.user_message_len = None
        self.number_of_check_bits = None
        self.message = None
        self.check_indices = None
        self.check_bits = None
        self.generating_matrix = None
        self.encoded_message = None
        self.modified_message = None
        self.binary_syndrome = None
        self.error_pos = None
        self.decoded_message = None

    def hamming_encode(self):
        """
        Encode a binary message using a Hemming code.
        """
        # Calculate number of check bits based on message length
        self.number_of_check_bits = int(np.ceil(np.log2(self.user_message_len + 1)))
        # Find powers of two in message length -1 to get coordinates of check bits
        self.check_indices = np.array([2 ** i - 1 for i in range(self.number_of_check_bits)])

        # Create a np.ndarray consisting of 0 corresponding to the length of the message + the number of check bits
        encoded = np.zeros(self.user_message_len + self.number_of_check_bits, dtype=int)

        # Fill in the information bits in encode list
        counter = 0
        for item_id, _ in enumerate(encoded):
            if item_id not in self.check_indices:
                encoded[item_id] = self.message[counter]
                counter += 1
        # Create a generating matrix
        self._create_generating_matrix()

        # From the generating matrix and the encoded array, calculate the value of the check bits
        self.check_bits = self._calculate_syndrome(encoded)

        # Insert parity bits into their addresses
        for check_bit_id, element in enumerate(self.check_indices):
            encoded[element] = self.check_bits[check_bit_id]

        self.encoded_message = encoded

    def hamming_decode(self):
        """
        Decode a Hemming-encoded message.
        """
        if self.encoded_message:
            # Calculate error position and correct errors if possible.
            self.binary_syndrome = self._calculate_syndrome(self.encoded_message)
            error_pos = 0
            for num, item in enumerate(self.binary_syndrome):
                error_pos += item * (self.check_indices[num] + 1)
            if error_pos > 0:
                self.encoded_message[error_pos - 1] ^= 1

            # Extract original message bits.
            decoded_msg = np.delete(self.encoded_message, self.check_indices)
            self.decoded_message = decoded_msg
            self.error_pos = error_pos - 1

    def _create_generating_matrix(self):
        """
            Creates a matrix for calculating check bits and syndromes based on:
            message length,
            number of check bits,
            check bits addresses
            Only for use inside the model!
        """
        if self.user_message_len and self.number_of_check_bits and self.check_indices is not None:
            generating_matrix = []
            for item in self.check_indices + 1:
                counter = 0
                status = False
                list_of_elements_for_matrix = []
                for _ in range(self.user_message_len + self.number_of_check_bits + 1):
                    if counter != item:
                        if status:
                            list_of_elements_for_matrix.append(1)
                        else:
                            list_of_elements_for_matrix.append(0)
                        counter += 1
                    elif counter == item:
                        status = not status
                        counter = 0
                        if status:
                            list_of_elements_for_matrix.append(1)
                        else:
                            list_of_elements_for_matrix.append(0)
                        counter += 1

                generating_matrix.append(list_of_elements_for_matrix[1:])
            self.generating_matrix = np.array(generating_matrix)

    def _calculate_syndrome(self, message: np.ndarray) -> List[int]:
        """
            Calculates the syndrome or the value of the check bits
            Only for use inside the model!

            Args:
                message: numpy array that contain message for calculate

            Returns:
                A list containing integers whose value represents the check bits / binary syndrome .
        """
        if self.number_of_check_bits is not None and message is not False:
            result = []
            for num in range(self.number_of_check_bits):
                result.append(np.sum(message * self.generating_matrix[num]) % 2)

            return result

    def set_value_user_message_len(self, user_message_len: int):
        if user_message_len:
            self.user_message_len = user_message_len

    def get_value_user_message_len(self) -> int:
        if self.user_message_len:
            return self.user_message_len
        else:
            raise ValueError('Длинна сообщения не определенна')

    def get_number_of_check_bits(self) -> int:
        if self.number_of_check_bits:
            return self.number_of_check_bits
        else:
            return int(np.ceil(np.log2(self.user_message_len + 1)))

    def generate_message(self):
        if self.user_message_len:
            self.message = np.random.randint(2, size=self.user_message_len)
        else:
            raise ValueError('Длинна информационного блока не указана')

    def get_message(self) -> str:
        if self.message is not None:
            return np.array2string(self.message, separator='')[1:-1]
        else:
            raise ValueError('Сообщение не ввидено/сгенериновано')

    def set_message(self, input_message: str):
        if input_message:
            message_list = [int(i) for i in input_message]
            self.message = np.array(message_list)
        else:
            raise ValueError('Передаваемое сообщение пустое')

    def get_check_indices(self) -> str:
        return np.array2string(self.check_indices, separator=' ')[1:-1]

    def get_encoded_message(self) -> str:
        return np.array2string(self.encoded_message, separator='')[1:-1]

    def get_generating_matrix(self) -> list:
        result_generating_matrix = []
        for item in self.generating_matrix:
            result_generating_matrix.append(np.array2string(item, separator='')[1:-1])
        return result_generating_matrix


class HemmingView(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кодирование и декодирование блочным кодом Хэмминга")
        self.setupUi(self)
        self.show()

    def get_message_len_value(self) -> int:
        """
        Gets the value from the message length input field and returns it in integer format
        :return: message_len_value: int
        """
        try:
            message_len_value = int(self.message_len.text())
            return message_len_value
        except ValueError:
            raise ValueError('Нужно ввести целое число')

    def set_message_len_value_to_label(self, message_len_value: int):
        if message_len_value:
            self.label_message_len.setText(f'Длинна сообщения: {message_len_value}')

    def connect_message_len_button(self, callback):
        self.message_len_button.clicked.connect(callback)

    def set_label_number_of_check_bit(self, number_of_check_bit: int):
        if number_of_check_bit:
            self.label_number_of_check_bit.setText(f'Количество проверочных бит: {number_of_check_bit}')

    def set_label_coder_type(self, message_len, number_of_check_bits):
        if message_len and number_of_check_bits:
            self.label_coder_type.setText(f'Тип  блочного кода Хэмминга:'
                                          f' {message_len + number_of_check_bits},{message_len}')

    def connect_generate_message_button(self, callback):
        self.generate_message.clicked.connect(callback)

    def set_input_message_value(self, message: str):
        self.input_message.setText(message)

    def connect_encode_button(self, callback):
        self.encode_message.clicked.connect(callback)

    def get_input_message_value(self) -> str:
        if self.input_message.toPlainText():
            return self.input_message.toPlainText()
        else:
            raise ValueError('В поле с сообщением пусто')

    def set_label_check_indices(self, check_indices: str):
        self.label_check_indices.setText(f'Координаты проверочных бит: {check_indices}')

    def set_label_input_data(self, input_data: str):
        self.label_input_data.setText(f'Исходный информационный блок: \n {input_data}')

    def set_label_encoded(self, encoded_message: str, check_indices: str):
        start_string = '<html><body>'
        end_sting = '</body></html>'
        open_colored_teg = '<span style="color:#32CD32;">'
        close_colored_teg = '</span>'
        check_indices = check_indices.split(' ')
        check_indices_for_iterations = []
        for item in check_indices:
            try:
                check_indices_for_iterations.append(int(item))
            except ValueError:
                continue
        message_with_color = ''
        for id, item in enumerate(encoded_message):
            if id in check_indices_for_iterations:
                message_with_color += (open_colored_teg + item + close_colored_teg)
            else:
                message_with_color += item
        self.label_encoded.setText('{0}Закодированный информационный блок: \n {1}{2}'.format(
            start_string, end_sting, message_with_color)
        )

    def set_label_matrix(self, generating_matrix: list):
        matrix = ''
        for item in generating_matrix:
            matrix += item + '\n'
        self.label_matrix.setText(matrix)


class HemmingController(QObject):
    def __init__(self, model, view):
        super().__init__()
        self._model = model
        self._view = view

        self._view.connect_message_len_button(self.handle_message_len_button_click)
        self._view.connect_generate_message_button(self.handle_generate_message_button_click)
        self._view.connect_encode_button(self.handle_encode_button_click)

    def handle_message_len_button_click(self):
        message_len = self._view.get_message_len_value()
        self._view.set_message_len_value_to_label(message_len)
        self._model.set_value_user_message_len(message_len)

        number_of_check_bits = self._model.get_number_of_check_bits()
        self._view.set_label_number_of_check_bit(number_of_check_bits)

        self._view.set_label_coder_type(message_len, number_of_check_bits)

    def handle_generate_message_button_click(self):
        self._model.generate_message()
        message = self._model.get_message()
        self._view.set_input_message_value(message)

    def handle_encode_button_click(self):
        message_for_encode = self._view.get_input_message_value()
        message_len_that_was_user_input = self._model.get_value_user_message_len()
        if len(message_for_encode) != message_len_that_was_user_input:
            raise ValueError("Введённая длина сообщения и длинна введённого сообщения не равны")
        else:
            self._model.set_message(message_for_encode)
            self._model.hamming_encode()
            check_indices = self._model.get_check_indices()
            self._view.set_label_check_indices(check_indices)
            message_for_view = self._model.get_message()
            self._view.set_label_input_data(message_for_view)
            encoded_message = self._model.get_encoded_message()
            self._view.set_label_encoded(encoded_message, check_indices)
            get_generating_matrix = self._model.get_generating_matrix()
            self._view.set_label_matrix(get_generating_matrix)


def main():
    # Create the main application instance
    application = QApplication(sys.argv)
    # Create the model instance
    model = Hemming()

    # Create the view instance
    view = HemmingView()

    # Create the controller instance
    controller = HemmingController(model, view)

    sys.exit(application.exec_())


if __name__ == '__main__':
    main()
