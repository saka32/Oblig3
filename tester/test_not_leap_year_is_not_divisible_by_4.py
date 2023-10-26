from leapyear import isLeapYear


def test_not_leap_year_is_not_divisible_by_4():
    assert isLeapYear(2001) == False
    assert isLeapYear(2002) == False
    assert isLeapYear(2003) == False
