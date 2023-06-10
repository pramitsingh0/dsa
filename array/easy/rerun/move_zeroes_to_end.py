import unittest
def move_zeroes(nums):
    k = 0
    while k < len(nums):
        if nums[k] == 0:
            break
        k += 1
    i = k
    j = k + 1
    while i < len(nums) and j < len(nums):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1
    return nums
def move_zeros(nums):
    natural_nums = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[natural_nums] = nums[i]
            natural_nums += 1
    for i in range(natural_nums, len(nums)):
        nums[i] = 0


class TestMoveZeros(unittest.TestCase):
    def test_move_zeros(self):
        arr = [0, 1, 0, 3, 12]
        move_zeros(arr)
        self.assertEqual(arr, [1, 3, 12, 0, 0])

        arr = [4, 2, 0, 5, 0, 1, 0]
        move_zeros(arr)
        self.assertEqual(arr, [4, 2, 5, 1, 0, 0, 0])

        arr = [0, 0, 0, 0, 0]
        move_zeros(arr)
        self.assertEqual(arr, [0, 0, 0, 0, 0])

        arr = [1, 2, 3, 4, 5]
        move_zeros(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

        arr = [-1, -2, 0, 0, 4, 0, 5, 0, 1, 0]
        move_zeros(arr)
        self.assertEqual(arr, [-1, -2, 4, 5, 1, 0, 0, 0, 0, 0])

if __name__ == '__main__':
    unittest.main()