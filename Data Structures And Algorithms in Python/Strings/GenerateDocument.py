import unittest


def generateDocument(characters, document):
    character_count_map = {}
    for c in characters:
        if c not in character_count_map:
            character_count_map[c] = 1
        else:
            character_count_map[c] += 1

    for c in document:
        if c not in character_count_map or character_count_map[c]==0:
            return False
        character_count_map[c]-=1

    return True


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        characters = "Bste!hetsi ogEAxpelrt x "
        document = "AlgoExpert is the Best!"
        expected = True
        actual = generateDocument(characters, document)
        self.assertEqual(actual, expected)
