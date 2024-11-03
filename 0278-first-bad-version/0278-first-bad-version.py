# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            mid_point = left + ((right-left)//2)
            if isBadVersion(mid_point): right = mid_point - 1
            else: left = mid_point + 1
        return left