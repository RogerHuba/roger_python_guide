class Node:
    """Node class
    """

    def __init__(self, val: any, _next=None) -> None:
        """Class initializer

        Args:
            val (any): value to be stored in the node
            _next (Node, optional): Next node. Defaults to None.
        """
        self.val = val
        self.next = _next

    def __repr__(self) -> str:
        """Formal string representation

        Returns:
            str: How to recreate an instance of the class
        """
        return f'{self.__class__.__name__}({self.val}, {self.next})'

    def __str__(self) -> str:
        """Informal string representation

        Returns:
            str: Current node value
        """
        return f'value: {self.val}'


class Stack:
    """Stack class
    """

    def __init__(self, val=None) -> None:
        """Class initializer

        Args:
            val (any, optional): Value to be passed in to the Stack upon instantiation. Defaults to None.
        """
        self.top = Node(val) if val else None

    def __repr__(self) -> str:
        """Formal string representation

        Returns:
            str: How to recreate an instance of the class
        """
        return f'{self.__class__.__name__}()'

    def __str__(self) -> str:
        """Informal string representation

        Returns:
            str: Values in the current stack top-to-bottom
        """
        output = []
        curr = self.top
        while curr:
            output.append(curr.val)
            curr = curr.next

        return ' -> '.join([f'({val})' for val in output])

    def __len__(self):
        count = 0
        curr = self.top
        while curr:
            count += 1
            curr = curr.next
        return count

    def push(self, val: any) -> None:
        """Add a new element onto the stack

        Args:
            val (any): Value to be stored in the Stack Node
        """
        self.top = Node(val, self.top)

    def pop(self) -> any:
        """Remove the topmost elements from the stack and return its value

        Raises:
            AttributeError: When the method is called on empty stack

        Returns:
            any: Value of the topmost element
        """
        if self.is_empty():
            raise AttributeError('Cannot be called on empty stack')
        else:
            tmp = self.top.val
            self.top = self.top.next
            return tmp

    def peek(self) -> any:
        """Get the value of the topmost element of the stack without removing it

        Raises:
            AttributeError: When the method is called on empty stack

        Returns:
            any: Value of the topmost element
        """
        if self.is_empty():
            raise AttributeError('Cannot be called on empty stack')
        else:
            return self.top.val

    def is_empty(self) -> bool:
        """Check whether the stack is empty

        Returns:
            bool: whether the stack is empty
        """
        return self.top is None


class Queue:
    """Queue class
    """

    def __init__(self, val=None):
        """Class initializer

        Args:
            val (any, optional): Value to be passed in to the Queue upon instantiation. Defaults to None.
        """
        self.front = self.rear = Node(val) if val else None

    def __repr__(self) -> str:
        """Formal string representation

        Returns:
            str: How to recreate an instance of the class
        """
        return f'{self.__class__.__name__}()'

    def __str__(self) -> str:
        """Informal string representation

        Returns:
            str: Values in the current queue front-to-rear
        """
        output = []
        curr = self.front
        while curr:
            output.append(curr.val)
            curr = curr.next

        return 'Front: ' + ' -> '.join([f'({val})' for val in output]) + ' :Rear'

    def __len__(self):
        count = 0
        curr = self.front
        while curr:
            count += 1
            curr = curr.next
        return count

    def enqueue(self, val: any) -> None:
        """Add a new element to the queue

        Args:
            val (any): Value to be stored in the Queue Node
        """
        if self.is_empty():
            self.front = self.rear = Node(val)
        else:
            new_node = Node(val)
            self.rear.next, self.rear = new_node, new_node

    def dequeue(self) -> any:
        """Remove the front elements from the queue and return its value

        Raises:
            AttributeError: When the method is called on empty queue

        Returns:
            any: Value of the front element
        """
        if self.is_empty():
            raise AttributeError('Cannot be called on empty Queue')
        else:
            tmp = self.front.val
            self.front = self.front.next
            return tmp

    def peek(self) -> any:
        """Get the value of the front element of the queue without removing it

        Raises:
            AttributeError: When the method is called on empty queue

        Returns:
            any: Value of the front element
        """
        if self.is_empty():
            raise AttributeError('Cannot be called on empty Queue')
        else:
            return self.front.val

    def is_empty(self):
        """Check whether the queue is empty

        Returns:
            bool: whether the queue is empty
        """
        return self.front is None
