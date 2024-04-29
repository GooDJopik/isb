from works_file import *


def frequency_analysis(text_p: str, path: str) -> None:
    """
    Performs a frequency analysis of the text and writes it to the dictionary in another file

    Parameters
        text_path: the path to the file with the text to analyze
        path: the path to the file where the frequency analysis will be recorded
    """
    text = read_files(text_p)
    frequencies = {}
    total_chars = len(text)
    for char in text:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    for char, count in frequencies.items():
        frequencies[char] = count / total_chars
    sorted_freq = dict(sorted(frequencies.items(), key=lambda x: x[1], reverse=True))
    write_json(sorted_freq, path)


def decrypt(path_key: str, path: str, path_decryption: str) -> None:
    """
    Decrypts the text by the key

    Parameters
        path_key (str): The path to the file containing the encryption key.
        path (str): The path to the file containing the encrypted text.
        path_decryption (str): The path to the file where the decrypted text will be written.
    """
    key = read_json(path_key)
    decrypted_text = ''
    text = read_files(path)
    for char in text:
        if char in key:
            decrypted_text += key[char]
        else:
            decrypted_text += char
    write_files(path_decryption, decrypted_text)


if __name__ == "__main__":
    try:
        config = read_json("config.json")
        text_path = config["text_path_task2"]
        freq_path = config["freq_path_task2"]
        key_path = config["key_path_task2"]
        decryption_path = config["decryption_path_task2"]

        frequency_analysis(text_path, freq_path)
        decrypt(key_path, text_path, decryption_path)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
