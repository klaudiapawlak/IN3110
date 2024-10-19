from Array import Array

#Tests for 1D array

def test_print():
    """
    Checks if print function returns a nice string
    """
    assert str(Array((4,1), 2, 3, 1, 0)) == "[2, 3, 1, 0]"

def test_add():
    """
    Checks if adding to a 1d-array element-wise returns what it’s supposed to
    """
    assert Array((4,1), 2, 3, 1, 0) + 1 == [3, 4, 2, 1]

def test_add2():
    """
    Checks if adding to a 1d-array element-wise returns what it’s supposed to
    """
    assert Array((4,1), 2, 3, 1, 0) + Array((4,1), 2, 3, 1, 0) == [4, 6, 2, 0]

def test_radd():
    """
    Checks if adding to a 1d-array element-wise returns what it’s supposed to
    """
    assert 1 + Array((4,1), 2, 3, 1, 0) == [3, 4, 2, 1]

def test_sub():
    """
    Checks if substracting to a 1d-array element-wise returns what it’s supposed to
    """
    assert Array((4,1), 2, 3, 1, 0) - 1 == [1, 2, 0, -1]

def test_sub2():
    """
    Checks if substracting to a 1d-array element-wise returns what it’s supposed to
    """
    assert Array((4,1), 2, 3, 1, 0) - Array((4,1), 2, 3, 1, 0) == [0, 0, 0, 0]

def test_rsub():
    """
    Checks if substracting to a 1d-array element-wise returns what it’s supposed to
    """
    assert 1 - Array((4,1), 2, 3, 1, 0) == [-1, -2, 0, 1]

def test_mult():
    """
    Checks if multiplying to a 1d-array element-wise returns what it’s supposed to
    """
    assert Array((4,1), 2, 3, 1, 0) * 2 == [4, 6, 2, 0]

def test_mult2():
    """
    Checks if multiplying to a 1d-array element-wise returns what it’s supposed to
    """
    assert Array((4,1), 2, 3, 1, 0) * Array((4,1), 2, 3, 1, 0) == [4, 9, 1, 0]

def test_rmult():
    """
    Checks if multiplying to a 1d-array element-wise returns what it’s supposed to
    """
    assert 2 * Array((4,1), 2, 3, 1, 0) == [4, 6, 2, 0]

def test_eq():
    """
    Checks if comparing arrays (by ==) returns what it is supposed to - which should be a boolean
    """
    assert (Array((4,1), 2, 3, 1, 0) == Array((4,1), 2, 3, 1, 0)) == True


def test_is_eq():
    """
    Checks if comparing a 1d-array element-wise to another array through is equal
    returns what it’s supposed to - which should be a boolean array.
    """
    test1 = Array((4,1), 2, 3, 1, 0)
    test2 = Array((4,1), 2, 5, 1, 0)
    assert test1.is_equal(test2) == [True, False, True, True]


def test_min():
    """
    Checks if that the the element returned by min element is the ”smallest” one in the array
    """
    test = Array((4,1), 2, 6, 1, 10)
    assert test.min_element() == 1

#Tests for 2D array

def test_2d_add():
    """
    Checks if adding to a 2d-array element-wise returns what it’s supposed to
    """
    assert Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9) + 1 == [2, 3, 4, 5, 6, 7, 8, 9, 10]

def test_2d_add2():
    """
    Checks if adding to a 2d-array element-wise returns what it’s supposed to
    """
    test1 = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9)
    test2 = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert test1 + test2 == [2, 4, 6, 8, 10, 12, 14, 16, 18]

def test_2d_sub():
    """
    Checks if substracting to a 2d-array element-wise returns what it’s supposed to
    """
    assert Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9) - 1 == [0, 1, 2, 3, 4, 5, 6, 7, 8]

def test_2d_sub2():
    """
    Checks if substracting to a 2d-array element-wise returns what it’s supposed to
    """
    test1 = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9)
    test2 = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert test1 - test2 == [0, 0, 0, 0, 0, 0, 0, 0, 0]

def test_2d_mult():
    """
    Checks if multiplying to a 2d-array element-wise returns what it’s supposed to
    """
    assert Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9) * 2 == [2, 4, 6, 8, 10, 12, 14, 16, 18]

def test_2d_mult2():
    """
    Checks if multiplying to a 2d-array element-wise returns what it’s supposed to
    """
    test1 = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9)
    test2 = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert test1 * test2 == [1, 4, 9, 16, 25, 36, 49, 64, 81]

def test_2d_eq():
    """
    Checks if comparing arrays (by ==) returns what it is supposed to - which should be a boolean
    """
    test1 = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9)
    test2 = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert (test1 == test2) == True


def test_2d_is_eq():
    """
    Checks if comparing a 2-dimensional array element-wise to another array through is equal
    returns what it’s supposed to - which should be a boolean array.
    """
    test1 = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9)
    test2 = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 10)
    assert test1.is_equal(test2) == [True, True, True, True, True, True, True, True, False]

def test_2d_min():
    """
    Checks if that the the element returned by min element is the ”smallest” one in the array
    """
    test = Array((3 , 3) , 1, 2, 3, 4, 5, 6, 7, 8, 9)
    assert test.min_element() == 1
