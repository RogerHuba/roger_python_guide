from data_structures.stacks_and_queues.stacks_and_queues import Stack


class PseudoQueue:
    """Queue that uses two stacks"""

    def __init__(self):
        """Method initializer
        """
        self.add = Stack()
        self.remove = Stack()

    def __len__(self):
        return len(self.add) + len(self.remove)

    def enqueue(self, val):
        """Add a new element ot the queue

        Args:
            val (any): Value to be added

        Returns:
            any: Value that was added to the queue
        """
        try:
            while self.remove.peek():
                self.add.push(self.remove.pop())
        except AttributeError as err:
            pass

        self.add.push(val)
        return self.add.top.val

    def dequeue(self):
        """Remove the first element from the queue and return its value

        Raises:
            AttributeError: When the method is called on the empty queue

        Returns:
            any: Value of the removed element
        """
        try:
            while self.add.peek():
                self.remove.push(self.add.pop())
        except AttributeError as err:
            pass

        try:
            return self.remove.pop()
        except AttributeError as err:
            raise AttributeError('Cannot be called on empty queue')
