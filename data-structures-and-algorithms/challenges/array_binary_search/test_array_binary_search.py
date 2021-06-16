from .array_binary_search import binary_search


class TestBinarySearch:
    arr_small = [i for i in range(100)]
    arr_medium = [i for i in range(10000)]
    arr_big = [i for i in range(100000)]

    # PASS
    def test_pass_small_1(self):
        target = 30
        expected = 30
        actual = binary_search(self.arr_small, target)
        assert actual == expected

    def test_pass_small_2(self):
        target = 3000
        expected = -1
        actual = binary_search(self.arr_small, target)
        assert actual == expected

    def test_pass_medium_1(self):
        target = 3000
        expected = 3000
        actual = binary_search(self.arr_medium, target)
        assert actual == expected

    def test_pass_medium_2(self):
        target = 30000
        expected = -1
        actual = binary_search(self.arr_medium, target)
        assert actual == expected

    def test_pass_big_1(self):
        target = 30000
        expected = 30000
        actual = binary_search(self.arr_big, target)
        assert actual == expected

    def test_pass_big_2(self):
        target = -5
        expected = -1
        actual = binary_search(self.arr_big, target)
        assert actual == expected

    # EDGE CASES
    def test_edge_small_1(self):
        target = 0
        expected = 0
        actual = binary_search(self.arr_small, target)
        assert actual == expected

    def test_edge_small_2(self):
        target = 99
        expected = 99
        actual = binary_search(self.arr_small, target)
        assert actual == expected

    def test_edge_small_3(self):
        target = 50
        expected = 50
        actual = binary_search(self.arr_small, target)
        assert actual == expected

    # FAIL
    def test_fail_small(self):
        target = 30
        expected = 29
        actual = binary_search(self.arr_small, target)
        assert actual != expected
