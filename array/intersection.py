import unittest


def intersection(arr1, arr2):
    i = 0
    j = 0
    aux_arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr1[i] > arr2[j]:
            j += 1
        else:
            aux_arr.append(arr1[i])
            i += 1
            j += 1
    return aux_arr


class TestIntersection(unittest.TestCase):
    def test_intersection_empty_arrays(self):
        arr1 = []
        arr2 = []
        result = intersection(arr1, arr2)
        self.assertEqual(result, [])

    def test_intersection_no_common_elements(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        result = intersection(arr1, arr2)
        self.assertEqual(result, [])

    def test_intersection_common_elements(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [4, 5, 6, 7, 8]
        result = intersection(arr1, arr2)
        self.assertEqual(result, [4, 5])

    def test_intersection_duplicate_elements(self):
        arr1 = [1, 2, 2, 3, 4, 4]
        arr2 = [3, 4, 4, 5, 6]
        result = intersection(arr1, arr2)
        self.assertEqual(result, [3, 4, 4])


if __name__ == "__main__":
    unittest.main()
