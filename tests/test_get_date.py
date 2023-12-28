from src.utils import get_date

def test_get_date():
    input_date = '2022-02-14T12:34:56.789012'
    result = get_date(input_date)
    assert result == '14.02.2022'

