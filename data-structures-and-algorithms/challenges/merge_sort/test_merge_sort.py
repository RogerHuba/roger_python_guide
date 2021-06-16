import pytest

from challenges.merge_sort.merge_sort import merge, merge_sort


class TestMergeSort:

    test_data = (
        # Empty list
        ([], []),

        # Positive values
        ([2, 6, 3, 8, 4, 8, 4, 1], [1, 2, 3, 4, 4, 6, 8, 8]),

        # Negative values
        ([-1, -5, -6, -8, -3, -6, -5], [-8, -6, -6, -5, -5, -3, -1]),

        # Mixed values
        ([0, 6, -1, 7, -9, 5, -8, 33, 8], [-9, -8, -1, 0, 5, 6, 7, 8, 33]),
    )

    def test_proof_of_life(self):
        assert merge
        assert merge_sort

    def test_merge(self):
        L = [1, 2, 5, 6]
        R = [3, 4, 7, 8]
        lst = [0] * 8
        expected = [1, 2, 3, 4, 5, 6, 7, 8]
        actual = merge(L, R, lst)
        assert actual == expected

    @pytest.mark.parametrize('lst, sorted_lst', test_data)
    def test_merge_sort(self, lst, sorted_lst):
        assert merge_sort(lst) == sorted_lst
