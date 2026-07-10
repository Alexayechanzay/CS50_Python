from um import count

def test_count():
    assert count("um, hello, um, world") == 2
    assert count("um....") == 1

def test_count2():
    assert count("yum") == 0
    assert count("UMbrella") == 0

def test_count3():
    assert count("yummy") == 0
    assert count("This is um... really umcommon!") == 1

def test_count4():
    assert count("What to say? um I remembered!") == 1
    assert count("This is really umcommon") == 0

def test_caseSensitivity():
    assert count("UM um ummmmm") == 2
    assert count("um um") == 2