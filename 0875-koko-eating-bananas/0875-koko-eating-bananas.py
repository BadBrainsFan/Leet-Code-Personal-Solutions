class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid_point = left + ((right-left)//2)
            hours = sum((pile + mid_point - 1 ) // mid_point for pile in piles)
            if hours > h:
                left = mid_point + 1
            else:
                right = mid_point
        return left