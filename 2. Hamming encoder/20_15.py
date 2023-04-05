#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from typing import Tuple


class Hemming_20_15_encode:
    def __init__(self):
        # check matrix rows are declared
        self.matrix_transform_fist_row = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0])
        self.matrix_transform_second_row = np.array([0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0])
        self.matrix_transform_third_row = np.array([0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1])
        self.matrix_transform_fourth_row = np.array([0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0])
        self.matrix_transform_fifth_row = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1])

    def hemming_20_15_encode(self, data: np.ndarray) -> np.ndarray:
        """
            Кодирует заданные 15-битные данные, используя схему кодирования Хемминга (20,15).
            Возвращает одномерный массив NumPy из 20 бит, представляющий закодированные данные.
        """

        # extend data with zeros at parity bits
        extended_data = np.array(
            [0, 0, data[0], 0, data[1], data[2], data[3], 0, data[4], data[5], data[6], data[7],
             data[8], data[9], data[10], 0, data[11],  data[12], data[13], data[14]], dtype=int
        )

        # parity bits are calculated
        parti_bit_1 = np.sum(extended_data * self.matrix_transform_fist_row) % 2
        parti_bit_2 = np.sum(extended_data * self.matrix_transform_second_row) % 2
        parti_bit_3 = np.sum(extended_data * self.matrix_transform_third_row) % 2
        parti_bit_4 = np.sum(extended_data * self.matrix_transform_fourth_row) % 2
        parti_bit_5 = np.sum(extended_data * self.matrix_transform_fifth_row) % 2

        # Create array of encoded message bits.
        encoded_data = np.array(
            [parti_bit_1, parti_bit_2, data[0], parti_bit_3, data[1], data[2], data[3], parti_bit_4, data[4], data[5], data[6], data[7],
             data[8], data[9], data[10], parti_bit_5, data[11], data[12], data[13], data[14]], dtype=int
        )

        return encoded_data

    def hamming_20_15_decode(self, encoded_data: np.ndarray) -> Tuple[np.ndarray, bool, int]:
        """
        Decodes a 20-bit message encoded using Hemming (20, 15) code.

        Args:
            encoded_data: A 20-bit binary string.

        Returns:
            A tuple containing the decoded 15-bit binary string and a boolean indicating whether errors were corrected.
        """

        # Calculate syndrome bits.
        s1 = sum(self.matrix_transform_fist_row * encoded_data) % 2
        s2 = sum(self.matrix_transform_second_row * encoded_data) % 2
        s3 = sum(self.matrix_transform_third_row * encoded_data) % 2
        s4 = sum(self.matrix_transform_fourth_row * encoded_data) % 2
        s5 = sum(self.matrix_transform_fifth_row * encoded_data) % 2

        # Calculate error position and correct errors if possible.
        error_pos = s1 + s2 * 2 + s3 * 4 + s4 * 8 + s5 * 16
        if error_pos > 0:
            encoded_data[error_pos - 1] ^= 1

        # Extract original message bits.
        decoded_data = np.array(
            [encoded_data[2], encoded_data[4], encoded_data[5], encoded_data[6], encoded_data[8], encoded_data[9],
             encoded_data[10], encoded_data[11], encoded_data[12], encoded_data[13], encoded_data[14], encoded_data[16],
             encoded_data[17], encoded_data[18], encoded_data[19]], dtype=int
        )

        is_corrected = (error_pos > 0)

        return decoded_data, is_corrected, error_pos


def main():
    data = np.array([1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1])  # Входные данные
    print('Input data:', data)
    coder = Hemming_20_15_encode()
    encoded_data = coder.hemming_20_15_encode(data)  # кодирование данных
    print("Encoded data:", encoded_data)

    # Вношу ошибку в закодированные данные
    error_pos = 4
    encoded_data[error_pos] = 1
    print("Encoded data with error:", encoded_data)
    error_pos = 0
    encoded_data[error_pos] = 1
    print("Encoded data with error:", encoded_data)

    # Декодирую ошибку
    decoded_data, is_corrected, error_pos = coder.hamming_20_15_decode(encoded_data)
    print('Error position:', error_pos)
    print("Decoded data:", decoded_data)
    print("Error corrected:", is_corrected)


if __name__ == '__main__':
    main()
