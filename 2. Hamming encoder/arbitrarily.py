#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from typing import Tuple


class Hamming:
    def __init__(self):
        self.user_message_len = None
        self.number_of_party_bits = None
        self.parity_indices = None
        self.generating_matrix = None

    def hamming_encode(self, message: np.ndarray) -> np.ndarray:
        """
        Encode a binary message using a Hamming code.

        Args:
            message: A binary numpy array to be encoded.

        Returns:
            A numpy array containing the Hamming-encoded message.
        """
        # Calculate message length
        self.user_message_len = len(message)
        # Calculate number of parity bits based on message length
        self.number_of_party_bits = int(np.ceil(np.log2(self.user_message_len + 1)))
        # Find powers of two in message length -1 to get coordinates of check bits
        self.parity_indices = np.array([2**i - 1 for i in range(self.number_of_party_bits)])

        # Create a np.ndarray consisting of 0 corresponding to the length of the message + the number of check bits
        encoded = np.zeros(self.user_message_len + self.number_of_party_bits, dtype=int)

        # Fill in the information bits in the encode list
        counter = 0
        for item_id, _ in enumerate(encoded):
            if item_id not in self.parity_indices:
                encoded[item_id] = message[counter]
                counter += 1
        # Create a generating matrix
        self._create_generating_matrix()

        # From the generating matrix and the encoded array, calculate the value of the check bits
        party_bits = []
        for num_of_party_bit in range(self.number_of_party_bits):
            party_bits.append(np.sum(encoded * self.generating_matrix[num_of_party_bit]) % 2)

        # Insert check bits into their addresses
        for party_bit_id, element in enumerate(self.parity_indices):
            encoded[element] = party_bits[party_bit_id]

        return encoded

    def hamming_decode(self, encoded: np.ndarray) -> Tuple[np.ndarray, bool, int]:
        """
        Decode a Hamming-encoded message.

        Args:
            encoded: A numpy array containing the Hamming-encoded message.

        Returns:
            A numpy array containing the decoded binary message.
        """
        n = len(encoded)
        k = int(np.ceil(np.log2(n)))
        parity_indices = [2**i - 1 for i in range(k)]
        print(parity_indices)
        syndrome = 0
        for i in parity_indices:
            p = 0
            for j in range(i, n, 2*i+1):
                p = np.sum(encoded[j:j + i])
                syndrome |= p << i
        if syndrome == 0:
            encoded = np.delete(encoded, parity_indices)
            return encoded, syndrome > 0, syndrome
        else:
            flipped_bit_index = syndrome - 1
            encoded[flipped_bit_index] ^= 1
            encoded = np.delete(encoded, parity_indices)
            return encoded, syndrome > 0, syndrome

    def _create_generating_matrix(self):
        if self.user_message_len and self.number_of_party_bits and self.parity_indices is not None:
            generating_matrix = []
            for item in self.parity_indices + 1:
                counter = 0
                status = False
                list_of_elements_for_matrix = []
                for _ in range(self.user_message_len + self.number_of_party_bits + 1):
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


def main():
    # Example binary data
    data = np.array([1, 1, 1, 1, 1, 1, 1, 1], dtype=int)
    print(f'Input data: {data}')
    coder = Hamming()

    # Encode the data using a Hamming code
    encoded = coder.hamming_encode(data)
    # Print the encoded data
    print(f"Encoded data: {encoded}")

    ''''
    # Introduce an error into the encoded data
    encoded[8] ^= 1

    # Print the modified encoded data
    print(f"Modified encoded data: {encoded}")
    # Decode the encoded data
    decoded_data, is_corrected, error_pos = hamming_decode(encoded)

    # Print the decoded data
    print('Error position:', error_pos)
    print("Decoded data:", decoded_data)
    print("Error corrected:", is_corrected)

    if np.array_equal(data, decoded_data):
        print('Input array and decoded array ar equal')
    else:
        print('Input array and decoded array not equal')
        
    '''


if __name__ == '__main__':
    main()
