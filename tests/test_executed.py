from src.utils import get_executed

def test_get_executed_no_executed():
    input_list = [
        {"state": "CANCELED"},
        {"state": "CANCELED"}
    ]
    result = get_executed(input_list)
    assert result == []

def test_get_executed():
    input_list = [
        {"state": "EXECUTED"},
        {"state": "CANCELED"}
    ]
    result = get_executed(input_list)
    assert result == [{"state": "EXECUTED"}]