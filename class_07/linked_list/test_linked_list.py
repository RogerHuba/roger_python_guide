import pytest
from linked_list import LinkedList, TargetError


def test_insert():
    linked_list = LinkedList()

    assert str(linked_list) == ""

    linked_list.insert("apple")

    assert str(linked_list) == "[apple],"

    linked_list.insert("banana")

    assert str(linked_list) == "[banana],[apple],"


def test_includes():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")

    assert not linked_list.includes("cucumber")


def test_append():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.append("cucumber")

    assert str(linked_list) == "[banana],[apple],[cucumber],"


def test_insert_before():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "[banana],[cucumber],[apple],"

def test_insert_before_first():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert_before("apple", "cucumber")

    assert str(linked_list) == "[cucumber],[apple],"

def test_insert_after():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    linked_list.insert_after("banana", "cucumber")

    assert str(linked_list) == "[banana],[cucumber],[apple],"


def test_insert_before_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


def test_insert_before_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_before("radish", "zucchinni")


def test_insert_after_empty():
    linked_list = LinkedList()

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


def test_insert_after_missing():
    linked_list = LinkedList()

    linked_list.insert("banana")

    with pytest.raises(TargetError):
        linked_list.insert_after("radish", "zucchinni")


def test_kth_from_end_zero():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.kth_from_end(0)
    expected = "cucumbers"
    assert actual == expected


def test_kth_from_end_one():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.kth_from_end(1)
    expected = "bananas"
    assert actual == expected


def test_kth_from_end_two():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])
    actual = linked_list.kth_from_end(2)
    expected = "apples"
    assert actual == expected


def test_kth_from_end_out_of_range():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])

    with pytest.raises(TargetError):
        linked_list.kth_from_end(3)


def test_kth_from_end_under_range():
    linked_list = LinkedList(values=["apples", "bananas", "cucumbers"])

    with pytest.raises(TargetError):
        linked_list.kth_from_end(-1)


def test_kth_from_end_size_one():
    linked_list = LinkedList(values=["apples"])
    actual = linked_list.kth_from_end(0)
    expected = "apples"
    assert actual == expected
