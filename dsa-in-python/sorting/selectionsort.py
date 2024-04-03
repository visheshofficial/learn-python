def selectionSort(array):
    for index in range(len(array)):
        smallest_index = index
        for j in range(index+1,len(array)):
            if array[j] < array[smallest_index]:
                smallest_index = j
        if smallest_index != index:
            array[index], array[smallest_index] = array[smallest_index], array[index]
    return array


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual([2, 3, 5, 5, 6, 8, 9], selectionSort([8, 5, 2, 9, 5, 6, 3]))
