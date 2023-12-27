from src.utils import get_sorted

def test_get_sorted_empty_list():
    result = get_sorted([])
    assert result == []

def test_get_sorted():
    input_list = [
        {'date': '2022-02-02T14:30:00.000000'},
        {'date': '2021-01-01T12:00:00.000000'},
        {'date': '2023-03-03T18:45:00.000000'},
    ]
    result = get_sorted(input_list)
    expected_output = [
        {'date': '2021-01-01T12:00:00.000000'},
        {'date': '2022-02-02T14:30:00.000000'},
        {'date': '2023-03-03T18:45:00.000000'},
    ]
    assert result == expected_output
