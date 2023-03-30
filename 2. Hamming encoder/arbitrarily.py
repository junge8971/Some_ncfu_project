#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from typing import Tuple


def hamming_encode(message: np.ndarray) -> np.ndarray:
    """
    Encode a binary message using a Hamming code.

    Args:
        message: A binary numpy array to be encoded.

    Returns:
        A numpy array containing the Hamming-encoded message.
    """
    n = len(message)
    k = int(np.ceil(np.log2(n + 1)))
    parity_indices = [2**i - 1 for i in range(k)]
    print(parity_indices)
    encoded = np.zeros(n + k, dtype=int)
    j = 0
    for i in range(n + k):
        if i in parity_indices:
            encoded[i] = 0
        else:
            encoded[i] = message[j]
            j += 1
    for i in parity_indices:
        p = 0
        for j in range(i, n + k, 2*i+1):
            p = np.sum(encoded[j:j+i]) % 2
            encoded[i] = p
    return encoded


def hamming_decode(encoded: np.ndarray) -> Tuple[np.ndarray, bool, int]:
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
            p = np.sum(encoded[j:j+i]) % 2
        syndrome |= p << i
    if syndrome == 0:
        encoded = np.delete(encoded, parity_indices)
        return encoded, syndrome > 0, syndrome
    else:
        flipped_bit_index = syndrome - 1
        encoded[flipped_bit_index] ^= 1
        encoded = np.delete(encoded, parity_indices)
        return encoded, syndrome > 0, syndrome


def main():
    # Example binary data
    data = np.array([1], dtype=int)
    print(f'Input data: {data}')

    # Encode the data using a Hamming code
    encoded = hamming_encode(data)

    # Print the encoded data
    print(f"Encoded data: {encoded}")

    # Introduce an error into the encoded data
    encoded[3] ^= 1

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


if __name__ == '__main__':
    main()
