import pytest

from .tree_intersection import tree_intersection as ti
from data_structures.tree.tree import BinaryTree as BT


class TestTreeIntersection:

    @pytest.fixture()
    def bt1(self):
        bt1 = BT()
        bt1.add(1)
        bt1.add(2)
        bt1.add(3)
        bt1.add(4)
        bt1.add(5)
        bt1.add(6)
        bt1.add(7)

        return bt1

    @pytest.fixture()
    def bt2(self):
        bt2 = BT()
        bt2.add(1)
        bt2.add(3)
        bt2.add(4)
        bt2.add(4)
        bt2.add(5)
        bt2.add(6)

        return bt2

    def test_proof_of_life(self):
        assert ti
        assert BT

    def test_tree_intersection_non_empty(self, bt1, bt2):
        expected = set((1, 4, 5, 6))
        actual = ti(bt1, bt2)

        assert actual == expected

    def test_tree_intersection_bt1_is_empty(self, bt2):
        bt1 = BT()

        assert ti(bt1, bt2) == set()

    def test_tree_intersection_bt2_is_empty(self, bt1):
        bt2 = BT()

        assert ti(bt1, bt2) == set()

    def test_tree_intersection_both_empty(self):
        bt1 = BT()
        bt2 = BT()

        assert ti(bt1, bt2) == set()

    def test_tree_intersection_no_matches(self):
        bt1 = BT()
        bt1.add('five')
        bt1.add('four')
        bt1.add('three')
        bt1.add('two')
        bt1.add('one')

        bt2 = BT()
        bt2.add(5)
        bt2.add(4)
        bt2.add(3)
        bt2.add(2)
        bt2.add(1)

        assert ti(bt1, bt2) == set()
