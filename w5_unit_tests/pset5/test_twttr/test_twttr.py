from twttr import shorten

def test_lower_shroten():
    assert shorten("hello, world") == 'hll, wrld'
    assert shorten("aeiou") == ""

def test_upper_shorten():
    assert shorten("AEIOU") == ""
    assert shorten("HELLO, WORLD") == "HLL, WRLD"

def test_alphanumeric_shorten():
    assert shorten("123Alex") == "123lx"


