import unittest


# def largest(arr):
#     largest = None
#     for ele in arr:
#         if largest == None:
#             largest = arr[0]
#             continue
#         if ele > largest:
#             largest = ele
#     return largest
#
#
# def find_second_largest(arr):
#     if len(arr) < 2:
#         raise ValueError("Array must have at least two elements")
#     first_largest = largest(arr)
#     second_largest = None
#     for ele in arr:
#         if second_largest == None:
#             second_largest = arr[0]
#             continue
#         if ele > second_largest and ele < first_largest:
#             second_largest = ele
#     return second_largest


def find_second_largest(arr):
    if len(arr) < 2:
        raise ValueError("Array must have at least two elements")
    largest = arr[0]
    second_largest = arr[0]
    for ele in arr:
        if ele > largest:
            second_largest = largest
            largest = ele
        elif ele > second_largest and ele != largest:
            second_largest = ele
    return second_largest


class SecondLargestTestCase(unittest.TestCase):
    def test_second_largest(self):
        # Test case with positive integers
        arr = [3, 5, 2, 9, 6]
        self.assertEqual(find_second_largest(arr), 6)

        # Test case with negative integers
        arr = [-7, -3, -5, -1]
        self.assertEqual(find_second_largest(arr), -3)

        # Test case with duplicate values
        arr = [5, 5, 5, 5, 5]
        self.assertEqual(find_second_largest(arr), 5)

    def test_array_length_less_than_two(self):
        # Test case with an array of length less than two
        arr = [1]
        with self.assertRaises(ValueError):
            find_second_largest(arr)

    def test_empty_array(self):
        # Test case with an empty array
        arr = []
        with self.assertRaises(ValueError):
            find_second_largest(arr)


if __name__ == "__main__":
    unittest.main()
