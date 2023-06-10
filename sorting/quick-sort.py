import unittest


def partition(arr, low, high):
    pivot_ind = len(arr) // 2
    pivot = arr[pivot_ind]
    arr[high], arr[pivot_ind] = arr[pivot_ind], arr[high]
    i = low
    j = high - 1
    while i < j:
        while arr[i] <= pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[high] = arr[high], arr[i]
    return i


def quick_sort(arr, low, high):
    if low < high:
        partition_ind = partition(arr, low, high)
        quick_sort(arr, low, partition_ind - 1)
        quick_sort(arr, partition_ind + 1, high)


# def quick_sort(arr):
#     if len(arr) < 2:
#         return arr
#
#     pivot = arr[0]
#     lesser_half = [x for x in arr[1:] if x <= pivot]
#     greater_half = [x for x in arr[1:] if x > pivot]
#     return quick_sort(lesser_half) + [pivot] + quick_sort(greater_half)


class QuickSortTests(unittest.TestCase):
    def test_quick_sort(self):
        arr = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
        low = 0
        high = len(arr) - 1
        quick_sort(arr, low, high)
        self.assertEqual(arr, [2, 3, 5, 6, 7, 9, 10, 11, 12, 14])

    def test_quick_sort_with_duplicates(self):
        arr = [5, 5, 3, 2, 8, 2, 1]
        low = 0
        high = len(arr) - 1
        quick_sort(arr, low, high)
        self.assertEqual(arr, [1, 2, 2, 3, 5, 5, 8])

    def test_quick_sort_with_single_element(self):
        arr = [9]
        low = 0
        high = len(arr) - 1
        quick_sort(arr, low, high)
        self.assertEqual(arr, [9])

    def test_quick_sort_with_empty_array(self):
        arr = []
        low = 0
        high = len(arr) - 1
        quick_sort(arr, low, high)
        self.assertEqual(arr, [])


if __name__ == "__main__":
    unittest.main()
