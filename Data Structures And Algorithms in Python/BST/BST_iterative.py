# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
from ctypes import c_uint
import unittest


class BST:
    def __init__(self, value):
        self.value = value
        self.left: BST = None
        self.right: BST = None

    # Average: O(lon(n)) time | O(1) space
    # Worst: O(n) time | O(1) Space

    def insert(self, value):
        current_node = self
        while True:
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = BST(value)
                    break
                else:
                    current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = BST(value)
                    break
                else:
                    current_node = current_node.right

        return self

    # Average: O(lon(n)) time | O(1) space
    # Worst: O(n) time | O(1) Space
    def contains(self, value):
        current_node = self
        while current_node is not None:
            if value < current_node.value:
                current_node = current_node.left
            elif current_node.value < value:
                current_node = current_node.right
            else:
                return True
        return False


def remove(root, key):
    # pointer to store the parent of the current node
    parent = None
    # start with the root node
    curr = root
    # search key in the BST and set its parent pointer
    while curr and curr.value != key:
        # update the parent to the current node
        parent = curr
        # if the given key is less than the current node, go to the left subtree;
        # otherwise, go to the right subtree
        if key < curr.value:
            curr = curr.left
        else:
            curr = curr.right
    # return if the key is not found in the tree
    if curr is None:
        return root
    # Case 1: node to be deleted has no children, i.e., it is a leaf node
    if curr.left is None and curr.right is None:
        # if the node to be deleted is not a root node, then set its
        # parent left/right child to None
        if curr != root:
            if parent.left == curr:
                parent.left = None
            else:
                parent.right = None
        # if the tree has only a root node, set it to None
        else:
            root = None
    # Case 2: node to be deleted has two children
    elif curr.left and curr.right:
        # find its inorder successor node
        successor = curr.right.get_minimum_value()
        # store successor value
        val = successor
        # recursively delete the successor. Note that the successor
        # will have at most one child (right child)
        remove(successor)
        # copy value of the successor to the current node
        curr.value = val
    # Case 3: node to be deleted has only one child
    else:
        # choose a child node
        if curr.left:
            child = curr.left
        else:
            child = curr.right
        # if the node to be deleted is not a root node, set its parent
        # to its child
        if curr != root:
            if curr == parent.left:
                parent.left = child
            else:
                parent.right = child
        # if the node to be deleted is a root node, then set the root to the child
        else:
            root.value = child.value
            root.right = child.right
            root.left = child.left
    return root


def get_minimum_value(self):
    current_node = self
    while current_node.left is not None:
        current_node = current_node.left
    return current_node.value


class TestProgram(unittest.TestCase):
    def test_case_3(self):
        root = BST(10)
        root.insert(5)
        root.insert(15)
        root.insert(2)
        root.insert(5)
        root.insert(13)
        root.insert(22)
        root.insert(1)
        root.insert(14)
        root.insert(12)
        root.remove(5)
        root.remove(5)
        root.remove(12)
        root.remove(13)
        root.remove(14)
        root.remove(22)
        root.remove(2)
        root.remove(1)

    # def test_case_1(self):
    #     root = BST(10)
    #     root.left = BST(5)
    #     root.left.left = BST(2)
    #     root.left.left.left = BST(1)
    #     root.left.right = BST(5)
    #     root.right = BST(15)
    #     root.right.left = BST(13)
    #     root.right.left.right = BST(14)
    #     root.right.right = BST(22)
    #     root.insert(12)
    #     self.assertTrue(root.right.left.left.value == 12)
    #     root.remove(10)
    #     cont = root.contains(10)
    #     self.assertFalse(cont)
    #     # self.assertTrue(root.value == 12)
    #
    #     self.assertTrue(root.contains(15))
    #
    # def test_case_2(self):
    #     root = BST(10)
    #     self.assertTrue(root.contains(10))
    #     root.insert(5)
    #     self.assertTrue(root.contains(5))
    #     root.insert(15)
    #     self.assertTrue(root.contains(15))
    #     root.remove(5)
    #     self.assertFalse(root.contains(5))
    #     # root.remove(15)
    #     # self.assertFalse(root.contains(15))
    #     root.remove(10)
    #     self.assertFalse(root.contains(10))
