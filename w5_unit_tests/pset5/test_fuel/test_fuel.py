from fuel import convert, gauge
import pytest

def test_convert_valueError():
    with pytest.raises(ValueError):
        convert("4/2")

def test_convert_zeroError():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")

def test_convert_normal_data():
    assert convert("2/4") == 50
    assert convert("3/4") == 75

def test_gauge_normal_data():
    assert gauge(90) == '90%'
    assert gauge(25) == '25%'

def test_gauge_boundary_data():
    assert gauge(1) == 'E'
    assert gauge(99) == 'F'

