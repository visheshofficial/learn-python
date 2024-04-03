import unittest


# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

def inOrderTraverse(tree, array):
    # Write your code here.
    current_node = tree

    if current_node.left:
        inOrderTraverse(current_node.left, array)
    array.append(current_node.value)
    if current_node.right:
        inOrderTraverse(current_node.right, array)
    return array


def preOrderTraverse(tree, array):
    # Write your code here.
    current_node = tree
    array.append(current_node.value)
    if current_node.left:
        preOrderTraverse(current_node.left, array)
    if current_node.right:
        preOrderTraverse(current_node.right, array)
    return array


def postOrderTraverse(tree, array):
    current_node = tree

    if current_node.left:
        postOrderTraverse(current_node.left, array)
    if current_node.right:
        postOrderTraverse(current_node.right, array)
    array.append(current_node.value)
    return array


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.right = BST(22)

        inOrder = [1, 2, 5, 5, 10, 15, 22]
        preOrder = [10, 5, 2, 1, 5, 15, 22]
        postOrder = [1, 2, 5, 5, 22, 15, 10]
        # result=inOrderTraverse(root, [])

        self.assertEqual(inOrderTraverse(root, []), inOrder)
        self.assertEqual(preOrder, preOrderTraverse(root, []))
        self.assertEqual(postOrder,postOrderTraverse(root, []) )
