from src.utils import mask_card_number


def test_mask_card_number_credit_card():
    input_number = 'Maestro 1308795367077170'
    result = mask_card_number(input_number)
    assert result == 'Maestro 1308 79** **** 7170'

def test_mask_card_number_bank_account():
    input_number = 'Счет 71687416928274675290'
    result = mask_card_number(input_number)
    assert result == 'Счет **5290'
