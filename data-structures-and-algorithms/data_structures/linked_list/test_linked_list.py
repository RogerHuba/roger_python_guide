from data_structures.linked_list.linked_list import LinkedList, Node
import pytest


class TestNode:
    n1 = Node(3)
    n2 = Node('test')
    n3 = Node({'key': 'value'})
    n4 = Node(False)

    def test_node1_pass(self):
        assert (self.n1.val == 3 and self.n1.next is None)

    def test_node2_pass(self):
        assert (self.n2.val == 'test' and self.n2.next is None)

    def test_node3_pass(self):
        assert (self.n3.val == {'key': 'value'} and self.n3.next is None)

    def test_node4_pass(self):
        assert (self.n4.val == False and self.n4.next is None)


class TestLinkedList:
    ll1 = LinkedList()
    ll2 = LinkedList(1)

    def test_ll_1_pass(self):
        assert self.ll1.head == None

    def test_ll_2_pass(self):
        assert isinstance(self.ll2.head, Node)

    def test_ll_3_pass(self):
        assert self.ll2.head.val == 1

    def test_ll_4_pass(self):
        assert self.ll2.head.next == None

    def test_ll_insert_1_pass(self):
        self.ll1.insert(5)
        assert self.ll1.head.val == 5

    def test_ll_insert_2_pass(self):
        assert self.ll1.head.next == None

    def test_ll_insert_3_pass(self):
        self.ll1.insert(4)
        assert self.ll1.head.val == 4

    def test_ll_insert_4_pass(self):
        assert self.ll1.head.next.val == 5

    def test_ll_insert_5_pass(self):
        self.ll1.insert(3)
        assert self.ll1.head.val == 3

    def test_ll_insert_6_pass(self):
        assert self.ll1.head.next.val == 4

    def test_ll_includes_1_pass(self):
        assert self.ll1.includes(5) == True

    def test_ll_includes_2_pass(self):
        assert self.ll1.includes(4) == True

    def test_ll_includes_3_pass(self):
        assert self.ll1.includes(3) == True

    def test_ll_includes_4_pass(self):
        assert self.ll1.includes(1) == False

    def test_ll_str_1_pass(self):
        self.ll2.insert(2)
        self.ll2.insert(3)
        self.ll2.insert(4)
        self.ll2.insert(5)
        assert str(self.ll2) == '{5} -> {4} -> {3} -> {2} -> {1} -> None'


class TestLLInsertion:
    @pytest.fixture()
    def empty_ll(self):
        return LinkedList()

    @pytest.fixture()
    def ll(self):
        return LinkedList(1)

    def test_ll_append_edge_case(self, empty_ll):
        empty_ll.append(1)
        empty_ll.append(2)
        assert empty_ll.head.val == 1
        assert empty_ll.head.next.val == 2

    def test_ll_insert_before_1(self, empty_ll):
        """Assert it can handle an empty LL"""
        empty_ll.insert_before(1, 2)
        assert empty_ll.head is None

    def test_ll_insert_before_2(self, ll):
        """Assert it can replace the head"""
        ll.insert_before(1, 0)
        assert ll.head.val == 0
        assert ll.head.next.val == 1

    def test_ll_insert_before_3(self, ll):
        """Assert it works when the value doesn't exist in the list"""
        ll.insert_before(6, 0)
        assert ll.head.val == 1
        assert ll.head.next is None

    def test_ll_insert_after_1(self, empty_ll):
        """Assert it can handle an empty LL"""
        empty_ll.insert_after(0, 1)
        assert empty_ll.head is None

    def test_ll_insert_after_2(self, ll):
        """Assert it works when the value doesn't exist in the list"""
        ll.insert_after(6, 1)
        assert ll.head.val == 1

    def test_ll_insert_after_3(self, ll):
        """Assert it can handle an empty LL"""
        ll.insert_after(1, 2)
        assert ll.head.val == 1
        assert ll.head.next.val == 2

    def test_ll_insert_after_happy_path(self, ll):
        """Happy path"""
        ll.insert_after(1, 2)
        ll.insert_after(2, 3)
        ll.insert_after(3, 4)
        assert ll.head.val == 1
        assert ll.head.next.val == 2
        assert ll.head.next.next.val == 3
        assert ll.head.next.next.next.val == 4


