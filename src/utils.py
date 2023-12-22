import os
import json

def open_json_file(filename):
    ROOT_DIR = os.path.dirname(__file__)
    file_path = os.path.join(ROOT_DIR, filename)

    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_executed(list_of_dicts):
    executed_list = [item for item in list_of_dicts if any(value == 'EXECUTED' for value in item.values())]
    return executed_list

def get_sorted(filtered_list):
    sorted_list = sorted(filtered_list, key=lambda x: list(x.keys())[0])
    return sorted_list
