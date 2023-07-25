class Node:
    """
    A node in a singly-linked list.

    Attributes:
        data (any): The data stored in the node.
        next (Node): The next node in the list.

    """

    def __init__(self, data):
        """
        Initializes a new node with the given data.

        Args:
            data (any): The data to store in the node.

        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A singly-linked list.

    Attributes:
        head (Node): The first node in the list.
        size (int): The number of nodes in the list.

    """

    def __init__(self):
        """
        Initializes an empty linked list.

        """
        self.head = None
        self.size = 0

    def add_first(self, data):
        """
        Adds a new node with the given data to the beginning of the list.

        Args:
            data (any): The data to store in the new node.

        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def remove_first(self):
        """
        Removes the first node from the list and returns its data.

        Returns:
            any: The data stored in the removed node.

        Raises:
            IndexError: If the list is empty.

        """
        if not self.head:
            raise IndexError("Cannot remove from empty list.")
        data = self.head.data
        self.head = self.head.next
        self.size -= 1
        return data

    def __len__(self):
        """
        Returns the number of nodes in the list.

        Returns:
            int: The number of nodes in the list.

        """
        return self.size