from seasons import output, calculate_dob

def test_case1():
    assert output(365) == "Five hundred twenty-five thousand, six hundred minutes"


def test_case3():
    assert output(366) == "Five hundred twenty-seven thousand forty minutes"
