import unittest


def runLengthEncoding(string):
    # Write your code here.
    result = []
    prev_letter = string[0]
    count = 1
    for index in range(1, len(string)):
        cur_letter = string[index]
        if prev_letter == cur_letter:
            if count == 9:
                result.append(str(9) + prev_letter)
                count = 1
            else:
                count += 1
        else:
            result.append(str(count) + prev_letter)
            count = 1
            prev_letter = string[index]
    result.append(str(count) + prev_letter)
    return "".join(result)


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        string = "AAAAAAAAAAAAABBCCCCDD"
        expected = "9A4A2B4C2D"
        actual = runLengthEncoding(string)
        self.assertEqual(expected, actual)
