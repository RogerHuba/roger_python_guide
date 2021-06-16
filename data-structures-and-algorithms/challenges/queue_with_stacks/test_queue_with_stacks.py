import pytest

from .queue_with_stacks import PseudoQueue


class TestPseudoQueue:
    """PsuedoQueue Test class
    """
    @pytest.fixture()
    def queue(self):
        return PseudoQueue()

    def test_instance(self):
        assert PseudoQueue

    def test_enqueue(self, queue):
        """Test if the method returns added value and if the value is added to the queue
        """
        assert queue.enqueue(1) == 1
        assert len(queue) == 1
        assert queue.enqueue(2) == 2
        assert len(queue) == 2
        assert queue.enqueue(3) == 3
        assert len(queue) == 3
        assert queue.enqueue(4) == 4
        assert len(queue) == 4
        assert queue.enqueue(5) == 5
        assert len(queue) == 5

    def test_dequeue_error(self, queue):
        with pytest.raises(AttributeError) as err:
            assert queue.dequeue()
        assert str(err.value) == 'Cannot be called on empty queue'

    def test_dequeue(self, queue):
        """Test if the method works for any order of adding/removing elements
        """
        queue.enqueue(1)
        queue.enqueue(2)
        assert len(queue) == 2

        assert queue.dequeue() == 1
        assert len(queue) == 1

        queue.enqueue(3)
        queue.enqueue(4)
        assert len(queue) == 3

        assert queue.dequeue() == 2
        assert len(queue) == 2

        queue.enqueue(5)
        assert len(queue) == 3

        assert queue.dequeue() == 3
        assert queue.dequeue() == 4
        assert queue.dequeue() == 5
        assert len(queue) == 0
