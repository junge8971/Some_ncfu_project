#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from typing import Tuple, List


class Hamming:
    def __init__(self):
        self.user_message_len = None
        self.number_of_check_bits = None
        self.check_indices = None
        self.generating_matrix = None

    def hamming_encode(self, message: np.ndarray) -> np.ndarray:
        """
        Encode a binary message using a Hemming code.

        Args:
            message: A binary numpy array to be encoded.

        Returns:
            A numpy array containing the Hemming-encoded message.
        """
        # Calculate message length
        self.user_message_len = len(message)
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
                encoded[item_id] = message[counter]
                counter += 1
        # Create a generating matrix
        self._create_generating_matrix()

        # From the generating matrix and the encoded array, calculate the value of the check bits
        check_bits = self._calculate_syndrome(encoded)

        # Insert parity bits into their addresses
        for check_bit_id, element in enumerate(self.check_indices):
            encoded[element] = check_bits[check_bit_id]

        return encoded

    def hamming_decode(self, encoded: np.ndarray) -> Tuple[np.ndarray, bool, int]:
        """
        Decode a Hemming-encoded message.

        Args:
            encoded: A numpy array containing the Hemming-encoded message.

        Returns:
            A numpy array containing the decoded binary message.
        """
        # Calculate error position and correct errors if possible.
        binary_syndrome = self._calculate_syndrome(encoded)
        error_pos = 0
        for num, item in enumerate(binary_syndrome):
            error_pos += item * (self.check_indices[num] + 1)
        if error_pos > 0:
            encoded[error_pos - 1] ^= 1

        # Extract original message bits.
        decoded_msg = np.delete(encoded, self.check_indices)

        return decoded_msg, error_pos > 0, error_pos - 1

    def _create_generating_matrix(self):
        """
            Creates a matrix for calculating check bits and syndromes based on:
            message length,
            number of check bits,
            check bits addresses
            Only for use inside the class!
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
            Only for use inside the class!

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


def main():
    # Example binary data
    data = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 1], dtype=int)
    print(f'Input data: {data}')

    coder = Hamming()

    # Encode the data using a Hemming code
    encoded = coder.hamming_encode(data)
    # Print the encoded data
    print(f"Encoded data: {encoded}")

    # Introduce an error into the encoded data
    error_pos = int(input('>>'))
    encoded[error_pos] ^= 1

    # Print the modified encoded data
    print(f"Modified encoded data: {encoded}")

    # Decode the encoded data
    decoded_data, is_corrected, error_pos = coder.hamming_decode(encoded)

    # Print the decoded data
    print('Error position:', error_pos)
    print("Decoded data:", decoded_data)
    print("Error corrected:", is_corrected)

    if np.array_equal(data, decoded_data):
        print('Input array and decoded array ar equal')
    else:
        print('Input array and decoded array not equal')


if __name__ == '__main__':
    main()
