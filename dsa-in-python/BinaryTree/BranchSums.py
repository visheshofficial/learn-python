# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    branch_sums = []
    barchSumHelper(root, 0, branch_sums)
    return branch_sums


def barchSumHelper(node, total, branch_sums):
    if node.left is None and node.right == None:
        branch_sums.append(total + node.value)
    if node.left:
        barchSumHelper(node.left, total + node.value, branch_sums)
    if node.right:
        barchSumHelper(node.right, total + node.value, branch_sums)


import unittest


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        tree = BinaryTreeNew(1).insert([2, 3, 4, 5, 6, 7, 8, 9, 10])
        self.assertEqual(branchSums(tree), [15, 16, 18, 10, 11])


class BinaryTreeNew(BinaryTree):
    def insert(self, values, i=0):
        if i >= len(values):
            return
        queue = [self]
        while len(queue) > 0:
            current = queue.pop(0)
            if current.left is None:
                current.left = BinaryTree(values[i])
                break
            queue.append(current.left)
            if current.right is None:
                current.right = BinaryTree(values[i])
                break
            queue.append(current.right)
        self.insert(values, i + 1)
        return self


