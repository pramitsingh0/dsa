import unittest
def left_rotate_array(nums, d):
    if len(nums) < 1:
        return nums
    d = d % len(nums)
    nums[:] =  nums[d:] + nums[:d]

class TestLeftRotation(unittest.TestCase):
    def test_left_rotate_array(self):
        arr = [1, 2, 3, 4, 5, 6]
        left_rotate_array(arr, 2)
        self.assertEqual(arr, [3, 4, 5, 6, 1, 2])

        arr = [7, 8, 9, 10, 11]
        left_rotate_array(arr, 3)
        self.assertEqual(arr, [10, 11, 7, 8, 9])

        arr = [0, 1, 2, 3, 4, 5]
        left_rotate_array(arr, 0)
        self.assertEqual(arr, [0, 1, 2, 3, 4, 5])

        arr = [1, 2, 3, 4, 5, 6]
        left_rotate_array(arr, 6)
        self.assertEqual(arr, [1, 2, 3, 4, 5, 6])

        arr = [1, 2, 3, 4, 5, 6]
        left_rotate_array(arr, 7)
        self.assertEqual(arr, [2, 3, 4, 5, 6, 1])

if __name__ == '__main__':
    unittest.main()