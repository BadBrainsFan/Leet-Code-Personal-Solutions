class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previous = {}
        for index, item in enumerate(nums):
            value = target - item
            if value in previous:
                return [previous[value], index]
            previous[item] = index