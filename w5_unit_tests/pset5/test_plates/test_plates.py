from plates import is_valid

def test_is_valid_length_check():
    assert is_valid("C") == False
    assert is_valid("CS50") == True

def test_is_valid_punctuation_check():
    assert is_valid("CS,50") == False
    assert is_valid("HEL LO") == False

def test_is_valid_minimim():
    assert is_valid("Alex36") == True
    assert is_valid("12Alex") == False

def test_is_valid_alpha_check():
    assert is_valid("AAA222") == True
    assert is_valid("AA220A") == False
    assert is_valid("PI3.14") == False

def test_is_valid_zero_check():
    assert is_valid("Alex01") == False
    assert is_valid("Alex10") == True

def test_is_valid_alphaCheck():
    assert is_valid("Hello") == True
    assert is_valid("1234") == False
    assert is_valid("") == False


