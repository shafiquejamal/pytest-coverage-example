from module_1a import check_whether_greater_than_5


def test_check_whether_greater_than_5():
    n = 2
    result = check_whether_greater_than_5(n)
    assert result == "2 is not greater than 5."
