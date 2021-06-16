import pytest

from data_structures.stacks_and_queues.stacks_and_queues import Queue, Stack


class TestStack:
    """Test Stack class
    """
    @pytest.fixture()
    def stack(self):
        """
        Returns:
            [Stack]: Empty Stack instance
        """
        return Stack()

    def test_instantiation_empty(self):
        """Check if the class can successfully create empty instances
        """
        assert Stack

    def test_instantiation_not_empty(self):
        """Check if the class can successfully create non-empty instances
        """
        assert Stack(1).top.val == 1

    def test_repr(self, stack):
        """Check if the method returns correct formal string representation
        """
        assert repr(stack) == 'Stack()'

    def test_str(self, stack):
        """Check if the method returns correct informal string representation
        """
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        assert str(stack) == '(4) -> (3) -> (2) -> (1)'

    def test_push(self, stack):
        """Check if the push() method works for single and multiple values
        """
        assert stack.top is None

        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        stack.push(5)

        assert stack.top.val == 5
        assert stack.top.next.val == 4
        assert stack.top.next.next.val == 3
        assert stack.top.next.next.next.val == 2
        assert stack.top.next.next.next.next.val == 1

    def test_pop_error(self, stack):
        """Check if the method raises the error when called on empty stack
        """
        with pytest.raises(AttributeError) as err:
            assert stack.pop()
        assert str(err.value) == 'Cannot be called on empty stack'

    def test_pop(self, stack):
        """Check if the pop() method returns expected values and can succesfully empty the stack
        """
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        assert stack.pop() == 4
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert stack.pop() == 1
        assert stack.top is None

    def test_peek_error(self, stack):
        """Check if the method raises the error when called on empty stack
        """
        with pytest.raises(AttributeError) as err:
            assert stack.pop()
        assert str(err.value) == 'Cannot be called on empty stack'

    def test_peek(self, stack):
        """Check if the method can successfully peek the next item on the stack
        """
        stack.push(1)
        assert stack.peek() == 1
        stack.push(2)
        assert stack.peek() == 2
        stack.push(3)
        assert stack.peek() == 3
        stack.push(4)
        assert stack.peek() == 4


class TestQueue:
    """Test Queue class
    """
    @pytest.fixture()
    def queue(self):
        """
        Returns:
            [Stack]: Empty Queue instance
        """
        return Queue()

    def test_instantiation_empty(self):
        """Check if the class can successfully create empty instances
        """
        assert Queue

    def test_instantiation_not_empty(self):
        """Check if the class can successfully create non-empty instances
        """
        assert Queue(1).front.val == 1

    def test_repr(self, queue):
        """Check if the method returns correct formal string representation
        """
        assert repr(queue) == 'Queue()'

    def test_str(self, queue):
        """Check if the method returns correct informal string representation
        """
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        assert str(queue) == 'Front: (1) -> (2) -> (3) -> (4) :Rear'

    def test_enqueue(self, queue):
        """Check if the enqueue() method works for single and multiple values
        """
        queue.enqueue(1)
        assert queue.front.val == queue.rear.val == 1

        queue.enqueue(2)
        assert queue.front.val == 1
        assert queue.rear.val == 2

        queue.enqueue(3)
        assert queue.front.val == 1
        assert queue.rear.val == 3

        queue.enqueue(4)
        assert queue.front.val == 1
        assert queue.rear.val == 4

    def test_dequeue_error(self, queue):
        """Check if the method raises the error when called on empty Queue
        """
        with pytest.raises(AttributeError) as err:
            assert queue.dequeue()
        assert str(err.value) == 'Cannot be called on empty Queue'

    def test_dequeue(self, queue):
        """Check if the enqueue() method returns expected values and can succesfully empty the stack
        """
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)

        assert queue.dequeue() == 1
        assert queue.dequeue() == 2
        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5

    def test_peek_error(self, queue):
        """Check if the method raises the error when called on empty Queue
        """
        with pytest.raises(AttributeError) as err:
            assert queue.peek()
        assert str(err.value) == 'Cannot be called on empty Queue'

    def test_peek(self, queue):
        """Check if the method can successfully peek the next item in queue
        """
        queue.enqueue(1)
        assert queue.peek() == 1

        queue.enqueue(2)
        assert queue.peek() == 1
