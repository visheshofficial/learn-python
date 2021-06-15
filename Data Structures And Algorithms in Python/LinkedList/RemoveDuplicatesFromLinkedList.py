# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.

    cur_node = linkedList
    while cur_node.next:
        next_node = cur_node.next
        if next_node.value == cur_node.value:
            cur_node.next = next_node.next
        else:
            cur_node = cur_node.next
    return linkedList


import unittest


class LinkedListTest(LinkedList):
    def addMany(self, values):
        current = self
        while current.next is not None:
            current = current.next
        for value in values:
            current.next = LinkedListTest(value)
            current = current.next
        return self

    def getNodesInArray(self):
        nodes = []
        current = self
        while current is not None:
            nodes.append(current.value)
            current = current.next
        return nodes


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        test = LinkedListTest(1).addMany([1, 3, 4, 4, 4, 5, 6, 6])
        expected = LinkedListTest(1).addMany([3, 4, 5, 6])
        actual = removeDuplicatesFromLinkedList(test)
        self.assertEqual(expected.getNodesInArray(), actual.getNodesInArray())
