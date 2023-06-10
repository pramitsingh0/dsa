import unittest


def union(arr1, arr2):
    aux_arr = []
    i = 0
    j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            if len(aux_arr) == 0 or aux_arr[-1] != arr1[i]:
                aux_arr.append(arr1[i])
            i += 1
        else:
            if len(aux_arr) == 0 or aux_arr[-1] != arr2[j]:
                aux_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        if aux_arr[-1] != arr1[i]:
            aux_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        if aux_arr[-1] != arr2[j]:
            aux_arr.append(arr2[j])
        j += 1

    return aux_arr


class UnionTestCase(unittest.TestCase):
    def test_union_with_common_elements(self):
        arr1 = [1, 2, 3, 4]
        arr2 = [3, 4, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(union(arr1, arr2), expected_result)

    def test_union_with_no_common_elements(self):
        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6]
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(union(arr1, arr2), expected_result)

    def test_union_with_duplicate_elements(self):
        arr1 = [1, 2, 2, 3]
        arr2 = [3, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(union(arr1, arr2), expected_result)


if __name__ == "__main__":
    unittest.main()
