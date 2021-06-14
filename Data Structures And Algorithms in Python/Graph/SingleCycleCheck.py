from ctypes import c_uint


def hasSingleCycle(array):
    # Write your code here.
    visited_positions = set()
    visited_positions.add(0)
    current_pos = 0

    while len(visited_positions) <= len(array):
        jump = array[current_pos]
        new_pos = (current_pos + jump) % len(array)
        if new_pos in visited_positions:
            if new_pos == 0 and len(visited_positions) == len(array):
                return True
            else:
                return False
        visited_positions.add(new_pos)
        current_pos = new_pos
    return False


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        # self.assertEqual(hasSingleCycle([2, 3, 1, -4, -4, 2]), True)
        # self.assertEqual(hasSingleCycle([1, -1, 1, -1]), False)
        self.assertEqual(hasSingleCycle([10, 11, -6, -23, -2, 3, 88, 909, -26]), False)
