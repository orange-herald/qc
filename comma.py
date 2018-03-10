import re
import humanize


def add_the_commas_humanize(i):
    """
    Simplest method using third-party hummanize package.
    :link https://pypi.python.org/pypi/humanize
    :param i: Integer value to format.
    :return: Value with thousands separated with commas
    """
    return str(humanize.intcomma(i))


def add_the_commas_regex(i):
    """
    Simple-ish implementation using regular expression
    to parse string version of input and insert correct
    number of thousands separators (',').
    :param i: Integer value to format.
    :return: Value with thousands separated with commas
    """

    number = str(i)

    # Simple case - no commas required
    if len(number) < 4:
        return number

    decimal_part = False

    # Special case: decimal values
    if number.find('.') is not -1:
        decimal_part = number.split('.')[1]
        number = number.split('.')[0]

    """
    Regular expression tokenizes value in groups of
    three '000's as long as there is still one or
    two leading digits. 
    """
    pattern = r'(?<=[0-9])(?=(?:[0-9]{3})+(?![0-9]))'
    separator = ','
    good_number = re.sub(pattern, separator, number)

    if decimal_part is not False:
        good_number = '.'.join([good_number, decimal_part])

    return str(good_number)


def add_the_commas_diy(i):
    """
    Most complex method using homebrew implementation.
    :param i: Integer value to format.
    :return: Value with thousands separated with commas
    """
    number = str(i)

    # Simple case - no commas required
    if len(number) < 4:
        return number

    decimal_part = False

    # Special case: decimal values
    if number.find('.') is not -1:
        decimal_part = number.split('.')[1]
        number = number.split('.')[0]

    number_list = list(number)

    good_number = []

    first_comma = len(number) % 3
    if first_comma is 0:
        first_comma = 3

    last_comma = len(number) - 3
    commas = list(range(first_comma, last_comma + 1, 3))

    position = 0
    while position is not len(number_list):
        if position in commas:
            good_number.append(',')
        good_number.append(number_list[position])
        position += 1

    good_number = ''.join(good_number)

    if decimal_part is not False:
        return '.'.join([good_number, decimal_part])

    return good_number
