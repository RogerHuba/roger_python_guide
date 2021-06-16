from data_structures.stacks_and_queues.stacks_and_queues import Queue


class Node:
    """Node class
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.__class__.__name__}({self.val})'

    def __str__(self):
        l = self.left.val if self.left else None
        r = self.right.val if self.right else None
        return f'left: ({l}) -- ({self.val}) -- ({r}) :right'


class BinaryTree:
    """Binary Tree class
    """

    def __init__(self, val=None):
        self.root = Node(val) if val else None

    def add(self, val: any) -> None:
        """Add a new node with Breadth first approach

        Args:
            val (any): Value to add
        """
        new_node = Node(val)
        if self.root:
            q = Queue()
            q.enqueue(self.root)

            while not q.is_empty():
                node = q.dequeue()

                if node.left:
                    q.enqueue(node.left)
                else:
                    node.left = new_node
                    return

                if node.right:
                    q.enqueue(node.right)
                else:
                    node.right = new_node
                    return

        else:
            self.root = new_node

    def contains(self, val: any) -> bool:
        """Return whether or not the given value is in the tree

        Args:
            val (any): Value to look for

        Returns:
            bool: Whether or not the value is present in the tree
        """
        def traverse(node):
            if node:
                if node.val == val:
                    return True
                traverse(node.left)
                traverse(node.right)
                return False

        return traverse(self.root)

    def pre_order(self) -> list:
        """Traverse the list in pre-order manner: root >> left >> right

        Returns:
            list: List of values
        """
        output = []

        def traverse(node):
            if node:
                output.append(node.val)
                traverse(node.left)
                traverse(node.right)

        traverse(self.root)

        return output

    def in_order(self) -> list:
        """Traverse the list in pre-order manner: left >> root >> right

        Returns:
            list: List of values
        """
        output = []

        def traverse(node):
            if node:
                traverse(node.left)
                output.append(node.val)
                traverse(node.right)

        traverse(self.root)

        return output

    def post_order(self):
        """Traverse the list in pre-order manner: left >> right >> root

        Returns:
            list: List of values
        """
        output = []

        def traverse(node):
            if node:
                traverse(node.left)
                traverse(node.right)
                output.append(node.val)

        traverse(self.root)

        return output

    def breadth_first(self) -> list:
        """Traverse the tree in breadth-first manner

        Returns:
            list: Values of the tree
        """
        output = []
        if self.root:
            q = Queue()
            q.enqueue(self.root)

            while not q.is_empty():
                el = q.dequeue()
                output.append(el.val)

                if el.left:
                    q.enqueue(el.left)
                if el.right:
                    q.enqueue(el.right)

        return output

    def max_val(self) -> int:
        """Get the maximum value of the tree

        Returns:
            int: maximum value of the tree
        """
        if self.root:
            _max = self.root.val

            def traverse(node):
                nonlocal _max
                if node:
                    if node.val > _max:
                        _max = node.val
                    traverse(node.left)
                    traverse(node.right)
                    return _max

            traverse(self.root)
            return _max


class BinarySearchTree(BinaryTree):
    """Binary Search Tree class
    """

    def add(self, val: any) -> None:
        """Add a value to the BST (values that are strictly less than the root - got to the left, the rest - to the right)

        Args:
            val (any): Value to be inserted
        """
        new_node = Node(val)

        def traverse(node):
            if new_node.val < node.val:
                if node.left:
                    traverse(node.left)
                else:
                    node.left = new_node
            else:
                if node.right:
                    traverse(node.right)
                else:
                    node.right = new_node

        if self.root:
            traverse(self.root)
        else:
            self.root = new_node
