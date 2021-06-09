def caesarCipherEncryptor(string, key):
    # Write your code here.
    key = key % 26
    new_string = []
    a_ord = ord('a')
    z_ord = ord('z')

    for letter in string:
        pos = ord(letter)
        new_pos = pos + key
        if new_pos > z_ord:
            new_pos = a_ord + (new_pos - z_ord) - 1
        new_letter = chr(new_pos)
        new_string.append(new_letter)
    return "".join(new_string)


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(caesarCipherEncryptor("xyz", 2), "zab")
