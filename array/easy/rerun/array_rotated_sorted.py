import unittest
def rotated_sorted(nums):
    if len(nums) < 1:
        return False
    count = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i + 1) % len(nums)]:
            count += 1

    return count <= 1

class RotatedSortedTestCase(unittest.TestCase):
    def test_rotated_sorted(self):
        self.assertTrue(rotated_sorted([4, 5, 6, 7, 1, 2, 3]))  # Rotated sorted array
        self.assertTrue(rotated_sorted([1, 2, 3, 4, 5, 6, 7]))  # Non-rotated sorted array
        self.assertFalse(rotated_sorted([7, 6, 5, 4, 3, 2, 1]))  # Reverse sorted array
        self.assertTrue(rotated_sorted([2, 3, 4, 5, 6, 1]))  # Not rotated sorted array
        self.assertFalse(rotated_sorted([]))  # Empty array

if __name__ == '__main__':
    unittest.main()