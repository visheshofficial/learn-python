# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


def threeNumberSort(array, order):
    first_index = 0
    second_index = 0
    third_index = len(array) - 1
    while second_index <= third_index:
        if array[second_index]== order[0]:
            first_index+=1
            second_index+=1




    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        array = [1, 0, 0, -1, -1, 0, 1, 1]
        order = [0, 1, -1]
        expected = [0, 0, 0, 1, 1, 1, -1, -1]
        actual = threeNumberSort(array, order)
        self.assertEqual(actual, expected)
