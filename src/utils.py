import os
import json
from datetime import datetime

def open_json_file(filename):
    ROOT_DIR = os.path.dirname(__file__)
    file_path = os.path.join(ROOT_DIR, filename)

    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_executed(list_of_dicts):
    executed_list = [item for item in list_of_dicts if any(value == 'EXECUTED' for value in item.values())]
    return executed_list

def get_sorted(list_executed):
    sorted_list = sorted(list_executed, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'))
    return sorted_list

def get_last_five(filtered_list):
    last_five_list = filtered_list[-5:]
    return last_five_list

def get_date(date_list):
    for i in date_list:
        if 'date' in i:
            date_str = i['date']
            date_value = datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
            return date_value