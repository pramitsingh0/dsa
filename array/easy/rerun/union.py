import unittest


def find_union(arr1, arr2):
    i = 0
    j = 0
    aux_arr = []
    while i < len(arr1) and j < len(arr2):
        print(i, j)
        if arr1[i] < arr2[j]:
            if len(aux_arr) == 0 or aux_arr[-1] != arr1[i]:
                aux_arr.append(arr1[i])
                i += 1
        elif arr1[i] > arr2[j]:
            if len(aux_arr) == 0 or aux_arr[-1] != arr2[j]:
                aux_arr.append(arr2[j])
                j += 1
        else:
            if len(aux_arr) == 0 or aux_arr[-1] != arr2[j]:
                aux_arr.append(arr1[i])
                i += 1
                j += 1
    while i < len(arr1):
        if len(aux_arr) == 0 or aux_arr[-1] != arr1[i]:
            aux_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        if len(aux_arr) == 0 or aux_arr[-1] != arr2[j]:
            aux_arr.append(arr2[j])
        j += 1

    return aux_arr


class TestFindUnion(unittest.TestCase):
    def test_find_union(self):
        arr1 = [1, 2, 3, 4, 5]
        arr2 = [4, 5, 6, 7, 8]
        self.assertEqual(find_union(arr1, arr2), [1, 2, 3, 4, 5, 6, 7, 8])

        arr1 = [1, 2, 4, 5, 6]
        arr2 = [3, 5, 7, 8]
        self.assertEqual(find_union(arr1, arr2), [1, 2, 3, 4, 5, 6, 7, 8])

        arr1 = [1, 3, 5, 7, 9]
        arr2 = [2, 4, 6, 8, 10]
        self.assertEqual(find_union(arr1, arr2), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        arr1 = [1, 2, 3]
        arr2 = [4, 5, 6, 7, 8]
        self.assertEqual(find_union(arr1, arr2), [1, 2, 3, 4, 5, 6, 7, 8])

        arr1 = []
        arr2 = [1, 2, 3]
        self.assertEqual(find_union(arr1, arr2), [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
