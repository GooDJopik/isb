import json


def read_jsons(path: str) -> dict:
    """
    A function for reading data from a JSON file and returning a dictionary.

    Parameters
        path: the path to the JSON file to read
    """
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            data = json.load(file)
        return data
    except FileNotFoundError as e:
        print(f"The JSON file was not found: {str(e)}")
    except Exception as e:
        print(f"An error occurred while reading the JSON file: {str(e)}")


def write_files(path: str, data: str) -> None:
    """
    A function for writing data to a file.

    Parameters
        path: the path to the file to write
        data: data to write to a file
    """
    try:
        with open(path, "a+", encoding='UTF-8') as file:
            file.write(data)
        print(f"The data has been successfully written to the file '{path}'.")
    except FileNotFoundError as e:
        print(f"The file was not found: {str(e)}")
    except Exception as e:
        print(f"An error occurred while writing the file: {str(e)}")