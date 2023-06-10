import unittest


def remove_dups(nums):
    if len(nums) < 1:
        return 0
    i = 0
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1


class TestRemoveDups(unittest.TestCase):
    def test_remove_dups_empty_array(self):
        arr = []
        result = remove_dups(arr)
        self.assertEqual(result, 0)

    def test_remove_dups_no_duplicates(self):
        arr = [1, 2, 3, 4, 5]
        result = remove_dups(arr)
        self.assertEqual(result, 5)

    def test_remove_dups_with_duplicates(self):
        arr = [1, 2, 2, 3, 4, 4, 5]
        result = remove_dups(arr)
        self.assertEqual(result, 5)

    def test_remove_dups_all_duplicates(self):
        arr = [1, 1, 1, 1, 1]
        result = remove_dups(arr)
        self.assertEqual(result, 1)


if __name__ == "__main__":
    unittest.main()
