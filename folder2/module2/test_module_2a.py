from module_2a import make_a_list


def test_check_whether_greater_than_5():
    n = 2
    result = make_a_list(n, 1, 2, 3, 4)
    assert result == [1, 2]
