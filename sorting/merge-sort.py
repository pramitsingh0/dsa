import unittest


def merge(arr1, arr2):
    aux_arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            aux_arr.append(arr1[i])
            i += 1
        else:
            aux_arr.append(arr2[j])
            j += 1
    aux_arr.extend(arr1[i:])
    aux_arr.extend(arr2[j:])
    return aux_arr


def merge_sort(arr):
    if len(arr) < 2:
        return arr
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    return merge(left_half, right_half)


class MergeSortTest(unittest.TestCase):
    def test_empty_list(self):
        arr = []
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [])

    def test_sorted_list(self):
        arr = [1, 2, 3, 4, 5]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        arr = [5, 4, 3, 2, 1]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        arr = [8, 3, 1, 7, 0, 2, 4, 6, 9, 5]
        sorted_arr = merge_sort(arr)
        self.assertEqual(sorted_arr, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
