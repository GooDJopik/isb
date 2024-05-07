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
        zita = ones_count / n
        if abs(zita - 0.5) < (2 / math.sqrt(len(sequence.get(key)))):
            v = 0
            for bit in range(len(sequence.get(key)) - 1):
                if sequence.get(key)[bit] != sequence.get(key)[bit + 1]:
                    v += 1
            numerator = abs(v - 2 * n * zita * (1 - zita))
            denominator = 2 * math.sqrt(2 * n) * zita * (1 - zita)
            p_v = math.erfc(numerator / denominator)
        else:
            p_v = 0
        write_files(write, "Тест на одинаковые подряд идущие биты " f'{key} : {p_v} \n')
    except Exception as e:
        print("An error occurred when performing a test for the same consecutive bits: ", e)