class TestLLKthValue:
    @pytest.fixture()
    def empty_ll(self):
        return LinkedList()

    @pytest.fixture()
    def ll(self):
        return LinkedList(0)

    def test_ll_len_1(self, empty_ll, ll):
        assert empty_ll.ll_len() == 0
        assert ll.ll_len() == 1

    def test_ll_kth_exception_1(self, ll):
        with pytest.raises(Exception) as e:
            assert ll.kth_from_end_val(2.5)
        assert str(e.value) == 'k must be an integer'

    def test_ll_kth_exception_2(self, ll):
        with pytest.raises(Exception) as e:
            assert ll.kth_from_end_val(-2)
        assert str(e.value) == 'k must be greater than 0'

    def test_ll_kth_exception_3(self, ll):
        with pytest.raises(Exception) as e:
            assert ll.kth_from_end_val(2)
        assert str(e.value) == 'k must be less than the length of the list'

    def test_ll_kth_exception_happy_path_1(self, ll):
        assert ll.kth_from_end_val(0) == 0

    def test_ll_kth_exception_happy_path_2(self, ll):
        ll.insert(1)
        ll.insert(2)
        ll.insert(3)
        assert ll.kth_from_end_val(0) == 0
        assert ll.kth_from_end_val(1) == 1
        assert ll.kth_from_end_val(2) == 2
        assert ll.kth_from_end_val(3) == 3


class TestMergeLinkedLists:

    @pytest.fixture()
    def ll1(self):
        return LinkedList()

    @pytest.fixture()
    def ll2(self):
        return LinkedList()

    def test_both_ll_empty(self, ll1, ll2):
        assert LinkedList.mergeLists(ll1, ll2) == None

    def test_ll1_empty(self, ll1, ll2):
        ll2.append(1)
        ll2.append(2)
        ll2.append(3)
        merged_list = LinkedList.mergeLists(ll1, ll2)

        assert merged_list.val == 1
        assert merged_list.next.val == 2
        assert merged_list.next.next.val == 3

    def test_ll2_empty(self, ll1, ll2):
        ll1.append(1)
        ll1.append(2)
        ll1.append(3)
        merged_list = LinkedList.mergeLists(ll1, ll2)

        assert merged_list.val == 1
        assert merged_list.next.val == 2
        assert merged_list.next.next.val == 3

    def test_lists_equal_length(self, ll1, ll2):
        ll1.append(1)
        ll1.append(2)
        ll1.append(3)
        ll2.append(4)
        ll2.append(5)
        ll2.append(6)

        merged_list = LinkedList.mergeLists(ll1, ll2)

        assert merged_list.val == 1
        assert merged_list.next.val == 4
        assert merged_list.next.next.val == 2
        assert merged_list.next.next.next.val == 5
        assert merged_list.next.next.next.next.val == 3
        assert merged_list.next.next.next.next.next.val == 6

    def test_ll1_longer(self, ll1, ll2):
        ll1.append(1)
        ll1.append(2)
        ll1.append(3)
        ll1.append(4)
        ll2.append(5)
        ll2.append(6)

        merged_list = LinkedList.mergeLists(ll1, ll2)

        assert merged_list.val == 1
        assert merged_list.next.val == 5
        assert merged_list.next.next.val == 2
        assert merged_list.next.next.next.val == 6
        assert merged_list.next.next.next.next.val == 3
        assert merged_list.next.next.next.next.next.val == 4

    def test_ll2_longer(self, ll1, ll2):
        ll1.append(1)
        ll1.append(2)
        ll2.append(3)
        ll2.append(4)
        ll2.append(5)
        ll2.append(6)

        merged_list = LinkedList.mergeLists(ll1, ll2)

        assert merged_list.val == 1
        assert merged_list.next.val == 3
        assert merged_list.next.next.val == 2
        assert merged_list.next.next.next.val == 4
        assert merged_list.next.next.next.next.val == 5
        assert merged_list.next.next.next.next.next.val == 6
