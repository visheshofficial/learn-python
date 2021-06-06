def binarySearch(array, target):
    # Write your code here.
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) // 2
        if target == array[middle]:
            return middle
        elif target < array[middle]:
            right = middle
        else:
            left = middle
    return -1

# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(binarySearch([0, 1, 21, 33, 45, 45, 61, 71, 72, 73], 33), 3)
