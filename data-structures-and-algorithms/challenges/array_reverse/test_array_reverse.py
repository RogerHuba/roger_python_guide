import unittest
from .array_reverse import reverse_array, reverse_array_in_place


class TestUnits(unittest.TestCase):
    def test_array_reverse(self):
        self.assertEqual(reverse_array([1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_array([]), [])
        self.assertEqual(reverse_array(
            [-5, -4, -3, -2, -1, 0]), [0, -1, -2, -3, -4, -5])

    def test_array_reverse_in_place(self):
        self.assertEqual(reverse_array_in_place(
            [1, 2, 3, 4, 5]), [5, 4, 3, 2, 1])
        self.assertEqual(reverse_array_in_place([]), [])
        self.assertEqual(reverse_array_in_place(
            [-5, -4, -3, -2, -1, 0]), [0, -1, -2, -3, -4, -5])
