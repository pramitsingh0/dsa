class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev = 0
        iterator = x
        if x < 0: return False
        while iterator > 0:
            rev = rev * 10 + (iterator % 10);
            iterator //= 10
        return rev == x if x > (-2**31 - 1) and x < (2 ** 31 - 2) else False

things = Solution()

print(things.isPalindrome(12321))

