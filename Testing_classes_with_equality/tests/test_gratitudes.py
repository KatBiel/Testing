from lib.gratitudes import *

def test_one_gratitude():
    gratitude = Gratitudes()
    gratitude.add('sunshine')
    assert gratitude.format() == 'Be grateful for: sunshine'

def test_multiple_gratitude():
    gratitude = Gratitudes()
    gratitude.add('sunshine')
    gratitude.add('rain')
    gratitude.add('friends')
    assert gratitude.format() == 'Be grateful for: sunshine, rain, friends'