import unittest

from ..eratosthenes import eratosthenes


class TestEratosthenes(unittest.TestCase):
    def setUp(self):
        self.sequence = range(2, 101)

    def test_era(self):
        expected_nums = [
            2, 3, 5, 7, 11, 13, 17, 19,
            23, 29, 31, 37, 41, 43, 47,
            53, 59, 61, 67, 71, 73, 79,
            83, 89, 97
        ]

        nums = eratosthenes(self.sequence)

        self.assertItemsEqual(nums, expected_nums)


if __name__ == '__main__':
    unittest.main()
