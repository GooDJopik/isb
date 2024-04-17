from works_file import *

alphabet = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя :.,?/!()- \n "


def encrypt(path_key: str, kill_path: str, path: str) -> None:
    """
    Implements a cipher with a key and writes the data to a file

    Parameters:
    path_key: str - the path to the key file
    kill_path: str - path to the file where the message is located
    path: str - the path where the cipher will be written
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

    Parameters:
    path_encryption: str - the path to the encrypted text file
    path_key: str - the path to the key file
    path_decryption: str - the path to the file where the decrypted text will be written
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


def key_json(key: str, path: str) -> None:
    """
    Create a key to the text using the transpose method for a given key
    value and write it to a json file as a dictionary

    Parameters:
    key: str - the values of the key that will be used to create a new one
    path: str - the path where the key will be written
    """
    keyword = key

    keyword_set = set()
    shifted_alphabet = ''

    for letter in keyword:
        if letter not in keyword_set:
            keyword_set.add(letter)
            shifted_alphabet += letter

    for letter in alphabet:
        if letter not in keyword_set:
            shifted_alphabet += letter

    key_mapping = {alphabet[i]: shifted_alphabet[i] for i in range(len(alphabet))}
    write_json(key_mapping, path)


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
