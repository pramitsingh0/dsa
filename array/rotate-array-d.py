import unittest


def rotate_array(nums, k):
    if len(nums) < 1:
        return []
    k = k % len(nums)
    nums[:] = nums[k:] + nums[:k]  # inplace edit
    return nums


class RotateArrayTests(unittest.TestCase):
    def test_rotate_array(self):
        # Test case 1
        arr1 = [1, 2, 3, 4, 5]
        k1 = 2
        expected1 = [3, 4, 5, 1, 2]
        self.assertEqual(rotate_array(arr1, k1), expected1)

        # Test case 2
        arr2 = ["a", "b", "c", "d"]
        k2 = 3
        expected2 = ["d", "a", "b", "c"]
        self.assertEqual(rotate_array(arr2, k2), expected2)

        # Test case 3 (edge case with empty array)
        arr3 = []
        k3 = 1
        expected3 = []
        self.assertEqual(rotate_array(arr3, k3), expected3)

        # Test case 4 (k larger than array length)
        arr4 = [1, 2, 3, 4, 5]
        k4 = 10
        expected4 = [1, 2, 3, 4, 5]
        self.assertEqual(rotate_array(arr4, k4), expected4)


if __name__ == "__main__":
    unittest.main()
