class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        
        for index, item in enumerate(nums):
            delta = target - item
            if delta in previous:
                return [previous[delta], index]
            previous[item] = index