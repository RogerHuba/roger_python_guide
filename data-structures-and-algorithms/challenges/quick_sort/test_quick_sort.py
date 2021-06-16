import pytest
from challenges.quick_sort.quick_sort import quick_sort


class TestQuickSort:

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
        assert quick_sort

    @pytest.mark.parametrize('lst, sorted_lst', test_data)
    def test_quick_sort(self, lst, sorted_lst):
        assert quick_sort(lst) == sorted_lst
