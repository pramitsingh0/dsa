import unittest


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def insertionSort(nums):
    n = len(nums)
    for i in range(1, n):
        curr_ele = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > curr_ele:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = curr_ele


print(insertionSort([5, 4, 3, 1, 2, 7]))


class InsertionSortTestCase(unittest.TestCase):
    def test_sort_empty_list(self):
        arr = []
        insertion_sort(arr)
        self.assertEqual(arr, [])

    def test_sort_already_sorted(self):
        arr = [1, 2, 3, 4, 5]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_sort_reverse_order(self):
        arr = [5, 4, 3, 2, 1]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_sort_random_order(self):
        arr = [3, 5, 1, 2, 4]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_sort_duplicates(self):
        arr = [3, 5, 1, 2, 4, 3]
        insertion_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 3, 4, 5])
