from test import *


if __name__ == "__main__":

    try:
        setting = read_jsons("setting.json")
        take = setting["from"]
        drop = setting["to"]

        frequency_test_nist(take, drop, "c++")
        frequency_test_nist(take, drop, "java")

        same_bits_test_nist(take, drop, "c++")
        same_bits_test_nist(take, drop, "java")

        longest_run_ones_test_nist(take, drop, 'c++')
        longest_run_ones_test_nist(take, drop, "java")
    except Exception as e:
        print(f"An error occurred during the main execution: {e}")