import math
import mpmath

from work_files import *

PI = {0: 0.2148, 1: 0.3672, 2: 0.2305, 3: 0.1875}
max_length_block = 8


def frequency_test_nist(path: str, write: str, key: str) -> None:
    """
    Performs a frequency test NIST on a binary sequence and writes the result to a file.

    Parameters:
        path(str): the path to the JSON file containing the binary sequence.
        write(str): the path to write the result of the test.
        key(str): the key in the dictionary to the binary sequence.
    """
    sequence = read_jsons(path)
    try:
        b_sequence = [-1 if bit == "0" else 1 for bit in sequence.get(key)]
        s_n = sum(b_sequence) / math.sqrt(len(b_sequence))
        p_v = math.erfc(math.fabs(s_n) / math.sqrt(2))
        write_files(write, "Частотный побитовый тест " f'{key} : {p_v} \n')
    except Exception as e:
        print("Error when performing a frequency bitwise test: ", e)


def same_bits_test_nist(path: str, write: str, key: str) -> None:
    """
    Performs a test NIST for the same consecutive bits and writes the result to a file.

    Parameters:
        path(str): the path to the JSON file containing the binary sequence.
        write(str): the path to write the result of the test.
        key(str): the key in the dictionary to the binary sequence.
    """
    sequence = read_jsons(path)
    try:
        n = len(sequence.get(key))
        ones_count = sequence.get(key).count("1")
        proportion_of_ones = ones_count / n
        if abs(proportion_of_ones - 0.5) < (2 / math.sqrt(len(sequence.get(key)))):
            v = 0
            for bit in range(len(sequence.get(key)) - 1):
                if sequence.get(key)[bit] != sequence.get(key)[bit + 1]:
                    v += 1
            numerator = abs(v - 2 * n * proportion_of_ones * (1 - proportion_of_ones))
            denominator = 2 * math.sqrt(2 * n) * proportion_of_ones * (1 - proportion_of_ones)
            p_v = math.erfc(numerator / denominator)
        else:
            p_v = 0
        write_files(write, "Тест на одинаковые подряд идущие биты " f'{key} : {p_v} \n')
    except Exception as e:
        print("An error occurred when performing a test for the same consecutive bits: ", e)


def longest_run_ones_test_nist(path: str, write: str, key: str) -> None:
    """
    Performs a test NIST for the longest sequence of units in a block and writes the result to a file.

    Parameters:
        path(str): the path to the JSON file containing the binary sequence.
        write(str): the path to write the result of the test.
        key(str): the key in the dictionary to the binary sequence.
    """
    sequence = read_jsons(path)
    try:
        len_sequence = len(sequence.get(key))
        blocks = [sequence.get(key)[i:i + max_length_block] for i in range(0, len_sequence, max_length_block)]
        v = {1: 0, 2: 0, 3: 0, 4: 0}
        for block in blocks:
            max_count = 0
            count = 0
            for bit in block:
                count = count + 1 if bit == "1" else 0
                max_count = max(max_count, count)
            match max_count:
                case 0 | 1:
                    v[1] += 1
                case 2:
                    v[2] += 1
                case 3:
                    v[3] += 1
                case _:
                    v[4] += 1
        xi_square = 0
        for i in range(len(PI)):
            xi_square += pow(v[i + 1] - 16 * PI[i], 2) / (16 * PI[i])
        value = mpmath.gammainc(3 / 2, xi_square / 2)
        write_files(write, "Тест на самую длинную последовательность единиц в блоке " f'{key} : {value} \n')
    except Exception as e:
        print("An error occurred while performing the test for the longest sequence of ones in the block: ", e)
