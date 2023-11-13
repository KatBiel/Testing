from lib.greet import *

def test_greet_return_hello_Sarah():
    result = greet('Sarah')
    answer = 'Hello, Sarah!'
    assert result == answer

def test_greet_return_hello_Emily():
    result = greet('Emily')
    assert result == 'Hello, Emily!'