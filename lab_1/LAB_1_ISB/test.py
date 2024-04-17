from works_file import *

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя :.,?/!()- \n "


def encrypt(path_key: str, kill_path: str, path: str) -> None:
    """
    implements a cipher with a key and writes the data to a file

    Parameters
        path_key: the path to the key file
        text_path: path to the file where the message is located
        path: the path where the cipher will be written
    """
    key = read_json(path_key)
    result = ''
    text = read_files(kill_path)
    for char in text:
        if char in key:
            result += key[char]
        else:
            result += char
    write_files(path, result)


def decrypt(path_encryption: str, path_key: str, path_decryption: str) -> None:
    """
    Decrypts the text by the key

    Parameters
        path_key: the path to the key file
        path_encryption: the path to the encrypted text file
        path_decryption: the path to the file where the decrypted text will be written
    """
    key = read_json(path_key)
    result = ''
    text = read_files(path_encryption)
    for char in text:
        found_key = None
        for k, v in key.items():
            if v == char:
                found_key = k
                break

        result += found_key
    write_files(path_decryption, result)


def key_json(key: str, path: str):
    """
    Create a key to the text using the transpose method for a given key
    value and write it to a json file as a dictionary

    Parameters
        key: the values of the key that will be used to create a new one
        path: the path where the key will be written
    """
    sz = len(key)
    key = dict()
    num_rows = -(-len(alphabet) // sz)
    matrix = [['' for _ in range(sz)] for _ in range(num_rows)]

    index = 0
    for row in range(num_rows):
        for col in range(sz):
            if index < len(alphabet):
                matrix[row][col] = alphabet[index]
                index += 1

    ciphertext = ''
    for col in range(sz):
        for row in range(num_rows):
            ciphertext += matrix[row][col]

    for i, char in enumerate(alphabet):
        key[char] = ciphertext[i]
    write_json(key, path)


if __name__ == "__main__":

    try:
        config = read_json("config.json")
        text_path = config["text_path_task1"]
        key_path = config["key_path_task1"]
        encryption_path = config["encryption_path_task1"]
        decryption_path = config["decryption_path_task1"]
        keys = config["keys_task1"]

        key_json(keys, key_path)
        encrypt(key_path, text_path, encryption_path)
        decrypt(encryption_path, key_path, decryption_path)
    except Exception as e:
        print(f"An error occurred during the main execution: {e}")
