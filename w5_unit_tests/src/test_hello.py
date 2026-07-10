from hello import hello

def test_argument():
    hello("Alex") == "hello, Alex"

def test_default():
    hello() == "hello, world"
