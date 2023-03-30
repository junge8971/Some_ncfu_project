#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from typing import Tuple


def hemming_7_4_encode(data: np.ndarray) -> np.ndarray:
    """
    Кодирует заданные 4-битные данные, используя схему кодирования Хемминга (7,4).
    Возвращает одномерный массив NumPy из 7 бит, представляющий закодированные данные.
    """
    # Вычисляю биты четности
    p1 = (data[0] + data[1] + data[3]) % 2
    p2 = (data[0] + data[2] + data[3]) % 2
    p3 = (data[1] + data[2] + data[3]) % 2

    # Создание закодированных данных
    encoded_data = np.array([p1, p2, data[0], p3, data[1], data[2], data[3]])

    return encoded_data


def hemming_7_4_decode(encoded_data: np.ndarray) -> Tuple[np.ndarray, bool, int]:
    """
    Декодирует заданные 7-битные закодированные данные, используя схему декодирования Хемминга (7,4).
    Возвращает кортеж, содержащий одномерный массив NumPy из 4 бит, представляющий декодированные данные.
    и логическое значение, указывающее, были ли обнаружены и исправлены какие-либо ошибки.
    """
    # Вычисляю биты синдрома
    s1 = (encoded_data[0] + encoded_data[2] + encoded_data[4] + encoded_data[6]) % 2
    s2 = (encoded_data[1] + encoded_data[2] + encoded_data[5] + encoded_data[6]) % 2
    s3 = (encoded_data[3] + encoded_data[4] + encoded_data[5] + encoded_data[6]) % 2

    # Вычисляю позицию ошибки
    error_pos = s1 + s2 * 2 + s3 * 4

    # Исправляю ошибку, если она есть
    if error_pos > 0:
        encoded_data[error_pos - 1] = 1 - encoded_data[error_pos - 1]

    # Извлекаю биты данных
    data = encoded_data[[2, 4, 5, 6]]

    # Указывается была ли ошибка
    is_corrected = (error_pos > 0)

    return data, is_corrected, error_pos


def main():
    data = np.array([1, 0, 1, 0])  # Входные данные
    print('Input data:', data)
    encoded_data = hemming_7_4_encode(data)  # кодирование данных
    print("Encoded data:", encoded_data)

    # Вношу ошибку в закодированные данные
    error_pos = 1
    encoded_data[error_pos] = 1
    print("Encoded data with error:", encoded_data)

    # Декодирую ошибку
    decoded_data, is_corrected, error_pos = hemming_7_4_decode(encoded_data)
    print('Error position:', error_pos)
    print("Decoded data:", decoded_data)
    print("Error corrected:", is_corrected)


if __name__ == '__main__':
    main()
