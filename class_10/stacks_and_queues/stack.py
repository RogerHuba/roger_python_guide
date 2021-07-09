from invalid_operation_error import InvalidOperationError
from node import Node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        self.top = Node(value, self.top)

    def pop(self):

        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")

        popped = self.top

        self.top = self.top.next

        return popped.value

    def is_empty(self):
        return self.top == None

    def peek(self):

        if not self.top:
            raise InvalidOperationError("Method not allowed on empty collection")

        return self.top.value
