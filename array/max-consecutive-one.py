import unittest


def max_consecutive(arr):
    max = 0
    count = 0
    for ele in arr:
        if ele == 1:
            count += 1
            max = count if count > max else max
        else:
            count = 0

    return max


class MaxConsecutiveTestCase(unittest.TestCase):
    def test_max_consecutive(self):
        # Test case where the maximum consecutive ones is 3
        nums = [1, 1, 0, 1, 1, 1, 0, 0, 1]
        self.assertEqual(max_consecutive(nums), 3)

        # Test case where the maximum consecutive ones is 2
        nums = [1, 0, 1, 1, 0, 1, 1, 1]
        self.assertEqual(max_consecutive(nums), 3)

        # Test case where there are no consecutive ones
        nums = [0, 0, 0, 0, 0, 0]
        self.assertEqual(max_consecutive(nums), 0)

        # Test case where the input array is empty
        nums = []
        self.assertEqual(max_consecutive(nums), 0)

        # Test case where the input array has only one element (0)
        nums = [0]
        self.assertEqual(max_consecutive(nums), 0)

        # Test case where the input array has only one element (1)
        nums = [1]
        self.assertEqual(max_consecutive(nums), 1)


if __name__ == "__main__":
    unittest.main()
