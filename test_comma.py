from comma import *


test_data = {
    1234: '1,234',
    1234567: '1,234,567',
    123456789: '123,456,789',
    10: '10',
    123456.045124: '123456.045124'  # additional test for FP values
}


def test_add_the_commas_humanize():
    for key in test_data:
        assert add_the_commas_humanize(key) == test_data[key]


def test_add_the_commas_regex():
    for key in test_data:
        assert add_the_commas_regex(key) == test_data[key]


def test_add_the_commas_diy():
    for key in test_data:
        assert add_the_commas_diy(key) == test_data[key]


