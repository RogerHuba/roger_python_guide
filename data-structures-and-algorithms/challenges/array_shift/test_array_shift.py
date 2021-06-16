import unittest
from .array_shift import insertShiftArray


class TestUnits(unittest.TestCase):
    def test_array_shift(self):
        self.assertEqual(insertShiftArray([1, 2, 3, 4], 5), [1, 2, 5, 3, 4])
        self.assertEqual(insertShiftArray([], 0), [0])
        self.assertEqual(insertShiftArray(
            [1, 2, 3, 4], 'a'), [1, 2, 'a', 3, 4])
        self.assertEqual(insertShiftArray([1], 5), [1, 5])
