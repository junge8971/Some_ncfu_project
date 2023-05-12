#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import sys
from typing import List
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2.QtCore import QObject


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Кодирование и декодирование блочным кодом Хэмминга")
        self.resize(1500, 750)

        self.gridLayout = QGridLayout()
        self.gridLayout.setContentsMargins(10, 0, 0, 0)

        self.modify_and_decod_input = QLineEdit()
        self.modify_and_decod_input.setObjectName(u"modify_and_decod_input")
        self.gridLayout.addWidget(self.modify_and_decod_input, 3, 2, 1, 1)

        self.modify_and_decod_button = QPushButton('Декодировать')
        self.modify_and_decod_button.setObjectName(u"modify_and_decod_button")
        self.gridLayout.addWidget(self.modify_and_decod_button, 4, 2, 1, 1)

        self.label_message_len = QLabel('Длинна информационного блока:')
        self.label_message_len.setObjectName(u"label_message_len")
        font = QFont()
        font.setPointSize(10)
        self.label_message_len.setFont(font)
        self.label_message_len.setWordWrap(True)
        self.gridLayout.addWidget(self.label_message_len, 5, 0, 1, 1)

        self.label_modifaed = QLabel('Модифицированный информационный блок: ')
        self.label_modifaed.setObjectName(u"label_modifaed")
        self.label_modifaed.setFont(font)
        self.label_modifaed.setWordWrap(True)
        self.gridLayout.addWidget(self.label_modifaed, 5, 2, 1, 1)

        self.generate_message = QPushButton('Сгенерировать')
        self.generate_message.setObjectName(u"generate_message")
        self.gridLayout.addWidget(self.generate_message, 3, 1, 1, 1)

        self.encode_message = QPushButton('Закодировать')
        self.encode_message.setObjectName(u"encode_message")
        self.gridLayout.addWidget(self.encode_message, 4, 1, 1, 1)

        self.label_2 = QLabel('Введите в поле или сгенерируйте информационные биты с заданной по варианту длинной и нажмите кнопку закодировать')
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setPointSize(11)
        self.label_2.setFont(font1)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label = QLabel('Введите длинну ифномационного блока')
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setFont(font1)
        self.label.setLineWidth(2)
        self.label.setMidLineWidth(0)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_check_indices = QLabel('Координаты проверочных бит: ')
        self.label_check_indices.setObjectName(u"label_check_indices")
        self.label_check_indices.setFont(font)
        self.label_check_indices.setWordWrap(True)
        self.gridLayout.addWidget(self.label_check_indices, 5, 1, 1, 1)

        self.label_number_of_check_bit = QLabel('Количество проверочных бит: ')
        self.label_number_of_check_bit.setObjectName(u"label_number_of_check_bit")
        self.label_number_of_check_bit.setFont(font)
        self.label_number_of_check_bit.setWordWrap(True)
        self.gridLayout.addWidget(self.label_number_of_check_bit, 6, 0, 1, 1)

        self.label_input_data = QLabel('Исходный информационный блок: ')
        self.label_input_data.setObjectName(u"label_input_data")
        self.label_input_data.setFont(font)
        self.label_input_data.setWordWrap(True)
        self.gridLayout.addWidget(self.label_input_data, 6, 1, 1, 1)


        self.label_binary_syndrome_and_error_pos = QLabel('Синдом и позиция ошибки: ')
        self.label_binary_syndrome_and_error_pos.setObjectName(u"label_binary_syndrome_and_error_pos")
        self.label_binary_syndrome_and_error_pos.setFont(font)
        self.label_binary_syndrome_and_error_pos.setWordWrap(True)
        self.gridLayout.addWidget(self.label_binary_syndrome_and_error_pos, 6, 2, 1, 1)

        self.label_encoded = QLabel('Закодированный информационный блок: ')
        self.label_encoded.setObjectName(u"label_encoded")
        self.label_encoded.setFont(font)
        self.label_encoded.setWordWrap(True)
        self.gridLayout.addWidget(self.label_encoded, 7, 1, 1, 1)

        self.label_3 = QLabel('Лабораторная работа: Иследование кода Хэмминга')
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1)

        self.label_decode = QLabel('Исходный и декодированный информационный блок: ')
        self.label_decode.setObjectName(u"label_decode")
        self.label_decode.setFont(font)
        self.label_decode.setWordWrap(True)
        self.gridLayout.addWidget(self.label_decode, 7, 2, 1, 1)

        self.label_matrix = QLabel()
        self.label_matrix.setObjectName(u"label_matrix")
        self.label_matrix.setFont(font)
        self.label_matrix.setAlignment(Qt.AlignCenter)
        self.gridLayout.addWidget(self.label_matrix, 9, 1, 1, 1)

        self.label_coder_type = QLabel('Тип блочного кода: ')
        self.label_coder_type.setObjectName(u"label_coder_type")
        self.label_coder_type.setFont(font)
        self.label_coder_type.setWordWrap(True)
        self.gridLayout.addWidget(self.label_coder_type, 7, 0, 1, 1)

        self.label_7 = QLabel('Внесите адрес или адреса разрадов для внесения ошибки, либо отсавьте поле пустым и нажмите на кнопку "Декодировать"')
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setAlignment(Qt.AlignCenter)
        self.label_7.setWordWrap(True)
        self.gridLayout.addWidget(self.label_7, 1, 2, 1, 1)

        self.message_len_button = QPushButton('Внести')
        self.message_len_button.setObjectName(u"message_len_button")
        self.gridLayout.addWidget(self.message_len_button, 4, 0, 1, 1)

        self.label_matrix_info = QLabel('Генерирующая матрица:')
        self.label_matrix_info.setObjectName(u"label_matrix_info")
        sizePolicy1.setHeightForWidth(self.label_matrix_info.sizePolicy().hasHeightForWidth())
        self.label_matrix_info.setSizePolicy(sizePolicy1)
        self.label_matrix_info.setFont(font)
        self.gridLayout.addWidget(self.label_matrix_info, 8, 1, 1, 1)

        self.input_message = QLineEdit()
        self.input_message.setObjectName(u"input_message")
        self.gridLayout.addWidget(self.input_message, 2, 1, 1, 1)

        self.message_len = QLineEdit()
        self.message_len.setObjectName(u"message_len")
        self.gridLayout.addWidget(self.message_len, 3, 0, 1, 1)

        self.setLayout(self.gridLayout)


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
        The purpose of this function is to perform the encoding process using a Hamming code.
        It calculates the number of check bits, determines the check bit coordinates, fills in the information bits,
        creates a generating matrix, calculates the check bit values, inserts the check bits into the encoded message,
        and stores the encoded message for further use.
        """
        # Calculate number of check bits based on message length
        self.number_of_check_bits = int(np.ceil(np.log2(self.user_message_len)))
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
        The purpose of this function is to perform the decoding process on a Hamming-encoded message.
        It calculates the binary syndrome of the modified message,
        identifies the error position, corrects errors if possible,
        extracts the original message bits by removing the check bits,
        and stores the decoded message and error position for further use.
        """
        if self.modified_message is not None:
            # Calculate error position and correct errors if possible.
            self.binary_syndrome = self._calculate_syndrome(self.modified_message)
            error_pos = 0
            decoded_msg = np.copy(self.modified_message)
            for num, item in enumerate(self.binary_syndrome):
                error_pos += item * (self.check_indices[num] + 1)
            if error_pos > 0:
                decoded_msg[error_pos - 1] ^= 1

            # Extract original message bits.
            decoded_msg = np.delete(decoded_msg, self.check_indices)
            self.decoded_message = decoded_msg
            self.error_pos = error_pos - 1

    def _create_generating_matrix(self):
        """
        The purpose of this function is to create a generating matrix used for calculating check bits
        and syndromes in Hamming encoding.
        It generates the matrix based on the message length, number of check bits, and check bit addresses.
        The resulting matrix is stored in the generating_matrix attribute for further use within the model
        """
        if self.user_message_len and self.number_of_check_bits and self.check_indices:
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
        The purpose of this function is to calculate the syndrome or the value of the check bits
        for a given message in Hamming encoding.
        It utilizes the generating matrix stored in the generating_matrix attribute and performs
        the necessary calculations to determine the check bit values.
        :param message:  expected to be a NumPy array containing the message for which the syndrome needs to be calculated.
        :return: resulting check bit values, represented as a binary syndrome
        """
        if self.number_of_check_bits is not None and message is not False:
            result = []
            for num in range(self.number_of_check_bits):
                result.append(np.sum(message * self.generating_matrix[num]) % 2)

            return result

    def set_value_user_message_len(self, user_message_len: int):
        """
        The purpose of this function is to receive the desired length of the information block as input,
        convert it to an integer, and set it as the value of the user_message_len attribute within the class.
        This attribute can then be used for further calculations and operations related to the information block length.
        :param user_message_len:  represents the desired length of the information block.
        """
        if user_message_len:
            try:
                user_message_len = int(user_message_len)
                self.user_message_len = user_message_len
            except ValueError:
                raise ValueError('Значение длинны сообщения переданно не правильно')

    def get_value_user_message_len(self) -> int:
        """
        The purpose of this function is to retrieve the value of the information block length
        stored in the user_message_len attribute within the class.
        It ensures that the length value is defined and returns it as an integer.
        :return: value of user_message_len, which represents the length of the information block.
        """
        if self.user_message_len:
            return self.user_message_len
        else:
            raise ValueError('Длинна сообщения не определенна')

    def get_number_of_check_bits(self) -> int:
        """
        The purpose of this function is to retrieve the number of check bits based on the entered length of the message.
        If the number of check bits is already calculated and stored, it returns the stored value.
        Otherwise, it calculates the number of check bits using the formula and returns the calculated value.
        :return: the amount of check bits
        """
        if self.number_of_check_bits:
            return self.number_of_check_bits
        else:
            self.number_of_check_bits = int(np.ceil(np.log2(self.user_message_len + 1)))
            return self.number_of_check_bits

    def generate_message(self):
        """
        The purpose of this function is to generate the information part of the message as a binary array
        if the length of the message is specified.
        It utilizes NumPy to generate random binary values
        and saves the generated array to the self.message attribute for future use.
        """
        if self.user_message_len:
            self.message = np.random.randint(2, size=self.user_message_len)
        else:
            raise ValueError('Длинна информационного блока не указана')

    def set_message(self, input_message: str):
        """
        The purpose of this function is to set the message for the class instance by converting it from a string to a NumPy array.
        It performs validation checks to ensure that the input message is not empty.
        :param input_message: input message as a string
        """
        if input_message:
            message_list = [int(i) for i in input_message]
            self.message = np.array(message_list)
        else:
            raise ValueError('Передаваемое сообщение пустое')

    def get_message(self) -> str:
        """
        The purpose of this function is to retrieve the binary message that was previously entered by the user or generated.
        It ensures that a message exists before returning it as a string.
        :return: message for encode as srting
        """
        if self.message is not None:
            return np.array2string(self.message, separator='')[1:-1]
        else:
            raise ValueError('Сообщение не ввидено/сгенериновано')

    def get_check_indices(self) -> str:
        """
        The purpose of this function is to retrieve the addresses of the check bits as a string,
        with each address separated by spaces.
        It provides a convenient way to display or use the check bit addresses in the desired format.
        :return: String with the addresses of the check bits
        """
        return np.array2string(self.check_indices, separator=' ')[1:-1]

    def get_encoded_message(self) -> str:
        """
        The purpose of this function is to retrieve the encoded message as a string,
        providing a convenient way to access and use the encoded message
        if it has been generated or set in the object instance.
        :return: encoded message in string format
        """
        if self.encoded_message is not None:
            return np.array2string(self.encoded_message, separator='')[1:-1]
        else:
            raise ValueError('Закодированного сообщения нет')

    def get_generating_matrix(self) -> list[str]:
        """
        The purpose of this function is to retrieve the generating matrix in a format suitable for display or further processing.
        It converts the NumPy array representation of the generating matrix into a nested list of strings,
        providing a convenient way to access and use the generating matrix in a human-readable form.
        :return: generating matrix
        """
        result_generating_matrix = []
        for item in self.generating_matrix:
            result_generating_matrix.append(np.array2string(item, separator='')[1:-1])
        return result_generating_matrix

    def set_modify_bits_in_encoded_message(self, bit_addresses_to_modify: list[int] | None):
        """
        The function modifies specific bits in an encoded message and assigns the
         modified message to self.modified_message
        :param bit_addresses_to_modify: a list of integers representing the positions of the bits to be modified.
        It can also accept None if no specific bits need to be modified.
        """
        if bit_addresses_to_modify is not None:
            if bit_addresses_to_modify and self.encoded_message is not None:
                modified_message = []
                for id, bit in enumerate(self.encoded_message):
                    if id in bit_addresses_to_modify:
                        bit ^= 1
                        modified_message.append(bit)
                    else:
                        modified_message.append(bit)

                self.modified_message = np.array(modified_message)

            else:
                raise ValueError('Не получено закодированное сообщение для модификации')
        else:
            self.modified_message = self.encoded_message

    def get_modified_message(self) -> str:
        """
        The function retrieves the modified message obtained from
        the set_modify_bits_in_encoded_message.
        The function does not take any arguments but is a method of an object instance.
        The function checks that a modified message has been previously set.
        :return:The modified message string is then returned as the result of the function
        """
        if self.modified_message is not None:
            return np.array2string(self.modified_message, separator='')[1:-1]
        else:
            raise ValueError('Модифицированное закодированное сообщение не определено')

    def get_decoded_message(self) -> str:
        """
        The function retrieves the decoded message obtained from a decoding process.
        :return:The decoded message string is then returned as the result of the function.
        """
        if self.decoded_message is not None:
            return np.array2string(self.decoded_message, separator='')[1:-1]
        else:
            raise ValueError('Декодирование сообщение не определено')

    def get_error_pos_and_binary_syndrome(self) -> list[int, list]:
        """
        The function retrieves the error position and binary syndrome associated with
        a decoding process.
        The function does not take any arguments but is a method of an object instance.
        :return:The returned list provides information about the error position and the binary syndrome associated with
        the decoding process.
        """
        if self.error_pos and self.binary_syndrome:
            return [self.error_pos, self.binary_syndrome]
        else:
            raise ValueError('Позиция ошибки и синдром не определены')


class HemmingView(Window):
    def __init__(self):
        super().__init__()
        self.show()

    def get_message_len_value(self) -> int:
        """
        The function retrieves the value from a message length input field and returns it as an integer.
        The function does not take any arguments but is a method of an object instance.
        :return: value from a message length input field
        """
        try:
            message_len_value = int(self.message_len.text())
            return message_len_value
        except ValueError:
            raise ValueError('Нужно ввести целое число')

    def set_message_len_value_to_label(self, message_len_value: int):
        """
        The function sets the value of the message length to a label widget.
        :param message_len_value: integer representing the length of the message
        :return: The function is designed to update the label widget with the message length value to display it to the user.
        """
        if message_len_value:
            self.label_message_len.setText(f'Длинна сообщения: {message_len_value}')
        else:
            raise ValueError('Длинна сообщения не переданна')

    def connect_message_len_button(self, callback: classmethod):
        """
        The function establishes a connection between a button clicked signal and a specified callback method.
        :param callback: representing a class method that will be invoked when the button is clicked
        """
        self.message_len_button.clicked.connect(callback)

    def set_label_number_of_check_bit(self, number_of_check_bit: int):
        """
        The function is intended to set the label widget's text to indicate the count of check bits,
        providing information to the user.
        :param number_of_check_bit: an integer representing the count of check bits
        """
        if number_of_check_bit:
            self.label_number_of_check_bit.setText(f'Количество проверочных бит: {number_of_check_bit}')

    def set_label_coder_type(self, message_len: int, number_of_check_bits: int):
        """
        The function is intended to set the label widget's text to indicate the type of the Hamming block code,
        providing information about the code's parameters to the user.
        :param message_len: an integer representing the length of the message
        :param number_of_check_bits: an integer representing the count of check bits
        """
        if message_len and number_of_check_bits:
            self.label_coder_type.setText(f'Тип  блочного кода Хэмминга:'
                                          f' {message_len + number_of_check_bits},{message_len}')

    def connect_generate_message_button(self, callback: classmethod):
        """
        The purpose of this function is to establish the connection between the button's click event and a specific
        callback function, enabling the execution of custom logic or actions when the button is clicked.
        :param callback: representing a function that will be invoked when the button is clicked
        """
        self.generate_message.clicked.connect(callback)

    def set_input_message_value(self, message: str):
        """
        The purpose of this function is to programmatically set the value of an input widget to a input_message,
        allowing the pre-filling or updating of the input field with the desired text.
        :param message: a string representing the message to be set
        """
        self.input_message.setText(message)

    def connect_encode_button(self, callback: classmethod):
        """
        The purpose of this function is to establish the connection between the button's click event and a specific
        callback method, enabling the execution of custom logic or actions when the button is clicked to trigger the encoding process.
        :param callback: representing a class method that will be invoked when the button is clicked
        """
        self.encode_message.clicked.connect(callback)

    def get_input_message_value(self) -> str:
        """
        The function is designed to retrieve the message text from the input widget for further processing or use in
        other parts of the program.
        The function does not take any arguments but is a method of an object instance.
        :return: If the input widget contains non-empty text, the function retrieves the text from the input widget using
        self.input_message and returns it as a string.
        """
        if self.input_message.text():
            return self.input_message.text()
        else:
            raise ValueError('В поле с сообщением пусто')

    def set_label_check_indices(self, check_indices: str):
        """
        The purpose of this function is to set the label widget's text to indicate the coordinates of the check bits,
        providing information to the user about the positions of the check bits within a larger data structure or system.
        :param check_indices: a string representing the coordinates of the check bits
        """
        self.label_check_indices.setText(f'Координаты проверочных бит: {check_indices}')

    def set_label_input_data(self, input_data: str):
        """
        The purpose of this function is to set the label widget's text to indicate the input data block, providing
        information to the user about the content or nature of the data being processed or displayed
        :param input_data: a string representing the input data block
        """
        self.label_input_data.setText(f'Исходный информационный блок: \n {input_data}')

    def set_label_encoded(self, encoded_message: str, check_indices: str):
        """
        The purpose of this function is to set the label widget's text to indicate the encoded message with certain
        indices highlighted, providing visual emphasis or distinction for specific elements in the encoded data.
        :param encoded_message: a string representing the encoded message
        :param check_indices: a string representing the indices of specific elements in the encoded message that should
        be highlighted
        """
        start_string = '<html><body>'
        end_sting = '</body></html>'
        open_colored_teg = '<span style="font-weight: 700;">'
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

    def set_label_matrix(self, generating_matrix: list[str]):
        """
        The purpose of this function is to set the label widget's text to indicate the generating matrix,
        allowing the user to view the matrix structure
        :param generating_matrix: a list of strings representing the generating matrix
        """
        matrix = ''
        for item in generating_matrix:
            matrix += item + '\n'
        self.label_matrix.setText(matrix)

    def connect_modify_and_decod_button(self, callback: classmethod):
        """
        The purpose of this function is to establish the connection between the button's click event and a specific
        callback method, enabling the execution of custom logic or actions when the button is clicked to trigger the modification and decoding process.
        :param callback: representing a class method that will be invoked when the button is clicked
        """
        self.modify_and_decod_button.clicked.connect(callback)

    def get_modify_and_decod_input(self) -> list[int] | None:
        """
        The purpose of this function is to retrieve the input values for the "Modify and Decode" operation,
        convert them to integers, and return them as a list.
        The function handles input validation by ignoring non-integer values and returns None if no input is provided.
        The function does not take any arguments but is a method of an object instance.
        :return: list of integers denoting places to introduce errors into the encoding of the message,
        or returns None if the field is empty
        """
        if self.modify_and_decod_input.text():
            input_sting = self.modify_and_decod_input.text()
            input_sting = input_sting.replace(',', ' ').replace('.', ' ').split(' ')
            result = []
            for item in input_sting:
                try:
                    result.append(int(item))
                except ValueError:
                    continue
            return result
        else:
            return None

    def set_modified_message_label(self, modified_message: str, bit_addresses_to_modify: list[int] | None):
        if bit_addresses_to_modify is not None:
            start_string = '<html><body>'
            end_sting = '</body></html>'
            open_colored_teg = '<span style="font-weight: 700;">'
            close_colored_teg = '</span>'
            message_with_color = ''
            for id, item in enumerate(modified_message):
                separator = ""
                if id > 9:
                    separator = " "
                if id in bit_addresses_to_modify:
                    message_with_color += separator + open_colored_teg + item + close_colored_teg + '|'
                else:
                    message_with_color += separator + item + '|'
            self.label_modifaed.setText(f'{start_string} Модифицированный информационный блок: <br>'
                                        f'{message_with_color} {end_sting} \n'
                                        f'\n {self._set_format_for_addresses_of_digits(modified_message)}')
        else:
            self.label_modifaed.setText(f'Модифицированный информационный блок: \n '
                                        f'{modified_message}')

    def set_label_binary_syndrome_and_error_pos(self, binary_syndrome: list[int], error_pos: int):
        """
        The purpose of this function is to set the label widget's text to indicate the binary syndrome and error position,
        providing information or feedback to the user about the decoding process
        :param binary_syndrome: a list of integers representing the binary syndrome
        :param error_pos: integer representing the position of the error
        """
        self.label_binary_syndrome_and_error_pos.setText(f'Синдом и позицию ошибки: \n'
                                                         f'{binary_syndrome},  {error_pos}')

    def set_label_decode(self, message: str, decode_message: str):
        """
        The purpose of this function is to set the label widget's text to indicate the original and decoded information
        blocks, providing information or feedback to the user about the decoding process and allowing them to compare the original and decoded data.
        :param message: string representing the original information block
        :param decode_message: string representing the decoded information block
        """
        self.label_decode.setText(f'Исходный и декодированный информационный блок:\n'
                                  f'{message} \n'
                                  f'{decode_message}')

    def _set_format_for_addresses_of_digits(self, message: str) -> str:
        addresses_of_digits = [i for i in range(len(message))]
        formated_addresses_of_digits_to_str_with_separating = ''
        for item in addresses_of_digits:
            formated_addresses_of_digits_to_str_with_separating += str(item) + '|'

        return formated_addresses_of_digits_to_str_with_separating


class HemmingController(QObject):
    def __init__(self, model, view):
        super().__init__()
        self._model = model
        self._view = view

        self._view.connect_message_len_button(self.handle_message_len_button_click)
        self._view.connect_generate_message_button(self.handle_generate_message_button_click)
        self._view.connect_encode_button(self.handle_encode_button_click)
        self._view.connect_modify_and_decod_button(self.handle_modify_and_decod_button_click)

    def handle_message_len_button_click(self):
        """
        The purpose of this function is to handle the button click event related to the message length, update the view
        with the message length value, update the model with the message length value,
        update the view with the number of check bits, and update the view with the coder type label
        """
        message_len = self._view.get_message_len_value()
        self._view.set_message_len_value_to_label(message_len)
        self._model.set_value_user_message_len(message_len)

        number_of_check_bits = self._model.get_number_of_check_bits()
        self._view.set_label_number_of_check_bit(number_of_check_bits)

        self._view.set_label_coder_type(message_len, number_of_check_bits)

    def handle_generate_message_button_click(self):
        """
        The purpose of this function is to handle the button click event related to generating a message,
        generate a message using the model,
        and update the view with the generated message by setting it to the input message field.
        """
        self._model.generate_message()
        message = self._model.get_message()
        self._view.set_input_message_value(message)

    def handle_encode_button_click(self):
        """
        The purpose of this function is to handle the button click event related to encoding a message,
        validate the input message length,
        perform Hamming encoding on the message,
        update the view with the relevant information such as check indices,
        encoded message, and generating matrix.
        """
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

    def handle_modify_and_decod_button_click(self):
        """
        The purpose of this function is to handle the button click event related to modifying and decoding a message.
        It modifies the encoded message based on the specified bit addresses,
        performs Hamming decoding,
        and updates the view with the relevant information such as the modified message,
        binary syndrome, error position, original message, and decoded message.
        """
        bit_addresses_to_modify = self._view.get_modify_and_decod_input()
        self._model.set_modify_bits_in_encoded_message(bit_addresses_to_modify)

        modified_message = self._model.get_modified_message()
        self._view.set_modified_message_label(modified_message, bit_addresses_to_modify)

        self._model.hamming_decode()
        decoded_message = self._model.get_decoded_message()
        err_pos, binary_syndrome = self._model.get_error_pos_and_binary_syndrome()
        self._view.set_label_binary_syndrome_and_error_pos(binary_syndrome, err_pos)
        message = self._model.get_message()
        self._view.set_label_decode(message, decoded_message)


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
