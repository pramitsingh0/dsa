import math


def condition(piles, speed, h) -> bool:
    return sum(math.ceil(pile / speed) for pile in piles) <= h


def minEatingSpeed(piles, h):
    low = 1
    high = max(piles)
    while low < high:
        mid = low + (high - low) // 2
        if condition(piles, speed=mid, h=h):
            high = mid
        else:
            low = mid + 1
    return low


print(minEatingSpeed([3, 6, 7, 11], 8))
