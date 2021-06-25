# import pytest
from demo.linked_list import LinkedList, Node


def test_instance():
    ll = LinkedList()
    assert ll.head == None


def test_insert_empty():
    ll = LinkedList()
    ll.insert("apples")
    assert ll.head.value == "apples"


def test_insert_full():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert ll.head.value == "bananas"
    assert ll.head.next.value == "apples"


def test_str():
    ll = LinkedList()
    ll.insert("apples")
    ll.insert("bananas")
    assert str(ll) == "{ bananas } -> { apples } -> NULL"


def test_node_exception():
    with pytest.raises(TypeError):
        Node("sample", "this is NOT a Node")