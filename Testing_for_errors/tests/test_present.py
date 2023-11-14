import pytest
from lib.present import *

def test_wrap_and_unwrap():
    present = Present()
    present.wrap('gift')
    assert present.unwrap() == 'gift'

def test_present_wrapped_already():
    present = Present()
    present.wrap('gift')
    with pytest.raises(Exception) as e:
        present.wrap('another_gift')
    error_message = str(e.value)
    assert error_message == 'No contents have been wrapped.'

def test_present_unwrap_before_wrapping():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == 'A contents has already been wrapped.'

# if we try to wrap an already wrapped present, 
# the first wrapped value is unchanged

def test_present_wrapped_already_preserves_oryginal_value():
    present = Present()
    present.wrap('gift')
    with pytest.raises(Exception) as e:
        present.wrap('another_gift')
    assert present.unwrap() == 'gift'