from leapyear import isLeapYear


def test_not_leap_year_is_divisible_by_100_not_400():
    assert isLeapYear(1300) == False
    assert isLeapYear(1100) == False
    assert isLeapYear(1000) == False
