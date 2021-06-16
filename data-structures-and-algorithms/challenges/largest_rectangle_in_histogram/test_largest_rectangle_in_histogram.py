from .largest_rectangle_in_histogram import get_max_area


class TestLargestRectangle:
    def test_proof_of_life(self):
        assert get_max_area

    def test_get_max_area_pass(self):
        histogram = [2, 1, 5, 6, 2, 3]
        assert get_max_area(histogram) == 10

    def test_get_max_area_pass_empty_list(self):
        histogram = []
        assert get_max_area(histogram) == 0

    def test_get_max_area_pass_negative(self):
        histogram = [-1,-2,-3,-4]
        # Negative values make no sense => area = 0
        assert get_max_area(histogram) == 0
