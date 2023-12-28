from src.utils import mask_card_number

def test_mask_card_number_credit_card():
    input_number = '1234 5678 9012 3456'
    result = mask_card_number(input_number)
    assert result == '1234 56** **** 3456'

def test_mask_card_number_bank_account():
    input_number = 'счет 1234 567890123456'
    result = mask_card_number(input_number)
    assert result == 'счет **3456'