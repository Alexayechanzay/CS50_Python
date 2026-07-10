# from calculator import square

# def main():
#     test_square()

# def test_square():
#     # if square(2) != 4:
#     #     print("2 square was not 4")
#     # if square(3) != 9:
#     #     print("3 square was not 9")

#     # try:
#     #     assert square(2) == 4
#     # except:
#     #     print("2 square was not 4")
#     # try:
#     #     assert square(-2) == 4
#     # except:
#     #     print("-2 square was not 4")
#     # try:
#     #     assert square(3) == 9
#     # except:
#     #     print("3 square was not 9")
#     # try:
#     #     assert square(-3) == 9
#     # except:
#     #     print("-3 square was not 9")



# if __name__ == "__main__":
#     main()

from calculator import square
import pytest

# def test_square():
    # test_num = [2,-2,3,-3,0]
    # test_ans = [4,4,9,9,0]
    # for i in range(len(test_num)):
    #     assert square(test_num[i]) == test_ans[i]

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

def test_str():
    with pytest.raises(TypeError):
        square("cat")
