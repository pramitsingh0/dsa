import unittest
def remove_duplicates(nums):
    if len(nums) < 1:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1


class RemoveDuplicatesTestCase(unittest.TestCase):
    def test_remove_duplicates(self):
        # Test case with duplicates
        nums = [1, 1, 2]
        self.assertEqual(remove_duplicates(nums), 2)
        self.assertEqual(nums[:2], [1, 2])  # Check modified array
        
        # Test case with no duplicates
        nums = [1, 2, 3]
        self.assertEqual(remove_duplicates(nums), 3)
        self.assertEqual(nums[:3], [1, 2, 3])  # Check unchanged array
        
        # Test case with empty array
        nums = []
        self.assertEqual(remove_duplicates(nums), 0)
        self.assertEqual(nums, [])  # Check unchanged array
        
        # Test case with all duplicates
        nums = [1, 1, 1, 1, 1]
        self.assertEqual(remove_duplicates(nums), 1)
        self.assertEqual(nums[:1], [1])  # Check modified array

if __name__ == '__main__':
    unittest.main()