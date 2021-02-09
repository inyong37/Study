# Author      : inyong1020@gmail.com
# Date        : 2020-06-29-Mon.
# Description : Hacker Rank; 30 Days of code; Day 27: Testing.
# State       : Passed.
# Environment : -
# Input       : -
# Output      : -
# Reference   : https://www.hackerrank.com/challenges/30-testing/forum/comments/446721
# Reference   : classmethod, staticmethod, https://hamait.tistory.com/635
# Reference   : metaclasses, https://tech.ssut.me/understanding-python-metaclasses/
# Reference   : object keyword, https://stackoverflow.com/questions/10044321/class-classnameobject-what-sort-of-word-is-object-in-python
# Reference   : assert, https://wikidocs.net/21050
# Reference   : random
"""
This problem is all about unit testing.

Your company needs a function that meets the following requirements:

For a given array of  integers, the function returns the index of the element with the minimum value in the array. If there is more than one element with the minimum value, the returned index should be the smallest one.
If an empty array is passed to the function, it should raise an Exception.
Note: The arrays are indexed from .

A colleague has written that function, and your task is to design  separated unit tests, testing if the function behaves correctly. The implementation in Python is listed below (Implementations in other languages can be found in the code template):

def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if a[i] < a[min_idx]:
            min_idx = i
    return min_idx
Another co-worker has prepared functions that will perform the testing and validate returned results with expectations. Your task is to implement  classes that will produce test data and the expected results for the testing functions. More specifically: function get_array() in TestDataEmptyArray class and functions get_array() and get_expected_result() in classes TestDataUniqueValues and TestDataExactlyTwoDifferentMinimums following the below specifications:

get_array() method in class TestDataEmptyArray has to return an empty array.
get_array() method in class TestDataUniqueValues has to return an array of size at least 2 with all unique elements, while method get_expected_result() of this class has to return the expected minimum value index for this array.
get_array() method in class TestDataExactlyTwoDifferentMinimums has to return an array where there are exactly two different minimum values, while method get_expected_result() of this class has to return the expected minimum value index for this array.
Take a look at the code template to see the exact implementation of functions that your colleagues already implemented.
"""


def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i
    return min_idx


from random import randint


class TestDataEmptyArray(object):
    empty_array = list()

    @staticmethod
    def get_array():
        # complete this function
        array = TestDataEmptyArray.empty_array
        return array


class TestDataUniqueValues(object):
    unique_value_array = set()
    while len(unique_value_array) < 5:
        unique_value_array.add(randint(0, 10))

    @staticmethod
    def get_array():
        # complete this function
        array = list(TestDataUniqueValues.unique_value_array)
        return array

    @staticmethod
    def get_expected_result():
        # complete this function
        array = TestDataUniqueValues.get_array()
        index = array.index(min(array))
        return index


class TestDataExactlyTwoDifferentMinimums(object):
    two_different_min_array = set()
    while len(two_different_min_array) < 4:
        two_different_min_array.add(randint(0, 10))
    two_different_min_array = list(two_different_min_array)
    two_different_min_array.append(min(two_different_min_array))

    @staticmethod
    def get_array():
        # complete this function
        array = TestDataExactlyTwoDifferentMinimums.two_different_min_array
        return array

    @staticmethod
    def get_expected_result():
        # complete this function
        array = TestDataExactlyTwoDifferentMinimums.get_array()
        index = array.index(min(array))
        return index


def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2

    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")
