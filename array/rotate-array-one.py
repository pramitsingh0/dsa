import unittest


def rotate_array(arr):
    if len(arr) < 1:
        return arr
    temp = arr[0]
    for i in range(len(arr) - 1):
        arr[i] = arr[i + 1]
    arr[len(arr) - 1] = temp
    return arr


class TestRotateArray(unittest.TestCase):
    def test_rotate_array(self):
        # Test case 1: Empty array
        arr = []
        expected = []
        self.assertEqual(rotate_array(arr), expected)

        # Test case 2: Array with one element
        arr = [1]
        expected = [1]
        self.assertEqual(rotate_array(arr), expected)

        # Test case 3: Array with multiple elements
        arr = [1, 2, 3, 4, 5]
        expected = [2, 3, 4, 5, 1]
        self.assertEqual(rotate_array(arr), expected)

        # Test case 4: Array with duplicate elements
        arr = [5, 5, 5, 5]
        expected = [5, 5, 5, 5]
        self.assertEqual(rotate_array(arr), expected)


if __name__ == "__main__":
    unittest.main()
