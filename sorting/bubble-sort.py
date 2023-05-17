import unittest


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr = swap(arr, j, j + 1)
    return arr


# Best case and worst case both (n^2)


class BubbleSortTest(unittest.TestCase):
    def test_bubble_sort(self):
        # Test case 1: Random numbers
        numbers = [5, 2, 8, 1, 9]
        expected_output = [1, 2, 5, 8, 9]
        self.assertEqual(bubble_sort(numbers), expected_output)

        # Test case 2: Already sorted list
        numbers = [1, 2, 3, 4, 5]
        expected_output = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(numbers), expected_output)

        # Test case 3: Reverse sorted list
        numbers = [9, 7, 5, 3, 1]
        expected_output = [1, 3, 5, 7, 9]
        self.assertEqual(bubble_sort(numbers), expected_output)

        # Test case 4: Empty list
        numbers = []
        expected_output = []
        self.assertEqual(bubble_sort(numbers), expected_output)

        # Test case 5: List with duplicate elements
        numbers = [5, 2, 8, 2, 9, 5]
        expected_output = [2, 2, 5, 5, 8, 9]
        self.assertEqual(bubble_sort(numbers), expected_output)

        # Test case 6: List with negative numbers
        numbers = [-5, -2, -8, -1, -9]
        expected_output = [-9, -8, -5, -2, -1]
        self.assertEqual(bubble_sort(numbers), expected_output)


if __name__ == "__main__":
    unittest.main()
