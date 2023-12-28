from utils import get_date, get_sorted, get_executed, get_last_five, open_json_file, mask_card_number
import os

ROOT_DIR = os.path.dirname(__file__)
FILE_PATH = os.path.join(ROOT_DIR, 'operations.json')

data_file = open_json_file(FILE_PATH)
executed_transactions = get_executed(data_file)
sorted_files = get_sorted(executed_transactions)
last_transactions = get_last_five(sorted_files)

for item in last_transactions:
    if "from" not in item:
        print(f"{get_date(item['date'])} {item['description']}\n-> "
        f"{mask_card_number(item['to'])}\n{item['operationAmount']['amount']}"
        f" {item['operationAmount']['currency']['name']}\n")
    else:
        print(f"{get_date(item['date'])} {item['description']}\n{mask_card_number(item['from'])} -> "
        f"{mask_card_number(item['to'])}\n{item['operationAmount']['amount']}"
        f" {item['operationAmount']['currency']['name']}\n")