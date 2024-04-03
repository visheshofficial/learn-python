def findThreeLargestNumbers(array):
    result = array[:3]
    result.sort()
    for index in range(3, len(array)):
        if array[index] > result[2]:
            shift_values(result, array[index], 2)
        elif array[index] > result[1]:
            shift_values(result, array[index], 1)
        elif array[index] > result[0]:
            shift_values(result, array[index], 0)
    return result


def shift_values(array, num, index):
    for i in range(index):
        array[i] = array[i + 1]
    array[index] = num


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(findThreeLargestNumbers([141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]), [18, 141, 541])
