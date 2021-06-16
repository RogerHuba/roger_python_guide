class Node:
    """Class Node"""

    def __init__(self, val: any) -> None:
        """class Constructor

        Args:
            val (any): Value to be saved within the node
        """
        self.val = val
        self.next = None

    def __str__(self):
        return f'{{{self.val}}}'

    def __repr__(self):
        return f'Node({self.val})'


class LinkedList:
    """Class Singly Linked List"""

    def __init__(self, val: Node=None) -> None:
        """class Constructor

        Args:
            val (any, optional): Value to be passed to the head node upon LL instantiation. Defaults to None.
        """
        self.head = None
        if not val is None:
            new_node = Node(val)
            self.head = new_node

    def insert(self, val: any) -> None:
        """Prepends a new instance of Node class with a given value before LL head node

        Args:
            val (any): Value to be passed over to the Node
        """
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def includes(self, target: any) -> bool:
        """Traverses the LL and returns whether the given value is present in the List

        Args:
            target (any): Value to look for

        Returns:
            bool: Whether the value was found
        """
        curr = self.head
        while curr:
            if curr.val == target:
                return True
            curr = curr.next
        return False

    def append(self, val: any) -> None:
        """Appends a node with the given value to the end of the Linked List

        Args:
            val (any): Value to be passed in
        """
        new_node = Node(val)
        if self.head:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        else:
            self.head = new_node

    def insert_before(self, val: any, new_val: any) -> bool:
        """Inserts a node with the given new value before the first occurrence of the given target value. Returns False otherwise

        Args:
            val (any): Target value to look for
            new_val (any): New value to be passed in

        Returns:
            bool: Whether the insertion was successful
        """
        curr = prev = self.head
        while curr:
            if curr.val == val:
                new_node = Node(new_val)
                if curr == self.head:
                    self.head = new_node
                    new_node.next = curr
                else:
                    prev.next = new_node
                    new_node.next = curr
                return True
            else:
                prev, curr = curr, curr.next
        else:
            return False

    def insert_after(self, val: any, new_val: any) -> bool:
        """Inserts a node with the given new value after the first occurrence of the given target value. Returns False otherwise

        Args:
            val (any): Target value to look for
            new_val (any): New value to be passed in

        Returns:
            bool: Whether the insertion was successful
        """
        curr = self.head
        while curr:
            if curr.val == val:
                new_node = Node(new_val)
                new_node.next = curr.next
                curr.next = new_node
                return True
            else:
                curr = curr.next
        else:
            return False

    def ll_len(self) -> int:
        """Counts the length of the LL

        Returns:
            int: Number of nodes
        """
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def kth_from_end_val(self, k: int) -> any:
        """Returns value of the k-th from the end node

        Args:
            k (int): node position from the LL tail

        Raises:
            Exception: k is not int
            Exception: k is negative
            Exception: k is greater than LL length

        Returns:
            any: Node value
        """
        if type(k) is not int:
            raise Exception('k must be an integer')
        if k < 0:
            raise Exception('k must be greater than 0')
        curr = self.head
        steps = self.ll_len() - k
        if steps < 1:
            raise Exception('k must be less than the length of the list')
        for _ in range(1, steps):
            curr = curr.next
        return curr.val

    def __str__(self) -> str:
        """LL class String representation

        Returns:
            str: Visual LL representation
        """
        curr = self.head
        output = ''
        while not curr is None:
            output += f'{{{ curr.val }}} -> '
            curr = curr.next
        output += 'None'
        return output

    @staticmethod
    def mergeLists(ll_1: object, ll_2: object) -> object:
        """Merge two given Linked Lists (in place) and return the head of the new list

        Args:
            ll_1 (LinkedList): First LL to merge
            ll_2 (LinkedList): Second LL to merge

        Returns:
            Node: Head of the merged list
        """

        # Check if any of the given lists is empty
        if not ll_1.head:
            return ll_2.head
        elif not ll_2.head:
            return ll_1.head

        curr_1, curr_2 = ll_1.head, ll_2.head

        while curr_1 and curr_2:
            next_1, curr_1.next = curr_1.next, curr_2
            if next_1:
                next_2, curr_2.next = curr_2.next, next_1
            curr_1, curr_2 = next_1, next_2

        return ll_1.head
