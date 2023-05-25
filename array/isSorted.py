import unittest


def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i + 1] < arr[i]:
            return False
    return True


def smallest(arr):
    smallest = None
    smallest_ind = None
    for i in range(len(arr)):
        if smallest == None and smallest_ind == None:
            smallest_ind = 0
            smallest = arr[0]
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_ind = i
    return smallest_ind


def is_rotated_and_sorted(nums):
    count = 0
    for i in range(len(nums)):
        if nums[i] > nums[(i + 1) % len(nums)]:
            count += 1
    return count <= 1


print(is_rotated_and_sorted([6, 20, 6]))


class TestIsSorted(unittest.TestCase):
    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertTrue(isSorted(arr), "Failed for sorted array")

    def test_unsorted_array(self):
        arr = [5, 3, 2, 4, 1]
        self.assertFalse(isSorted(arr), "Failed for unsorted array")

    def test_empty_array(self):
        arr = []
        self.assertTrue(isSorted(arr), "Failed for empty array")

    def test_single_element_array(self):
        arr = [42]
        self.assertTrue(isSorted(arr), "Failed for single element array")

    def test_duplicate_elements_array(self):
        arr = [1, 2, 2, 3, 4]
        self.assertTrue(isSorted(arr), "Failed for duplicate elements array")


if __name__ == "__main__":
    unittest.main()
