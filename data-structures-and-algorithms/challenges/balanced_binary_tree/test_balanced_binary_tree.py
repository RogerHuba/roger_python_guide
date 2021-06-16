import pytest
from challenges.balanced_binary_tree.balanced_binary_tree import \
    balanced_binary_tree
from data_structures.tree.tree import BinaryTree, Node


class TestBalancedBinaryTree:
    def test_balanced_true(self):
        bt = BinaryTree()
        bt.add(1)
        bt.add(2)
        bt.add(3)
        bt.add(4)
        bt.add(5)
        assert balanced_binary_tree(bt.root) == True

    def test_balanced_false(self):
        bt = BinaryTree()
        bt.root = Node(1)
        bt.root.right = Node(2)
        bt.root.right.left = Node(3)
        bt.root.right.right = Node(4)
        assert balanced_binary_tree(bt.root) == False

    def test_empty_true(self):
        bt = BinaryTree()
        assert balanced_binary_tree(bt.root) == True
