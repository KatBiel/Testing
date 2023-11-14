from lib.counter import *

# Initially reposts count of zero

def test_count_zero():
    counter = Counter()
    assert counter.report() == 'Counted to 0 so far.'

# Add number 5 to a counter

def test_count_add_five():
    counter = Counter()
    counter.add(5)
    assert counter.report() == 'Counted to 5 so far.'

# Add multiple numbers

def test_count_multiple_numbers():
    counter = Counter()
    counter.add(5) 
    counter.add(10)
    counter.add(15)
    assert counter.report() == 'Counted to 30 so far.'
