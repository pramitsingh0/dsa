import unittest
def find_missing_number(n, arr):
    expected_sum = n * (n + 1) / 2
    actual_sum = sum(arr)
    return int(expected_sum - actual_sum)

class TestFindMissingNumber(unittest.TestCase):
    def test_find_missing_number(self):
        N = 5
        arr = [1, 2, 4, 5]
        self.assertEqual(find_missing_number(N, arr), 3)

        N = 8
        arr = [3, 6, 2, 1, 7, 5, 8]
        self.assertEqual(find_missing_number(N, arr), 4)

        N = 10
        arr = [5, 6, 2, 1, 9, 8, 4, 7, 3]
        self.assertEqual(find_missing_number(N, arr), 10)

        N = 4
        arr = [2, 3, 4]
        self.assertEqual(find_missing_number(N, arr), 1)

        N = 3
        arr = [2, 1]
        self.assertEqual(find_missing_number(N, arr), 3)

if __name__ == '__main__':
    unittest.main()