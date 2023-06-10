class Solution:
    def binSearch(self, nums: list[int], target: int, leftBias: bool):
        i = -1
        left = 0
        right = len(nums)

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                i = mid
                if leftBias:
                    right = mid - 1
                else:
                    left = mid + 1
        return i
                
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        start = self.binSearch(self, nums, target, leftBias=True)
        end = self.binSearch(self, nums, target, False)
        return (end - start) + 1
    
nums = [2, 2 , 3 , 3 , 3 , 3 , 4]
target = 3

print(Solution.searchRange(Solution, nums, target))