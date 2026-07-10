from bank import value
# import pytest

def test_value_100():
    assert value("What's up, bro?") == 100
    assert value("what's up") == 100

def test_value_20():
    assert value("How's it going?") == 20
    assert value("how's it going?") == 20

def test_value_0():
    assert value("Hello, friends?") == 0
    assert value("hello, world!") == 0

# def test_value_null():
#     with pytest.raises(IndexError):
#         value("")
