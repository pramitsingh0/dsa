def find_leaders(nums):
    n = len(nums)
    i = n - 1
    curr_leader = nums[i]
    leader_arr = [curr_leader]
    while i >= 0:
        if nums[i] > curr_leader:
            leader_arr.append(nums[i])
            curr_leader = nums[i]
        i -= 1
    return leader_arr


find_leaders([10, 22, 12, 3, 0, 6])
