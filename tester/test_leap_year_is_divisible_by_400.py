from leapyear import isLeapYear


def test_leap_year_is_divisible_by_400():
    assert isLeapYear(2000) == True
    assert isLeapYear(1600) == True
    assert isLeapYear(1200) == True
