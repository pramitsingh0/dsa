import unittest


def second_largest(nums):
    if len(nums) < 2:
        return -1
    largest = 0
    second_lar = 0
    for ele in nums:
        if ele > largest:
            second_lar = largest
            largest = ele
        elif ele > second_lar and ele != largest:
            second_lar = ele
    return second_lar


class SecondLargestTestCase(unittest.TestCase):
    def test_second_largest(self):
        self.assertEqual(second_largest([1, 2, 3, 4, 5]), 4)
        self.assertEqual(second_largest([5, 4, 3, 2, 1]), 4)
        self.assertEqual(second_largest([1, 1, 1, 1, 1]), 1)
        self.assertEqual(second_largest([1, 1, 2, 2, 3]), 2)
        self.assertEqual(second_largest([5, 1, 3, 2, 4]), 4)


if __name__ == "__main__":
    unittest.main()
