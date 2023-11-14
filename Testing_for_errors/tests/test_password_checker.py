import pytest
from lib.password_checker import *

def test_check_valid_password():
    checker = PasswordChecker()
    assert checker.check('KittyKat') == True

def test_check_not_valid_password():
    checker = PasswordChecker()
    with pytest.raises(Exception) as e:
        checker.check('Kitty')
    error_message = str(e.value)
    assert error_message == 'Invalid password, must be 8+ characters.'