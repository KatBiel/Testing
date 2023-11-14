from lib.string_builder import *

def test_string_octopus():
    builder = StringBuilder()
    builder.add('octopus')
    assert builder.size() == 7, builder.output() == 'octopus'

def test_strings_multiple():
    builder = StringBuilder()
    builder.add('100')
    builder.add('kitty')
    builder.add('cats')
    assert builder.size() == 12, builder.output() == '100 kitty cats'