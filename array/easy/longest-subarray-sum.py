def get_longest(nums, k):
    i = 0
    largest_sub = 0
    while i < len(nums):
        sum = 0
        j = i
        while sum < k and j < len(nums):
            sum += nums[j]
            j += 1
        if sum == k:
            if (j - i + 1) > largest_sub:
                largest_sub = j - i
        i += 1
    return largest_sub


# Optimal solution
def longest_subarray_sum(nums, k):
    prefix_sum = {}
    sum = 0
    longest = 0
    for i in range(len(nums)):
        sum += nums[i]
        prefix_sum[sum] = i
        if sum == k:
            longest = i + 1
        elif sum > k:
            prev_sum = sum - k
            if prev_sum in prefix_sum:
                diff = i - prefix_sum[prev_sum]
                if diff > longest:
                    longest = diff
    return longest


def test_longest_subarray_sum():
    # Test case 1: Example given in the question
    array1 = [1, -1, 5, -2, 3]
    k1 = 3
    assert longest_subarray_sum(array1, k1) == 4

    # Test case 2: Subarray with sum k at the beginning
    array2 = [3, 4, 5, -2, 1, 7]
    k2 = 12
    assert longest_subarray_sum(array2, k2) == 3

    # Test case 3: Subarray with sum k at the end
    array3 = [2, 4, 1, 3, 6, 8]
    k3 = 18
    assert longest_subarray_sum(array3, k3) == 2

    # Test case 4: Subarray with negative numbers
    array4 = [-1, -2, -3, -4, -5]
    k4 = -8
    assert longest_subarray_sum(array4, k4) == 3

    # Test case 5: No subarray with sum k
    array5 = [1, 2, 3, 4, 5]
    k5 = 10
    assert longest_subarray_sum(array5, k5) == 0

    # Test case 6: Empty array
    array6 = []
    k6 = 5
    assert longest_subarray_sum(array6, k6) == 0

    # Test case 7: Array with only one element
    array7 = [10]
    k7 = 10
    assert longest_subarray_sum(array7, k7) == 1

    print("All test cases pass")


# Run the unit tests
test_longest_subarray_sum()


print(get_longest_opt([2, 3, 5, 1, 9], 5))
