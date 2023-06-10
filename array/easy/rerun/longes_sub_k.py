def longest_subarray_sum(arr, k):
    prefix_sum = {}
    sum = 0
    longest = 0
    for i in range(len(arr)):
        sum += arr[i]
        prefix_sum[sum] = i
        if sum == k:
            longest = i + 1
        elif sum > k:
            prev_sum = sum - k
            if prev_sum in prefix_sum:
                diff = i - prefix_sum[prev_sum]
                if diff > longest:
                    longest = diff
    print(longest)
    return longest


# Unit tests
def run_tests():
    # Test 1: Basic test case with a subarray summing up to k = 7
    arr1 = [3, 4, 7, 2, -3, 1, 4, 2]
    k1 = 7
    assert longest_subarray_sum(arr1, k1) == 4

    # Test 2: No subarray sums up to k = 10
    arr2 = [1, 2, 3, 4, 5]
    k2 = 10
    assert longest_subarray_sum(arr2, k2) == 0

    # Test 3: Subarray with a negative sum (-4) sums up to k = 0
    arr3 = [3, -4, 2, 1, -1, 6]
    k3 = 0
    assert longest_subarray_sum(arr3, k3) == 4

    # Test 4: Empty array, so no subarray sum can be found
    arr4 = []
    k4 = 5
    assert longest_subarray_sum(arr4, k4) == 0

    # Test 5: Subarray with a single element sums up to k = 8
    arr5 = [8, 5, 2, 3, 1]
    k5 = 8
    assert longest_subarray_sum(arr5, k5) == 1

    print("All tests passed!")


run_tests()