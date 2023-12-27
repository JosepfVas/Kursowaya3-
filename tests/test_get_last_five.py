from src.utils import get_last_five

def test_get_last_five_empty_list():
    result = get_last_five([])
    assert result == []

def test_get_last_five_more():
    input_list = [{'item1': 1}, {'item2': 2}, {'item3': 3}, {'item4': 4}, {'item5': 5}, {'item6': 6}]
    result = get_last_five(input_list)
    expected_output = [{'item2': 2}, {'item3': 3}, {'item4': 4}, {'item5': 5}, {'item6': 6}]
    assert result == expected_output

def test_get_last_five_less():
    input_list = [{'item1': 1}, {'item2': 2}, {'item3': 3}]
    result = get_last_five(input_list)
    assert result == input_list

def test_get_last_five_five():
    input_list = [{'item1': 1}, {'item2': 2}, {'item3': 3}, {'item4': 4}, {'item5': 5}]
    result = get_last_five(input_list)
    assert result == input_list
