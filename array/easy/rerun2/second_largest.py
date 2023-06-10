import unittest


def find_second_largest(arr):
    if len(arr) < 1:
        return -1
    largest = 0
    second_largest = 0

    for i in range(len(arr)):
        if arr[i] > largest:
            second_largest = largest
            largest = arr[i]
        elif arr[i] > second_largest and arr[i] < largest:
            second_largest = arr[i]
    return second_largest


class SecondLargestTestCase(unittest.TestCase):
    def test_second_largest(self):
        self.assertEqual(find_second_largest([1, 2, 3, 4, 5]), 4)
        self.assertEqual(find_second_largest([5, 4, 3, 2, 1]), 4)
        self.assertEqual(find_second_largest([1, 1, 1, 1, 1]), 1)
        self.assertEqual(find_second_largest([1, 1, 2, 2, 3]), 2)
        self.assertEqual(find_second_largest([5, 1, 3, 2, 4]), 4)


if __name__ == "__main__":
    unittest.main()
