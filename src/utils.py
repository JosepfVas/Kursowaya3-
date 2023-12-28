import os
import json
from datetime import datetime

def open_json_file(filename):
    with open(filename, 'r', encoding="utf-8") as file:
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

def get_date(input_date):
    input_datetime = datetime.strptime(input_date, '%Y-%m-%dT%H:%M:%S.%f')
    output_date = input_datetime.strftime('%d.%m.%Y')
    return output_date


def mask_card_number(requisites_number):
    requisites = requisites_number
    parts = requisites.split()
    digits = parts[-1]
    if requisites.lower().startswith('счет'):
        hidded_number = f"**{digits[-4:]}"
    else:
        hidded_number = f"{digits[:4]} {digits[4:6]}** **** {digits[-4:]}"
    parts[-1] = hidded_number
    return ' '.join(parts)
