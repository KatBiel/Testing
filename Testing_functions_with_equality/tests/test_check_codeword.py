from lib.check_codeword import *

def test_check_codeword_horse():
    result = check_codeward('horse')
    assert result == 'Correct! Come in.'

def test_check_codeword_house():
    result = check_codeward('house')
    assert result == 'Close, but nope.'

def test_check_codeword_random():
    result = check_codeward('random')
    assert result == 'WRONG!'

def test_check_codeword_first_letter_wrong():
    result = check_codeward('douse')
    assert result == 'WRONG!'