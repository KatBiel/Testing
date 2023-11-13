from lib.report_length import *

def test_report_lenght_observation():
    result = report_length('observation')
    assert result == 'This string was 11 characters long.'

def test_report_lenght_11():
    result = report_length('11')
    assert result == 'This string was 2 characters long.'