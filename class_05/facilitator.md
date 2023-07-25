Certainly! Let's take a closer look at this Python implementation of a singly-linked list.

First, we define a class called Node, which represents a node in the linked list. Each node has two attributes: data, which stores the data for the node, and next, which points to the next node in the list. Here's the code for the Node class:


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
The docstring for the Node class includes a brief description of what a node is in the context of a singly-linked list, as well as a list of the attributes that each node has. The __init__ method initializes a new node with the given data, and sets the next attribute to None by default (since this is the last node in the list).

Next, we define a class called LinkedList, which represents the linked list itself. Each LinkedList object has two attributes: head, which points to the first node in the list (or None if the list is empty), and size, which stores the number of nodes in the list. Here's the code for the LinkedList class:


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
The docstring for the LinkedList class includes a brief description of what a linked list is, as well as a list of the attributes that each LinkedList object has. The __init__ method initializes a new empty linked list by setting the head attribute to None and the size attribute to 0.

The LinkedList class also includes two methods: add_first and remove_first. The add_first method adds a new node to the beginning of the list, while the remove_first method removes the first node from the list and returns its data. Here's the code for these methods:


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

```python
    def add_first(self, data):
        """
        Adds a new node with the given data to the beginning of the list.

        Args:
            data (any): The data to store in the new node.

        """
        new_node = Node(data)
        # create a new node with the given data
        new_node.next = self.head
        # set the new node's next pointer to the current head of the list
        self.head = new_node
        # set the new node as the new head of the list
        self.size += 1
        # increment the size of the list
```

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


