import pytest

from data_structures.tree.k_ary_tree import Node, Tree

from .fizz_buzz_tree import fizz_buzz, fizz_buzz_tree


class TestFizzBuzz:

    def test_proof_of_life(self):
        assert fizz_buzz

    def test_fizz_buzz(self):
        assert fizz_buzz(15) == 'FizzBuzz'

    def test_fizz(self):
        assert fizz_buzz(3) == 'Fizz'

    def test_buzz(self):
        assert fizz_buzz(5) == 'Buzz'

    def test_none(self):
        assert fizz_buzz(8) == '8'


class TestFizzBuzzTree:

    def test_proof_of_life(self):
        assert fizz_buzz_tree

    @pytest.fixture()
    def tree(self):
        """Return k-ary tree that has the following structure:
               (15)
          /    /   \    \
        (0)  (2)   (4)  (6)
         |    |     |    |
        (0)  (3)   (6)  (9)        

        Returns:
            tree: k-ary tree
        """
        tree = Tree()
        tree.root = Node(15)

        for i in range(4):
            new_el = Node(i * 2)
            tree.root.children.append(new_el)

        for i, child in enumerate(tree.root.children):
            new_el = Node(i * 3)
            child.children.append(new_el)

        return tree

    def test_happy_path(self, tree):
        """Check if the function returns the k-ary tree with the following structure:
                (FB)
          /    /    \    \
        (FB)  (2)   (4)  (F)
          |    |     |    |
        (FB)  (F)   (F)  (F)        

        Returns:
            tree: k-ary tree
        """
        result = fizz_buzz_tree(tree)

        # Root
        assert result.root.val == 'FizzBuzz'

        # First level of children
        assert result.root.children[0].val == 'FizzBuzz'
        assert result.root.children[1].val == '2'
        assert result.root.children[2].val == '4'
        assert result.root.children[3].val == 'Fizz'

        # Second level of children
        assert result.root.children[0].children[0].val == 'FizzBuzz'
        assert result.root.children[1].children[0].val == 'Fizz'
        assert result.root.children[2].children[0].val == 'Fizz'
        assert result.root.children[3].children[0].val == 'Fizz'

    def test_no_root(self):
        tree = Tree()
        assert fizz_buzz_tree(tree).root == None
