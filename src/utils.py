import os
import json

def open_json_file(filename):
    ROOT_DIR = os.path.dirname(__file__)
    file_path = os.path.join(ROOT_DIR, filename)

    with open(file_path, encoding="utf-8") as file:
        data = json.load(file)
    return data


