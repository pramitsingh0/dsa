import unittest
def left_rotate_array(nums):
    if len(nums) < 1:
        return nums
    return nums[1:] + nums[:1]
class LeftRotateArrayTestCase(unittest.TestCase):
    def test_left_rotate_array(self):
        # Test case with positive integers
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(left_rotate_array(arr), [2, 3, 4, 5, 1])
        
        # Test case with negative integers
        arr = [-1, -2, -3, -4, -5]
        self.assertEqual(left_rotate_array(arr), [-2, -3, -4, -5, -1])
        
        # Test case with a single element
        arr = [10]
        self.assertEqual(left_rotate_array(arr), [10])
        
        # Test case with an empty array
        arr = []
        self.assertEqual(left_rotate_array(arr), [])
        
        # Test case with zero
        arr = [0, 1, 2, 3]
        self.assertEqual(left_rotate_array(arr), [1, 2, 3, 0])

if __name__ == '__main__':
    unittest.main()