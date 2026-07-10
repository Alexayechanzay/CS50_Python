from numb3rs import validate

def test_firstByte():
    valid = validate("127.1.1.1")
    invalid = validate("512.512.512.512")
    normal = validate("192.1.1.1")

    assert valid == True
    assert invalid == False
    assert normal == True

def test_secondByte():
    valid = validate("1.255.1.1")
    valid2 = validate("1.0.1.1")
    invalid = validate("64.128.256.512")
    normal = validate("1.192.1.1")

    assert valid == True
    assert valid2 == True
    assert invalid == False
    assert normal == True

def test_thirdByte():
    valid = validate("1.1.255.1")
    valid2 = validate("1.1.0.1")
    invalid = validate("cat")
    normal = validate("1.1.192.1")

    assert valid == True
    assert valid2 == True
    assert invalid == False
    assert normal == True

def test_fourthByte():
    valid = validate("1.1.1.255")
    valid2 = validate("1.1.1.0")
    invalid = validate("1.1.1.001")
    normal = validate("1.1.1.192")

    assert valid == True
    assert valid2 == True
    assert invalid == False
    assert normal == True
    result = validate("000.001.010.100") 
    assert result == False

