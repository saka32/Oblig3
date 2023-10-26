from leapyear import isLeapYear


def test_leap_year_is_divisible_by_4_not_100():
    assert isLeapYear(2004) == True
    assert isLeapYear(2008) == True
    assert isLeapYear(2012) == True

