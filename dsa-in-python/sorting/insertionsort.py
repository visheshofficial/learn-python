import unittest


def insertionSort(array):
    for array_index in range(1, len(array)):
        print(array)
        j = array_index
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual([2, 3, 5, 5, 6, 8, 9], insertionSort([8, 5, 2, 9, 5, 6, 3]))
